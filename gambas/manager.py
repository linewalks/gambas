import configparser
import json
from abc import abstractmethod, ABCMeta

DUMMY_SECTION = "[DEFAULT]\n"


class BaseContentManager(metaclass=ABCMeta):
  def __init__(self, filepath):
    self.__filepath = filepath

  def _set_filepath(self, filepath):
    self.__filepath = filepath
  
  def get_filepath(self):
    return self.__filepath

  @abstractmethod
  def _read_file(self):
    raise NotImplementedError

  @abstractmethod
  def get_key_list(self):
    raise NotImplementedError


class ConfigContentManager(BaseContentManager):
  def __init__(self, filepath):
    super().__init__(filepath)
    self.config_parser = configparser.ConfigParser(allow_no_value=True)
    self.config_parser.optionxform = str  # NOTE: not to change keys as lower case charactors
    self._read_file()

  def _read_file(self):
    filepath = self.get_filepath()
    with open(filepath) as config_file:
      content = config_file.read()
    try:
      self.config_parser.read_string(content)
    except configparser.MissingSectionHeaderError:
      content = f"{DUMMY_SECTION}{content}"
      self.config_parser.read_string(content)

  def get_key_list(self):
    return self.config_parser.defaults().keys()


class JsonContentManager(BaseContentManager):
  def __init__(self, filepath):
    super().__init__(filepath)
    self._read_file()

  def _read_file(self):
    filepath = self.get_filepath()
    with open(filepath) as data_file:
      self.json_dict = json.load(data_file)

  def get_key_list(self):
    return self.json_dict.keys()
