#!/usr/bin/env python3
__author__ = 'Derek King'

# Basic saving and loading settings to/from a file

from configparser import SafeConfigParser
def save_settings(settings_file, width, height):
    parser = SafeConfigParser()
    parser.add_section("Display")
    parser.set("Display", "width", str(width))
    parser.set("Display", "height", str(height))

    with open(settings_file, "w") as f:
        parser.write(f)

def load_settings(settings_file):
    # Use these defaults if the settings file is missing or doesn't contain the options
    width = 1024
    height = 720

    parser = SafeConfigParser()
    found = parser.read(settings_file)
    if found and parser.has_section("Display"):
        if parser.has_option("Display", "width"):
            width = parser.getint("Display", "width")
        if parser.has_option("Display", "height"):
            height = parser.getint("Display", "height")
    else:
        save_settings(settings_file, width, height)

    return width, height

def setup():
    settings_file = "settings.ini"
    width, height = load_settings(settings_file)