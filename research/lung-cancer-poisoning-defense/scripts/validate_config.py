from __future__ import annotations

import sys
from pathlib import Path
import yaml


def main(path):
    cfg = yaml.safe_load(Path(path).read_text())
    print(f"Loaded configuration: {path}")
    unresolved = []
    if cfg.get("provenance") == "published_method":
        if cfg["dataset"].get("gaussian_preprocessing_sigma") is None:
            unresolved.append("gaussian_preprocessing_sigma")
        if cfg["dataset"].get("validation_fraction") is None:
            unresolved.append("validation_fraction")
        if cfg["defense"].get("mixup_alpha") is None:
            unresolved.append("mixup_alpha")
        if cfg["defense"].get("randomized_smoothing_samples") is None:
            unresolved.append("randomized_smoothing_samples")
    if unresolved:
        print("Unresolved publication values: " + ", ".join(unresolved))
        print("The repository intentionally does not guess these values.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
