from __future__ import annotations

import numpy as np


def randomized_smoothing_predict(model, images, sigma: float = 0.01, samples: int | None = None, random_state: int | None = None):
    if samples is None or samples <= 0:
        raise ValueError("samples must be supplied; the recovered manuscript did not specify one canonical value")
    rng = np.random.default_rng(random_state)
    total = None
    for _ in range(samples):
        noise = rng.normal(0.0, sigma, size=images.shape).astype(np.float32)
        noisy = np.clip(images + noise, 0.0, 1.0)
        pred = np.asarray(model.predict(noisy, verbose=0), dtype=np.float64)
        total = pred if total is None else total + pred
    return (total / samples).astype(np.float32)
