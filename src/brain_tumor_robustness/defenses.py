"""Feature-squeezing utilities used by the publication-aligned defense pipeline."""

import numpy as np


def reduce_bit_depth(images, bits=4):
    """Reduce normalized image precision to ``bits`` per channel."""
    images = np.asarray(images, dtype=np.float32)
    levels = (2 ** bits) - 1
    squeezed = np.round(np.clip(images, 0.0, 1.0) * levels) / levels
    return squeezed.astype(np.float32)


def gaussian_blur_batch(images, kernel_size=3, sigma=None):
    """Apply Gaussian blurring to a batch of images.

    The publication specifies a 3x3 Gaussian kernel but the recovered final
    manuscript text does not provide one unambiguous numerical sigma. For that
    reason ``sigma`` is required rather than silently invented.
    """
    if sigma is None:
        raise ValueError(
            "gaussian sigma is unresolved in the recovered publication text; "
            "supply it explicitly for your experiment"
        )

    import cv2

    output = []
    for image in np.asarray(images):
        blurred = cv2.GaussianBlur(
            image,
            (kernel_size, kernel_size),
            sigmaX=float(sigma),
        )
        output.append(blurred)
    return np.asarray(output, dtype=np.float32)


def feature_squeeze(images, bits=4, kernel_size=3, sigma=None):
    """Apply bit-depth reduction followed by Gaussian blurring."""
    reduced = reduce_bit_depth(images, bits=bits)
    return gaussian_blur_batch(reduced, kernel_size=kernel_size, sigma=sigma)
