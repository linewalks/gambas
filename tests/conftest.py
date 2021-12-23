import os
import sys
import pytest

BASE_DIR = os.getcwd()
sys.path.append(BASE_DIR)


TEST_CONFIG_FOLDER = os.path.join(BASE_DIR, "tests", "files")
TEST_DEFAULT_CONFIG_DICT = {
    "TEST_USER": "user",
    "TEST_LUNCH": "gambas",
    "TEST_DINNER": "ssam"
}


def get_filepath_with_creating_file(
    config_file_name,
    test_file_folder,
    item_num=len(TEST_DEFAULT_CONFIG_DICT)
):
  if item_num > len(TEST_DEFAULT_CONFIG_DICT):
    raise IndexError(
        f"You set item_num {item_num}. Please set item_num less than length of TEST_DEFAULT_CONFIG_DICT"
    )

  filepath = os.path.join(test_file_folder, config_file_name)

  with open(filepath, "w") as f:
    for test_key, test_value in list(TEST_DEFAULT_CONFIG_DICT.items())[:item_num]:
      f.write(f'{test_key}="{test_value}"\n')

  return filepath


@pytest.fixture(scope="session")
def test_file_folder():
  if not os.path.isdir(TEST_CONFIG_FOLDER):
    os.makedirs(TEST_CONFIG_FOLDER)
  
  yield TEST_CONFIG_FOLDER
  os.rmdir(TEST_CONFIG_FOLDER)


@pytest.fixture(scope="session")
def default_config_path(test_file_folder):
  filepath = get_filepath_with_creating_file(
      "default_config.cfg",
      test_file_folder=test_file_folder,
  )
  yield filepath
  os.remove(filepath)


@pytest.fixture(scope="session")
def correct_config_path(test_file_folder):
  filepath = get_filepath_with_creating_file(
      "correct_config.cfg",
      test_file_folder=test_file_folder,
  )
  yield filepath
  os.remove(filepath)


@pytest.fixture(scope="session")
def missing_config_path(test_file_folder):
  filepath = get_filepath_with_creating_file(
      "missing_config.cfg",
      test_file_folder=test_file_folder,
      item_num=1
  )
  yield filepath
  os.remove(filepath)
