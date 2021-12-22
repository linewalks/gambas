from manager import ConfigContentManager


class ConfigValidator:
  def __init__(self, default_filepath, target_filepath):
    self.__default_filepath = default_filepath
    self.__target_filepath = target_filepath
    self.default_keys = ConfigContentManager(self.__default_filepath).get_key_list()
    self.target_keys = ConfigContentManager(self.__target_filepath).get_key_list()

  def check_exist_keys(self, is_error=True):
    cand_key_list = [
        cand_key
        for cand_key in self.default_keys
        if cand_key not in self.target_keys
    ]

    if cand_key_list:
      sentence = f"{', '.join(cand_key_list)} not in {self.__target_filepath}"
      raise KeyError(sentence) if is_error else Warning(sentence)
    else:
      print(f"There are all keys in a target config file {self.__target_filepath}")
