# Brain Tumor MRI Adversarial Robustness

Research code supporting the published study **“A Multi-Layered Defense Against Adversarial Attacks in Brain Tumor Classification Using Ensemble Adversarial Training and Feature Squeezing”** (*Scientific Reports*, 2025).

## Research Problem

Deep-learning models for medical-image classification can be highly accurate on clean images while remaining vulnerable to small adversarial perturbations. This project studies that problem in four-class brain-tumor MRI classification and evaluates a multilayer defense combining adversarial training with feature squeezing.

## Published Method Represented Here

- **Task:** four-class brain-tumor MRI classification
- **Backbone:** ImageNet-pretrained VGG16
- **Input:** 128 × 128 normalized MRI images
- **Classifier head:** Global Average Pooling, Dense 128 with ReLU, Dropout 0.5, four-class softmax
- **Attacks:** FGSM and PGD
- **Defense:** adversarial training plus feature squeezing
- **Feature squeezing:** 4-bit reduction and 3 × 3 Gaussian blurring

The paper reports the following reference results:

| Evaluation | Accuracy |
|---|---:|
| Clean baseline | 96% |
| FGSM before defense | 32% |
| PGD before defense | 13% |
| FGSM after defense | 54% |
| PGD after defense | 47% |

These values are included as publication reference targets.

## Repository Structure

```text
configs/
  published.yaml
src/brain_tumor_robustness/
  models.py
  attacks.py
  defenses.py
PUBLICATION.md
PROVENANCE.md
CITATION.cff
LICENSE_STATUS.md
requirements.txt
.gitignore
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The code modules can then be imported from `src/brain_tumor_robustness/` for training, attack generation, feature squeezing, and paper-aligned experimentation.

## Data

The publication uses the public Kaggle **Brain Tumor MRI Dataset** (`masoudnickparvar/brain-tumor-mri-dataset`), a composite collection of 7,023 MRI images derived from Figshare, SARTAJ, and Br35H sources. The dataset is not redistributed here.

Credentials, API keys, private configuration files, and restricted materials are not included in the public repository.

## Reproducibility Note

Implementation details, publication parameters, and the relationship between experimental development and the final methodology are documented in [`PROVENANCE.md`](PROVENANCE.md) and [`PUBLICATION.md`](PUBLICATION.md).

Where a publication parameter is not explicitly documented in the available research record, the repository identifies that limitation rather than presenting an unverified value as confirmed.

## Code and Materials Availability

This repository contains the public research implementation and selected supporting scripts for the study. **Additional or more complete implementation materials, research notebooks, configuration details, and supporting files may be requested from the author when available and shareable.** Availability may depend on what was retained from the original study and on applicable data, licensing, coauthor, or sharing restrictions.

## Citation

If you use this code, please cite the associated publication. Citation metadata are provided in [`CITATION.cff`](CITATION.cff).

## License Status

No software license has been selected for this public research-code release. See [`LICENSE_STATUS.md`](LICENSE_STATUS.md) before reuse or redistribution.

## Authors

**Ahmeed Adekunle Yinusa** and **Misa Faezipour**
