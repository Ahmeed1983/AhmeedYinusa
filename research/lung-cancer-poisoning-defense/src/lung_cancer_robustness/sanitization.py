from __future__ import annotations

import numpy as np
from sklearn.ensemble import IsolationForest


def isolation_forest_mask(features: np.ndarray, contamination: float = 0.1, random_state: int | None = None):
    detector = IsolationForest(contamination=contamination, random_state=random_state)
    prediction = detector.fit_predict(features)
    return prediction == 1


def sanitize_by_teacher_features(
    feature_model,
    images: np.ndarray,
    soft_labels: np.ndarray,
    contamination: float = 0.1,
    random_state: int | None = None,
):
    features = np.asarray(feature_model.predict(images, verbose=0))
    if features.ndim > 2:
        features = features.reshape(len(features), -1)
    mask = isolation_forest_mask(features, contamination, random_state)
    return images[mask], soft_labels[mask], mask
