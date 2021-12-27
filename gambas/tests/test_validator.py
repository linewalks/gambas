import pytest
from gambas.validator import ConfigValidator


class TestValidator:
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
  
  def test_validate_missing_config_file_with_no_error(self, default_config_path, missing_config_path):
    config_validator = ConfigValidator(default_config_path, missing_config_path)
    with pytest.warns(UserWarning):
      config_validator.check_exist_keys(is_error=False)

  def test_validate_correct_json_file(self, default_json_path, correct_json_path):
    config_validator = ConfigValidator(default_json_path, correct_json_path)
    try:
      config_validator.check_exist_keys()
    except Exception as e:
      assert False, e

  def test_validate_different_file_extension(self, default_json_path, correct_config_path):
    # NOTE: test the validator to compare other extensions like a pair of config and json file
    config_validator = ConfigValidator(default_json_path, correct_config_path)
    try:
      config_validator.check_exist_keys()
    except Exception as e:
      assert False, e

  def test_validate_different_file_extension_with_missing_key_file(self, default_json_path, missing_config_path):
    config_validator = ConfigValidator(default_json_path, missing_config_path)
    with pytest.raises(KeyError):
      config_validator.check_exist_keys()
