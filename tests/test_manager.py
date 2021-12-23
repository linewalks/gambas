import pytest
from tests.conftest import TEST_PAIR
from manager import ConfigContentManager


class TestManager:
  @pytest.fixture(scope="class")
  def config_manager(self, default_config_path):
    cm = ConfigContentManager(default_config_path)
    return cm

  def test_get_key_list(self, config_manager):
    config_key_list = config_manager.get_key_list()
    config_key_upper_list = map(lambda x: x.upper(), config_key_list)
    assert set(TEST_PAIR.keys()) == set(config_key_upper_list)
