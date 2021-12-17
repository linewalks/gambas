import argparse
import configparser

dummy_section = "[DEFAULT]\n"

class ConfigFileParser:
  def __init__(self, path):
    self.config_parser = configparser.ConfigParser(allow_no_value=True)
    with open(path) as config_file:
      content = f"{dummy_section}{config_file.read()}"

    self.config_parser.read_string(content)

  def get_key_list(self):
    return self.config_parser.defaults().keys()
