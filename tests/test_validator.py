import os
import sys

BASE_DIR = os.getcwd()

sys.path.append(BASE_DIR)

import pytest
from validator import ConfigValidator


class TestValidator:
  @pytest.fixture(scope="class")
  def default_config_path(self):
    return os.path.join(BASE_DIR "tests", "files", "default_config.cfg")
    
  @pytest.fixture(scope="class")
  def correct_config_path(self):
    return os.path.join(BASE_DIR, "tests", "files", "test_correct_config.cfg")
    
  @pytest.fixture(scope="class")
  def missing_config_path(self):
    return os.path.join(BASE_DIR, "tests", "files", "test_missing_config.cfg")

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
