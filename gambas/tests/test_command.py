import os
import pytest

from gambas.command import Command

class TestCommand:
  @pytest.fixture(scope="class")
  def command(self):
    return Command()

  @pytest.mark.parametrize(
      "no_error_option",
      [
          "--no-error",
          None
      ]
  )
  def test_command_with_option(self, command, default_config_path, correct_config_path, no_error_option):
    test_option_list = ["-d", default_config_path, "-t", correct_config_path]
    if no_error_option:
      test_option_list.extend([no_error_option])

    args = command.parser.parse_args(test_option_list)

    assert args.default_path == default_config_path
    assert args.target_path == correct_config_path
    assert args.error if not no_error_option else args.error == False

  def test_command_run(self, command, default_config_path, correct_config_path):
    option_list = ["-d", default_config_path, "-t", correct_config_path]
    command._set_args(option_list)
    command.run()

  def test_command_run_error_with_missing_key_config(self, command, default_config_path, missing_config_path):
    option_list = ["-d", default_config_path, "-t", missing_config_path]
    command._set_args(option_list)
    with pytest.raises(KeyError):
      command.run()

  def test_command_run_warning_with_missing_key_config(self, command, default_config_path, missing_config_path):
    option_list = ["-d", default_config_path, "-t", missing_config_path, "--no-error"]
    command._set_args(option_list)
    with pytest.warns(UserWarning):
      command.run()
