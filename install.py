#!/usr/bin/env python3

"""
Install script for my binfmt_misc formats.
"""

import os
import shutil
import subprocess
import sys

import yaml


WRAPPER_DIR = "/usr/local/bin"
BINFMT_DIR = "/etc/binfmt.d"


def load_configs():
    """
    Load the format configurations. This finds everything in the formats/
    directory and then opens them and parses them as YAML.
    """

    configs = ["formats/%s" % format for format in os.listdir("formats")
               if format.endswith(".yml")]
    formats = []
    for config in configs:
        with open(config, "r") as format:
            formats.append(yaml.safe_load(format))
    return formats


def generate_wrapper(config):
    """
    Generates a wrapper script for the format.

    :param config: The configuration for the format
    """

    return "#!/bin/sh\n%s" % config['interpreter']


def generate_binfmt_config(config):
    """
    Generates a binfmt_misc config that goes in /etc/binfmt.d.

    :param config: The configuration for the format
    """

    return (
        ":%s:E::%s::%s/%s:OC"
        % (
            config['name'], config['extension'],
            WRAPPER_DIR, config['wrapper_name']
        )
    )

def check_dependencies(config):
    """
    Checks the dependencies for the format and prints messages if any of
    them are not met. This does not stop the install from happening.

    :param config: The configuration for the format
    """

    if 'dependencies' not in config or not config['dependencies']:
        return

    for dependency in config['dependencies']:
        if 'software' in dependency:
            if not shutil.which(dependency['software']):
                print("  %s is not installed. This is required for %s files"
                      % (dependency['software'], config['extension']))
        elif 'file' in dependency:
            if not os.path.isfile(dependency['file']):
                print("  Cannot find %s. This is required for %s files"
                      % dependency['file'], config['extension'])


def write_binfmt_config(file_name, contents):
    """
    Writes the config in /etc/binfmt.d

    :param file_name: The name of the configuration file
    :param contents: The contents of the configuration file
    """

    with open(file_name, "w+") as binfmt_file:
        print(contents, file=binfmt_file)


def write_wrapper(file_name, contents):
    """
    Writes the wrapper file.

    :param file_name: The name of the file to write to
    :param contents: The contents of the wrapper
    """

    with open(file_name, "w+") as wrapper_file:
        print(contents, file=wrapper_file)
    os.chmod(file_name, 0o755)


def main():
    if os.geteuid() != 0:
        exit("This script must be run with root privileges.")
    for config in load_configs():
        print("Installing: %s" % config['name'])
        wrapper_file = "%s/%s" % (WRAPPER_DIR, config['wrapper_name'])
        wrapper_contents = generate_wrapper(config)
        binfmt_file = "%s/%s.conf" % (BINFMT_DIR, config['name'])
        binfmt_contents = generate_binfmt_config(config)
        check_dependencies(config)
        write_binfmt_config(binfmt_file, binfmt_contents)
        write_wrapper(wrapper_file, wrapper_contents)
    subprocess.call(['systemctl', 'restart', 'systemd-binfmt.service'])


if __name__ == '__main__':
    main()
