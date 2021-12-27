import os
import sys
import pytest
import json

BASE_DIR = os.getcwd()
sys.path.append(BASE_DIR)


TEST_CONFIG_FOLDER = os.path.join(BASE_DIR, "files")
TEST_DEFAULT_DICT = {
    "test_user": "user",
    "test_breakfast": "salad",
    "test_lunch": "gambas",
    "test_dinner": "ssam"
}


def get_filepath_with_creating_file(
    config_file_name,
    filetype,
    test_file_folder,
    item_num=len(TEST_DEFAULT_DICT)
):
  if item_num > len(TEST_DEFAULT_DICT):
    raise IndexError(
        f"You set item_num {item_num}. Please set item_num less than length of TEST_DEFAULT_DICT"
    )

  file = f"{config_file_name}.{filetype}"
  filepath = os.path.join(test_file_folder, file)

  with open(filepath, "w", encoding="utf-8") as f:
    if filetype == "cfg":
      for test_key, test_value in list(TEST_DEFAULT_DICT.items())[:item_num]:
        f.write(f'{test_key.upper()}="{test_value}"\n')
    elif filetype == "json":
      json.dump(TEST_DEFAULT_DICT, f, ensure_ascii=False, indent="\t")

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
      "default_config",
      test_file_folder=test_file_folder,
      filetype="cfg"
  )
  yield filepath
  os.remove(filepath)


@pytest.fixture(scope="session")
def correct_config_path(test_file_folder):
  filepath = get_filepath_with_creating_file(
      "correct_config",
      test_file_folder=test_file_folder,
      filetype="cfg"
  )
  yield filepath
  os.remove(filepath)



@pytest.fixture(scope="session")
def default_json_path(test_file_folder):
  filepath = get_filepath_with_creating_file(
      "default_json",
      test_file_folder=test_file_folder,
      filetype="json"
  )
  yield filepath
  os.remove(filepath)


@pytest.fixture(scope="session")
def correct_json_path(test_file_folder):
  filepath = get_filepath_with_creating_file(
      "correct_json",
      test_file_folder=test_file_folder,
      filetype="json"
  )
  yield filepath
  os.remove(filepath)


@pytest.fixture(scope="session")
def missing_config_path(test_file_folder):
  filepath = get_filepath_with_creating_file(
      "missing_config",
      test_file_folder=test_file_folder,
      filetype="cfg",
      item_num=1
  )
  yield filepath
  os.remove(filepath)
