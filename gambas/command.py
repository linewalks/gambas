import argparse
from gambas.validator import ConfigValidator


class Command:
  def __init__(self):
    self.parser = argparse.ArgumentParser(description="*** Config File Validator Option ***")
    self.add_options()

  def add_options(self):
    self.parser.add_argument("-d", "--default-path", type=str, help="Default config file path")
    self.parser.add_argument("-t", "--target-path", type=str, help="Target config file path")
    self.parser.add_argument(
        "--no-error",
        default=True,
        dest="error",
        action="store_false",
        help="""Do not get error when some keys do not exists. just raise warning"""
    )
    self.args = self.parser.parse_args()  

  def _set_args(self, option_list):
    self.args = self.parser.parse_args(option_list)

  def run(self):
    config_validator = ConfigValidator(self.args.default_path, self.args.target_path)
    config_validator.check_exist_keys(self.args.error)
