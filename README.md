# Brain Tumor MRI Adversarial Robustness

Research code aligned with the published study **“A Multi-Layered Defense Against Adversarial Attacks in Brain Tumor Classification Using Ensemble Adversarial Training and Feature Squeezing”** (*Scientific Reports*, 2025).

This repository presents a clean, publication-aligned implementation reconstructed from archived experimental notebooks and the final published methodology. It is intentionally described as a reconstructed research-code release rather than as the untouched original notebook used during publication.

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

These values are publication reference targets, not freshly regenerated results from this repository.

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

Do not commit datasets, model checkpoints, credentials, or `kaggle.json` files to this repository.

## Reproducibility and Provenance

The archived notebooks document genuine experimental development, but they are not a single one-to-one executable snapshot of the final paper. The clean `src/` modules follow the publication where the final paper is explicit and expose unresolved values instead of silently inventing them.

One example is Gaussian feature squeezing. The final paper specifies a 3 × 3 Gaussian blur but the recovered publication text does not provide one unambiguous numerical standard deviation. Therefore `configs/published.yaml` leaves `gaussian_sigma` unset.

See [`PROVENANCE.md`](PROVENANCE.md) and [`PUBLICATION.md`](PUBLICATION.md) for the paper-to-code mapping and documented differences between archived experimentation and the final publication.

## Research Integrity

This repository distinguishes publication-aligned implementation from historical experimental development. It does not claim that the cleaned modules are the untouched original publication source code.

## Citation

If you use this code, please cite the associated publication. Citation metadata are provided in [`CITATION.cff`](CITATION.cff).

## License Status

No software license has been selected for this reconstructed public research-code release. See [`LICENSE_STATUS.md`](LICENSE_STATUS.md) before reuse or redistribution.

## Authors

**Ahmeed Adekunle Yinusa** and **Misa Faezipour**
