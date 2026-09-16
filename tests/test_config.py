import pathlib
import pytest
from engine.config_loader import ConfigLoader

def test_loader_yaml(tmp_path: pathlib.Path):
    cfg_path = tmp_path / "cfg.yaml"
    cfg_path.write_text("data: [3, 2, 1]")
    loader = ConfigLoader(cfg_path)
    counter = loader.get_counter()
    assert counter.count() == 3  # 3 inversions in reverse order of length 3

def test_loader_invalid_missing_data(tmp_path: pathlib.Path):
    cfg_path = tmp_path / "bad.yaml"
    cfg_path.write_text("foo: bar")
    with pytest.raises(ValueError):
        ConfigLoader(cfg_path)

def test_loader_type_enforcement(tmp_path: pathlib.Path):
    cfg_path = tmp_path / "bad2.yaml"
    cfg_path.write_text("data: [1, 'a', 3]")
    with pytest.raises(TypeError):
        ConfigLoader(cfg_path)
