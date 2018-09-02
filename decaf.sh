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

# Restart the systemd service
systemctl restart systemd-binfmt.service
