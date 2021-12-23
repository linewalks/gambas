import pytest
from tests.conftest import TEST_PAIR
from manager import ConfigContentManager


class TestManager:
  @pytest.fixture(scope="class")
  def config_manager(self, default_config_path):
    return ConfigContentManager(default_config_path)

  def test_get_key_list(self, config_manager):
    """
    NOTE
    ConfigContentManager has features to parsing keys of a config file and return them as a list.
    default_config.cfg were made of TEST_PAIR on conftest.py
    Therefore, in this test, validate that default_config.cfg has all keys same with TEST_PAIR's
    """
    config_key_list = config_manager.get_key_list()
    config_key_upper_list = map(lambda x: x.upper(), config_key_list)
    assert set(TEST_PAIR.keys()) == set(config_key_upper_list)
