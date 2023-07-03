import json

import pytest
from api.core.config import get_config_values


# Tests that the function can successfully load a valid JSON file
def test_valid_json():
    config = get_config_values()
    assert isinstance(config, dict)
    assert len(config) > 0


# Tests that the function returns the expected JSON object when the config file exists and is readable
def test_valid_config_file():
    config = get_config_values()
    assert isinstance(config, dict)
    assert "openai_api_key" in config


# Tests that the function raises an exception when the config file is missing
def test_missing_config_file():
    with pytest.raises(Exception) as e:
        get_config_values("api/core/missing_config.json")
    assert str(e.value) == "The config file api/core/missing_config.json is missing"


# Tests that the function returns the expected JSON object when the config file contains invalid JSON
def test_invalid_json_config_file(tmp_path):
    path = tmp_path / "invalid_json_config.json"
    path.write_text("{invalid_json}")
    with pytest.raises(json.JSONDecodeError):
        get_config_values(str(path))


# Tests that the function returns the expected JSON object when the config file contains valid JSON but is not in the expected format
def test_unexpected_format_config_file(tmp_path):
    path = tmp_path / "unexpected_format_config.json"
    path.write_text('{"unexpected": "format"}')
    config = get_config_values(str(path))
    assert isinstance(config, dict)
    assert "unexpected" in config
    assert config["unexpected"] == "format"
