from __future__ import annotations

import numpy as np


def random_uniform_label_flip(
    labels: np.ndarray,
    fraction: float,
    n_classes: int = 3,
    random_state: int | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Flip a fraction of labels uniformly to one of the other classes."""
    if not 0 <= fraction <= 1:
        raise ValueError("fraction must be in [0, 1]")
    rng = np.random.default_rng(random_state)
    poisoned = np.asarray(labels, dtype=np.int64).copy()
    n = int(np.floor(len(poisoned) * fraction))
    indices = rng.choice(len(poisoned), size=n, replace=False)
    offsets = rng.integers(1, n_classes, size=n)
    poisoned[indices] = (poisoned[indices] + offsets) % n_classes
    return poisoned, indices


def cyclic_plus_two_flip(
    labels: np.ndarray,
    fraction: float,
    n_classes: int = 3,
    random_state: int | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Implement the manuscript alternative y' = (y + 2) mod 3."""
    if not 0 <= fraction <= 1:
        raise ValueError("fraction must be in [0, 1]")
    rng = np.random.default_rng(random_state)
    poisoned = np.asarray(labels, dtype=np.int64).copy()
    n = int(np.floor(len(poisoned) * fraction))
    indices = rng.choice(len(poisoned), size=n, replace=False)
    poisoned[indices] = (poisoned[indices] + 2) % n_classes
    return poisoned, indices
