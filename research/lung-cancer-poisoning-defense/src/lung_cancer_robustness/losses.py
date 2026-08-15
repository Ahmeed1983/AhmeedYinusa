from __future__ import annotations


def symmetric_cross_entropy(alpha_ce: float = 0.1, beta_rce: float = 1.0):
    """Return SCE = alpha * CE + beta * reverse-CE for probability targets."""
    import tensorflow as tf

    def loss(y_true, y_pred):
        eps = tf.keras.backend.epsilon()
        y_true_c = tf.clip_by_value(y_true, eps, 1.0)
        y_pred_c = tf.clip_by_value(y_pred, eps, 1.0)
        ce = -tf.reduce_sum(y_true * tf.math.log(y_pred_c), axis=-1)
        rce = -tf.reduce_sum(y_pred * tf.math.log(y_true_c), axis=-1)
        return alpha_ce * ce + beta_rce * rce

    return loss
