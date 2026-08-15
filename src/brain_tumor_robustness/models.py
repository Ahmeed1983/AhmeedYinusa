"""Publication-aligned VGG16 model for four-class brain tumor MRI classification.

This module is reconstructed from the final published methodology and archived
experimental notebooks. It is not presented as the untouched original source.
"""

from tensorflow import keras
from tensorflow.keras import layers


def build_vgg16_classifier(
    input_shape=(128, 128, 3),
    num_classes=4,
    dropout_rate=0.5,
    weights="imagenet",
):
    """Build the VGG16 classifier described in the publication.

    Architecture:
    VGG16 backbone -> GlobalAveragePooling2D -> Dense(128, relu)
    -> Dropout(0.5) -> Dense(num_classes, softmax).
    """
    base = keras.applications.VGG16(
        include_top=False,
        weights=weights,
        input_shape=input_shape,
    )
    base.trainable = False

    inputs = keras.Input(shape=input_shape)
    x = base(inputs, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(128, activation="relu")(x)
    x = layers.Dropout(dropout_rate)(x)
    outputs = layers.Dense(num_classes, activation="softmax")(x)
    return keras.Model(inputs, outputs, name="brain_tumor_vgg16")


def compile_model(model, learning_rate=1e-3):
    """Compile the classifier using Adam and sparse categorical cross-entropy."""
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def unfreeze_last_layers(model, n_layers=10):
    """Unfreeze the last ``n_layers`` of the VGG16 backbone for fine-tuning."""
    backbone = next(
        layer for layer in model.layers if isinstance(layer, keras.Model)
    )
    backbone.trainable = True
    for layer in backbone.layers[:-n_layers]:
        layer.trainable = False
    return model
