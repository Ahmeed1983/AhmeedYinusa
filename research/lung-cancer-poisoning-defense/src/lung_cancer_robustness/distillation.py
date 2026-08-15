from __future__ import annotations


def temperature_softmax_from_logits(logits, temperature: float = 10.0):
    import tensorflow as tf

    if temperature <= 0:
        raise ValueError("temperature must be positive")
    return tf.nn.softmax(logits / temperature, axis=-1)


def make_soft_labels(teacher_logits_model, images, temperature: float = 10.0):
    logits = teacher_logits_model(images, training=False)
    return temperature_softmax_from_logits(logits, temperature)


def categorical_label_smoothing(labels, n_classes: int, smoothing: float = 0.1):
    import tensorflow as tf

    one_hot = tf.one_hot(labels, depth=n_classes)
    return one_hot * (1.0 - smoothing) + smoothing / n_classes
