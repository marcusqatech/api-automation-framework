
"""
Purpose
Reads the configuration file (env_config.yaml) and provides easy access to the values in the code.

Explanation
Opens the env_config.yaml file.
Reads its content and parses it as a Python dictionary using yaml.safe_load().
Returns the value of base_url.

"""
import yaml

def get_base_url():
    """
    Load the base URL from the YAML configuration file.
    """
    with open("src/config/env_config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config["base_url"]
