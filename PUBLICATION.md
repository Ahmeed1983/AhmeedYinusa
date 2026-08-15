# Publication-to-Code Map

Associated publication: **“A Multi-Layered Defense Against Adversarial Attacks in Brain Tumor Classification Using Ensemble Adversarial Training and Feature Squeezing”** (*Scientific Reports*, 2025).

This repository is a publication-aligned reconstruction from archived experimental notebooks and the final paper. It is not described as an untouched original source-code snapshot.

## Paper component → repository implementation

| Publication component | Repository location |
|---|---|
| VGG16 transfer-learning classifier | `src/brain_tumor_robustness/models.py` |
| FGSM attack | `src/brain_tumor_robustness/attacks.py::fgsm_attack` |
| PGD attack | `src/brain_tumor_robustness/attacks.py::pgd_attack` |
| Bit-depth reduction | `src/brain_tumor_robustness/defenses.py::reduce_bit_depth` |
| Gaussian feature squeezing | `src/brain_tumor_robustness/defenses.py::gaussian_blur_batch` |
| Combined feature squeezing | `src/brain_tumor_robustness/defenses.py::feature_squeeze` |
| Publication parameters | `configs/published.yaml` |

## Publication reference values

The paper reports a 96% clean baseline, 32% accuracy under FGSM before defense, 13% under PGD before defense, 54% under FGSM after defense, and 47% under PGD after defense.

These values are retained as publication reference targets only. They are not claimed as fresh reruns from the cleaned repository.

## Important reproducibility note

The final paper specifies 4-bit feature squeezing and a 3 × 3 Gaussian blur, but the recovered final text does not provide one unambiguous numerical Gaussian standard deviation. The public configuration therefore leaves `gaussian_sigma` unresolved rather than inventing a value.
