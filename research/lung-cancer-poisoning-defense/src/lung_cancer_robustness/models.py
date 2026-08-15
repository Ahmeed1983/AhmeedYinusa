from __future__ import annotations


def build_baseline_cnn(image_size: int = 256, n_classes: int = 3, learning_rate: float = 1e-3):
    import tensorflow as tf

    inputs = tf.keras.Input((image_size, image_size, 1))
    x = tf.keras.layers.Conv2D(64, 3, activation="relu", name="conv1")(inputs)
    x = tf.keras.layers.MaxPooling2D(2)(x)
    x = tf.keras.layers.Conv2D(64, 3, activation="relu", name="conv2")(x)
    x = tf.keras.layers.MaxPooling2D(2)(x)
    x = tf.keras.layers.Dropout(0.5)(x)
    x = tf.keras.layers.Flatten()(x)
    features = tf.keras.layers.Dense(16, activation="relu", name="dense_features")(x)
    outputs = tf.keras.layers.Dense(n_classes, activation="softmax")(features)
    model = tf.keras.Model(inputs, outputs, name="lung_ct_baseline_cnn")
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def build_archived_teacher(image_size: int = 256, n_classes: int = 3):
    import tensorflow as tf

    return tf.keras.Sequential([
        tf.keras.layers.Input((image_size, image_size, 1)),
        tf.keras.layers.Conv2D(32, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(2),
        tf.keras.layers.Conv2D(64, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu", name="teacher_features"),
        tf.keras.layers.Dense(n_classes, activation="softmax"),
    ], name="archived_teacher")


def build_archived_student(image_size: int = 256, n_classes: int = 3):
    import tensorflow as tf

    return tf.keras.Sequential([
        tf.keras.layers.Input((image_size, image_size, 1)),
        tf.keras.layers.Conv2D(16, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(2),
        tf.keras.layers.Conv2D(32, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation="relu", name="student_features"),
        tf.keras.layers.Dense(n_classes, activation="softmax"),
    ], name="archived_student")
