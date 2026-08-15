# Lung Cancer Poisoning Defense

Paper-aligned research code reconstructed from archived experimental notebooks for the study **“Enhancing the Robustness of CNN-Based Lung Cancer Detection Models Against Label-Flipping Poison Attacks Using Defensive Distillation.”**

## Scope

This package distinguishes the final published-method description from four recovered 2024 notebooks. The notebooks demonstrate genuine CNN, SMOTE, label-poisoning, teacher-student, and temperature-distillation experiments, but they predate later elements described in the final manuscript, including Isolation Forest sanitization, symmetric cross-entropy, mixup, label smoothing, and randomized smoothing.

The `src/` package implements the final method where the paper is explicit and leaves unresolved parameters visible rather than silently guessing them. See `PROVENANCE.md`.

## Published method represented here

The paper describes the IQ-OTH/NCCD dataset with 1,190 CT images from 110 patients in three classes. Images are resized to 256 x 256, converted to grayscale, normalized, and balanced with SMOTE. The baseline CNN uses two 64-filter 3 x 3 convolution blocks, max pooling, dropout 0.5, a 16-unit dense layer, and a three-class softmax output. Training uses Adam at 0.001, batch size 8, and 50 epochs.

The final defense pipeline combines:

- 30% label-flipping poisoning evaluation
- a teacher model trained on clean, SMOTE-balanced data
- temperature 10.0 and label smoothing 0.1
- Isolation Forest sanitization with contamination 0.1
- mixup augmentation
- symmetric cross-entropy with 0.1 * CE + 1.0 * RCE
- randomized smoothing at inference with Gaussian noise sigma 0.01

Reported outcomes are retained only as reference targets: about 99% clean accuracy and 95-96% under poisoning.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate_config.py configs/published.yaml
```

## Important source gaps

The recovered manuscript gives the mixup formula but not one unambiguous numerical mixup alpha in the text available here. It also gives randomized-smoothing sigma 0.01 but does not specify a single number of Monte Carlo inference samples. Those fields remain unset in `configs/published.yaml`.

The manuscript also contains two label-flip descriptions: a cyclic `(y + 2) mod 3` equation and a later end-to-end algorithm using random offsets `k in {1, 2}`. Both are implemented. The canonical published config uses the random-uniform version because the abstract and final algorithm describe a random-uniform attack.

## Data and credentials

Do not commit the IQ-OTH/NCCD dataset or `kaggle.json`. Dataset access remains subject to the source terms.

## License

No software license has been selected. See the repository-level `LICENSE_STATUS.md` before public reuse or redistribution.
