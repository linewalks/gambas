import pytest
from gambas.tests.conftest import TEST_DEFAULT_CONFIG_DICT
from gambas.manager import ConfigContentManager


class TestManager:
  @pytest.fixture(scope="class")
  def config_manager(self, default_config_path):
    return ConfigContentManager(default_config_path)

  def test_get_key_list(self, config_manager):
    """
    NOTE
    ConfigContentManager has features to parse keys of a config file and return them as a list.
    default_config.cfg was made of TEST_DEFAULT_CONFIG_DICT on conftest.py
    Therefore, in this test, validate that default_config.cfg has all keys same with TEST_DEFAULT_CONFIG_DICT's
    """
    config_key_list = config_manager.get_key_list()
    config_key_upper_list = map(lambda x: x.upper(), config_key_list)
    assert set(TEST_DEFAULT_CONFIG_DICT.keys()) == set(config_key_upper_list)
