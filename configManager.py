from configparser import ConfigParser


def save_config(config_file, config_dict):
    parser = ConfigParser()
    parser.read_dict(config_dict)
    with open(config_file, "w") as f:
        parser.write(f)

def load_config(config_file_s, defaults=None, print_errors=True):
    parser = ConfigParser()
    if defaults:
        parser.read_dict(defaults)

    found = parser.read(config_file_s)

    if defaults:
        if found:
            for key in defaults:
                if key not in parser:
                    if print_errors:
                        print("Settings file:", found[0],
                              "is missing expected sections or is corrupt. Completing using defaults.")
                    save_config(config_file_s[0], parser)
                    break

        if not found:
            if print_errors:
                print("Settings file/s:", config_file_s,
                      "is/are missing. Saving defaults.")
            if isinstance(config_file_s, list):
                save_config(config_file_s[0], defaults)
            else:
                save_config(config_file_s, defaults)

    return parser

if __name__ == '__main__':
    CONFIG_FILE = "config.ini"
    DEFAULTS = {"Settings" : {
        "width" : "100",
    }}

    config = load_config(CONFIG_FILE, DEFAULTS)
    save_config(CONFIG_FILE, config)
    