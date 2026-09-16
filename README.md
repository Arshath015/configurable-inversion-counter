# Configurable Inversion Counter

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9%2B-green.svg)](https://www.python.org/downloads/)

A merge‑sort based inversion counting engine where behavior is defined purely by a declarative configuration file.

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Theoretical Background](#theoretical-background)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Analysis Document](#analysis-document)
- [Testing](#testing)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [License](#license)

## Overview
This repository provides a small, well‑tested utility that counts inversions in a list of integers using the classic merge‑sort technique. All runtime parameters are supplied via a YAML or JSON configuration, making the tool suitable for batch pipelines where code changes are undesirable.

## Tech Stack
- Python 3.9+
- PyYAML for config parsing
- pytest for testing

## Architecture
```text
config/
    example_config.yaml          # declarative run description
engine/
    __init__.py
    inversion_counter.py        # merge‑sort inversion logic
    config_loader.py            # schema validation & object creation
examples/
    run_demo.py                 # end‑to‑end example, writes results/output.txt
tests/
    test_counter.py
    test_config.py
docs/
    analysis.md                 # internal performance/design notes
README.md
requirements.txt
```

## Theoretical Background
Inversion counting measures how far a sequence is from being sorted. Formally, an inversion is a pair *(i, j)* such that *i < j* and *A[i] > A[j]*. A naïve O(n²) scan enumerates all pairs, which quickly becomes infeasible for large inputs.

The merge‑sort based algorithm achieves O(n log n) by counting cross‑inversions during the merge step. When the next element from the right half is placed before remaining elements in the left half, each of those left elements forms an inversion with the chosen right element. Summing these counts across recursive levels yields the total number of inversions.

Because the algorithm only requires comparisons, it works for any totally ordered type, but this package focuses on integers to keep the config schema simple and type‑safe.

## Installation
```bash
git clone https://github.com/yourorg/configurable-inversion-counter.git
cd configurable-inversion-counter
pip install -r requirements.txt
```

## Usage
```bash
python examples/run_demo.py
```
The script reads ``config/example_config.yaml`` (which contains ``data: [2, 4, 1, 3, 5]``), runs the counter, and writes the result to ``examples/results/output.txt``.

## API Reference
### class engine.inversion_counter.InversionCounter
- ``__init__(data: Sequence[int])`` – create a counter for the given list.
- ``count() -> int`` – return the total number of inversions.

### class engine.config_loader.ConfigLoader
- ``__init__(path: str | pathlib.Path)`` – load and validate a YAML/JSON config.
- ``get_counter() -> InversionCounter`` – instantiate the counter from the config.

## Analysis Document
See the detailed design and benchmark notes in [docs/analysis.md](docs/analysis.md).

## Testing
Run the test suite with:
```bash
pytest -q
```
All tests cover typical cases, edge conditions, and configuration validation.

## Limitations
- Only integer lists are supported; extending to generic comparable types requires schema changes.
- The implementation is single‑threaded; extremely large datasets may benefit from a parallel merge sort.

## Roadmap
- Add support for streaming input via generators.
- Provide a CLI wrapper that accepts a config path as an argument.
- Implement optional parallelism using multiprocessing.

## License
MIT License
