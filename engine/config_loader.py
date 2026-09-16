"""Load a run configuration and instantiate the engine.

The configuration schema is deliberately simple: a JSON/YAML mapping with a
single key ``data`` containing a list of integers. The loader validates the
structure and returns an ``InversionCounter`` ready to run.
"""

import json
import pathlib
from typing import Any, Dict, List

import yaml

from .inversion_counter import InversionCounter


class ConfigLoader:
    """Parse a YAML or JSON file into an ``InversionCounter`` instance.

    Parameters
    ----------
    path: str | pathlib.Path
        Path to the configuration file.
    """

    def __init__(self, path: str | pathlib.Path):
        self.path = pathlib.Path(path)
        if not self.path.is_file():
            raise FileNotFoundError(f"Config file not found: {self.path}")
        self.raw: Dict[str, Any] = self._read_file()
        self._validate()

    def _read_file(self) -> Dict[str, Any]:
        if self.path.suffix.lower() in {".yaml", ".yml"}:
            return yaml.safe_load(self.path.read_text())
        if self.path.suffix.lower() == ".json":
            return json.loads(self.path.read_text())
        raise ValueError("Unsupported config format; use .yaml or .json")

    def _validate(self) -> None:
        if "data" not in self.raw:
            raise ValueError("Config must contain a 'data' field")
        if not isinstance(self.raw["data"], list):
            raise TypeError("'data' must be a list of integers")
        if not all(isinstance(x, int) for x in self.raw["data"]):
            raise TypeError("All elements in 'data' must be integers")

    def get_counter(self) -> InversionCounter:
        """Create an ``InversionCounter`` from the loaded config."""
        return InversionCounter(self.raw["data"])
