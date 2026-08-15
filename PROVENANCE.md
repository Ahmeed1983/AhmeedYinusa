# Provenance

This repository was assembled from two evidence sources:

1. archived experimental notebooks recovered from the research workspace, and
2. the final published methodology for the Scientific Reports brain-tumor adversarial-robustness study.

The archived notebooks confirm genuine experimentation with VGG16, the Kaggle brain-tumor MRI dataset, FGSM, PGD, adversarial training, and related evaluation workflows. They do not form a single exact snapshot of the final published feature-squeezing pipeline.

The clean modules in `src/brain_tumor_robustness/` therefore follow the final paper where the publication is explicit and preserve unresolved values rather than silently substituting assumptions.

## Documented differences

- Archived notebooks commonly used PGD with three steps in some experiments, while the final paper reports ten-step PGD settings for the published evaluation.
- Archived notebooks commonly used a fine-tuning learning rate of `1e-5`, while the final paper text reports `1e-3`. `configs/published.yaml` follows the paper and records the discrepancy.
- Feature squeezing is part of the final paper but was not present in the recovered archived notebooks as a complete final pipeline.
- The recovered publication text specifies a 3 × 3 Gaussian blur but does not provide one unambiguous numerical sigma. The configuration leaves that value unresolved.

## Research-integrity statement

No synthetic commit history is used. No archived notebook is relabeled as the exact final publication source when the evidence does not support that claim. The public code should be cited as a cleaned, publication-aligned research implementation.
