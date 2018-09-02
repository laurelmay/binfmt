#!/usr/bin/env bash

if [ "$UID" -ne 0 ]; then
    echo "This must be run as root"
    exit 1
fi

wrapper="/usr/local/bin/decafrun"
extension="decaf"
name="decaf"
script=$(cat <<EOF
#!/bin/sh

decaf_jar="/opt/decaf-1.0.jar"
java -jar "\$decaf_jar" -i "\$1"
EOF
)

# Write the configuration file
echo ":${name}:E::${extension}::${wrapper}:OC" > /etc/binfmt.d/"${name}".conf

# Write the wrapper script
echo "$script" > "$wrapper"
chmod +x "$wrapper"

# Write message to user
if [ ! -f "/opt/decaf-1.0.jar" ]; then
    echo "The decaf reference solution must be placed at: /opt/decaf-1.0.jar"
    echo "before executing decaf files will be possible"
fi

# Restart the systemd service
systemctl restart systemd-binfmt.service
