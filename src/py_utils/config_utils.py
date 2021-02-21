def read_config_file():
    """
    Reads config.txt file into dictionary with the strings left of the '=' as keys and the values on the right as values.
    Returns ditionary object containing all keys with their corresponding values.

    Returns:
        dict: config.txt-file represented as dictionary.
    """
    config_dict = {}
    conf_lines = open('./config.txt', 'r')
    for line in conf_lines:
        key, value_str = line.strip().split('=')
        value_var = str_to_var(value_str)
        config_dict[key.strip()] = value_var
    return config_dict


def str_to_var(input_string):
    """
    Transforms a string to either an integer, None, True or False (boolean) if possible. Otherwise just returns original string.
    Returns a list if values in one row contains comma-seperated values.

    Args:
        input_string (str): input string to be converted.

    Returns:
        int/bool/str/list: value represented in input string
    """
    try:
        num = int(input_string)
        return num
    except ValueError:
        if input_string == "False":
            return False
        elif input_string == "True":
            return True
        elif input_string == "None":
            return None
        elif "," in input_string:
            return [str_to_var(element.strip()) for element in input_string.split(",")]
        else:
            return input_string.strip()



def set_config_value(key, value):
    """
    Sets value for a given key in the config.txt file and updates the file. 
    If the key does not exist, the key value pair will be appended to the config file.

    Args:
        key (str): key for which value is to be set
        value (str/bool/int/None): value to be saved with key
    """
    cnfg_dct = read_config_file()
    cnfg_dct[key] = value
    write_config_file(cnfg_dct)


def get_config_value(key):
    """
    Returns value for a given key in the config.txt file

    Args:
        key (str): key whose corresponding value is to be returned

    Returns:
        int/bool/str: value saved in dictionary for given key
    """
    cnfg_dct = read_config_file()
    return cnfg_dct[key]


def write_config_file(config_dict):
    """
    Wrtites a given dictionary into the ./config.txt file overwriting previous file.
    """
    lines = []
    for key in config_dict.keys():
        lines.append("{} = {}".format(key, config_dict[key]))

    writer = open('./config.txt', 'w')
    for line in lines:
        writer.write(line + '\n')
