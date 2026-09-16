# Demo: run the inversion counter using the example config

import pathlib
from engine.config_loader import ConfigLoader

def main() -> None:
    cfg_file = pathlib.Path(__file__).parents[1] / "config" / "example_config.yaml"
    loader = ConfigLoader(cfg_file)
    counter = loader.get_counter()
    inversions = counter.count()
    # Write a human‑readable result
    results_dir = pathlib.Path(__file__).parent / "results"
    results_dir.mkdir(exist_ok=True)
    out_file = results_dir / "output.txt"
    out_file.write_text(f"Inversion count: {inversions}\n")
    print(f"Result written to {out_file}")

if __name__ == "__main__":
    main()
