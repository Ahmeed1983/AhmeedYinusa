# Lung Cancer Poisoning Defense

Research code supporting the study **“Enhancing the Robustness of CNN-Based Lung Cancer Detection Models Against Label-Flipping Poison Attacks Using Defensive Distillation.”**

## Scope

This repository presents the computational framework used to investigate the robustness of CNN-based lung cancer classification under label-flipping poisoning attacks. The implementation covers image preprocessing, class balancing, CNN classification, poisoning experiments, defensive distillation, data sanitization, robust loss functions, augmentation, and model evaluation.

The repository is organized to support reproducible experimentation and further research in trustworthy medical AI, adversarial machine learning, and healthcare cybersecurity.

## Published Method Represented Here

The study uses the IQ-OTH/NCCD dataset with 1,190 CT images from 110 patients in three classes. Images are resized to 256 x 256, converted to grayscale, normalized, and balanced with SMOTE. The baseline CNN uses two 64-filter 3 x 3 convolution blocks, max pooling, dropout 0.5, a 16-unit dense layer, and a three-class softmax output. Training uses Adam at 0.001, batch size 8, and 50 epochs.

The defense pipeline includes:

- 30% label-flipping poisoning evaluation
- a teacher model trained on clean, SMOTE-balanced data
- temperature 10.0 and label smoothing 0.1
- Isolation Forest sanitization with contamination 0.1
- mixup augmentation
- symmetric cross-entropy with 0.1 * CE + 1.0 * RCE
- randomized smoothing at inference with Gaussian noise sigma 0.01

Reported outcomes are retained as publication reference targets: approximately 99% clean accuracy and 95-96% under poisoning.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate_config.py configs/published.yaml
```

## Reproducibility Note

Implementation details, publication parameters, and the relationship between experimental development and the final methodology are documented in `PROVENANCE.md`.

Where a publication parameter is not explicitly specified in the available research record, it is documented rather than presented as a confirmed value.

## Code and Materials Availability

This repository contains the public research implementation and selected supporting scripts for the study. **Additional implementation details, research notebooks, and supporting materials may be requested from the author when available and shareable.** Availability may depend on the material retained from the original study and on applicable data, licensing, or sharing restrictions.

## Data and Credentials

The IQ-OTH/NCCD dataset is not redistributed through this repository. Dataset access remains subject to the source terms. Credentials, API keys, and private configuration files are not included.

## License

No software license has been selected. See the repository-level `LICENSE_STATUS.md` before reuse or redistribution.
