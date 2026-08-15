from __future__ import annotations

import numpy as np


def mixup(images: np.ndarray, labels: np.ndarray, alpha: float, random_state: int | None = None):
    if alpha is None or alpha <= 0:
        raise ValueError("mixup alpha must be a verified positive value")
    rng = np.random.default_rng(random_state)
    permutation = rng.permutation(len(images))
    lam = rng.beta(alpha, alpha, size=len(images)).astype(np.float32)
    x_shape = (len(images),) + (1,) * (images.ndim - 1)
    y_shape = (len(labels),) + (1,) * (labels.ndim - 1)
    mixed_x = lam.reshape(x_shape) * images + (1 - lam).reshape(x_shape) * images[permutation]
    mixed_y = lam.reshape(y_shape) * labels + (1 - lam).reshape(y_shape) * labels[permutation]
    return mixed_x.astype(np.float32), mixed_y.astype(np.float32)
