import argparse
from validator import ConfigValidator

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="*** Config File Validator Option ***")
  parser.add_argument("-d", "--default-path", type=str, help="Default config file path")
  parser.add_argument("-t", "--target-path", type=str, help="Target config file path")

  args = parser.parse_args()

  default_filepath = args.default_path
  target_filepath = args.target_path

  config_validator = ConfigValidator(default_filepath, target_filepath)
  config_validator.check_exist_keys()
