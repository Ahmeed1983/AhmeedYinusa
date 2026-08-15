"""FGSM and PGD attacks for publication-aligned robustness experiments."""

import tensorflow as tf


def fgsm_attack(model, images, labels, epsilon=0.01):
    """Generate untargeted FGSM adversarial examples."""
    images = tf.cast(images, tf.float32)
    labels = tf.cast(labels, tf.int64)

    with tf.GradientTape() as tape:
        tape.watch(images)
        predictions = model(images, training=False)
        loss = tf.keras.losses.sparse_categorical_crossentropy(labels, predictions)

    gradient = tape.gradient(loss, images)
    adversarial = images + epsilon * tf.sign(gradient)
    return tf.clip_by_value(adversarial, 0.0, 1.0)


def pgd_attack(model, images, labels, epsilon=0.01, alpha=0.002, steps=10):
    """Generate untargeted L-infinity PGD adversarial examples.

    Defaults correspond to one attack setting reported in the final paper.
    Other simulation settings should be supplied explicitly from configuration.
    """
    original = tf.cast(images, tf.float32)
    labels = tf.cast(labels, tf.int64)
    adversarial = tf.identity(original)

    for _ in range(steps):
        with tf.GradientTape() as tape:
            tape.watch(adversarial)
            predictions = model(adversarial, training=False)
            loss = tf.keras.losses.sparse_categorical_crossentropy(labels, predictions)

        gradient = tape.gradient(loss, adversarial)
        adversarial = adversarial + alpha * tf.sign(gradient)
        perturbation = tf.clip_by_value(adversarial - original, -epsilon, epsilon)
        adversarial = tf.clip_by_value(original + perturbation, 0.0, 1.0)

    return adversarial
