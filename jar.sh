#!/usr/bin/env bash

if [ "$UID" -ne 0 ]; then
    echo "This must be run as root"
    exit 1
fi

wrapper="/usr/local/bin/jarwrapper"
extension="jar"
name="jar"
script=$(cat <<EOF
#!/bin/sh

java -jar "\$@"
EOF
)

# Write the configuration file
echo ":${name}:E::${extension}::${wrapper}:OC" > /etc/binfmt.d/"${name}".conf

# Write the wrapper script
echo "$script" > "$wrapper"
chmod +x "$wrapper"

# Restart the systemd service
systemctl restart systemd-binfmt.service
