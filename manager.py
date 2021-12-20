import configparser

DUMMY_SECTION = "[DEFAULT]\n"


class ConfigContentManager:
  def __init__(self, filepath):
    self.filepath = filepath
    self.config_parser = configparser.ConfigParser(allow_no_value=True)
    self._read_file()

  def _read_file(self):
    with open(self.filepath) as config_file:
      content = config_file.read()
    try:
      self.config_parser.read_string(content)
    except configparser.MissingSectionHeaderError:
      content = f"{DUMMY_SECTION}{content}"
      self.config_parser.read_string(f"{DUMMY_SECTION}{content}")

  def _set_filepath(self, filepath):
    self.filepath = filepath
  
  def get_filepath(self):
    return filepath

  def get_key_list(self):
    return self.config_parser.defaults().keys()
