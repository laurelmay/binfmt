#!/usr/bin/env bash

if [ "$UID" -ne 0 ]; then
    echo "This must be run as root"
    exit 1
fi

wrapper="/usr/local/bin/ktsrun"
extension="kts"
name="kotlin_script"
script=$(cat <<EOF
#!/bin/sh

kotlinc -script "\$@"
EOF
)

# Write the configuration file
echo ":${name}:E::${extension}::${wrapper}:OC" > /etc/binfmt.d/"${name}".conf

# Write the wrapper script
echo "$script" > "$wrapper"
chmod +x "$wrapper"

if ! which kotlinc &> /dev/null; then
    echo "kotlinc does not appear to be installed. This will be necessary in"
    echo "order to run .kts files"
fi

# Restart the systemd service
systemctl restart systemd-binfmt.service
