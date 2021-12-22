import argparse
from validator import ConfigValidator

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="*** Config File Validator Option ***")
  parser.add_argument("-d", "--default-path", type=str, help="Default config file path")
  parser.add_argument("-t", "--target-path", type=str, help="Target config file path")
  parser.add_argument(
      "--no-error",
      default=True,
      dest="error",
      action="store_false",
      help="""Do not get error when some keys do not exists. just raise warning"""
  )

  args = parser.parse_args()

  config_validator = ConfigValidator(args.default_path, args.target_path)
  config_validator.check_exist_keys(args.error)
