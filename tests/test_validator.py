import os
import sys

BASE_DIR = os.getcwd()

sys.path.append(BASE_DIR)

import pytest
from validator import ConfigValidator


TEST_CONFIG_FOLDER = os.path.join(BASE_DIR, "tests", "files")

TEST_PAIR = {
    "TEST_USER": "user",
    "TEST_LUNCH": "gambas",
    "TEST_DINNER": "ssam"
}


class TestValidator:
  @pytest.fixture(scope="class")
  def test_file_folder(self):
    if not os.path.isdir(TEST_CONFIG_FOLDER):
      os.makedirs(TEST_CONFIG_FOLDER)
    
    yield TEST_CONFIG_FOLDER
    os.rmdir(TEST_CONFIG_FOLDER)

  @pytest.fixture(scope="class")
  def default_config_path(self, test_file_folder):
    filepath = os.path.join(test_file_folder, "default_config.cfg")

    with open(filepath, "w") as f:
      for test_key in TEST_PAIR.keys():
        f.write(f"{test_key}=\n")

    yield filepath
    os.remove(filepath)

  @pytest.fixture(scope="class")
  def correct_config_path(self, test_file_folder):
    filepath = os.path.join(test_file_folder, "correct_config.cfg")

    with open(filepath, "w") as f:
      for test_key, test_value in TEST_PAIR.items():
        f.write(f'{test_key}="{test_value}"\n')

    yield filepath
    os.remove(filepath)
    
  @pytest.fixture(scope="class")
  def missing_config_path(self, test_file_folder):
    filepath = os.path.join(test_file_folder, "missing_config.cfg")

    with open(filepath, "w") as f:
      for test_key, test_value in list(TEST_PAIR.items())[:1]:
        f.write(f'{test_key}="{test_value}"\n')
  
    yield filepath
    os.remove(filepath)

  def test_validate_correct_config_file(self, default_config_path, correct_config_path):
    config_validator = ConfigValidator(default_config_path, correct_config_path)
    try:
      config_validator.check_exist_keys()
    except Exception as e:
      assert False, e
  
  def test_validate_missing_config_file(self, default_config_path, missing_config_path):
    config_validator = ConfigValidator(default_config_path, missing_config_path)
    with pytest.raises(KeyError):
      config_validator.check_exist_keys()
