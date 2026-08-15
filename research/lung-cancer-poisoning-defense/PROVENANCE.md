# Provenance and paper alignment

## Recovered notebooks

Four raw notebooks were recovered from Google Drive:

- `CANCER_POISON_ATTACK_RESEARCH_MAIN.ipynb`, modified 2024-08-22
- `Poisson Attack on AI Medical Cancer Detection Model.ipynb`, modified 2024-08-13
- `CANCER_ATTACK_RESEARCH_MAIN3.ipynb`, modified 2024-08-09
- `CANCER_ATTACK_RESEARCH_MAIN2.ipynb`, modified 2024-08-09

They include the IQ-OTH/NCCD path, 256 x 256 grayscale preprocessing, SMOTE, the two-block CNN baseline, label poisoning, teacher and student CNNs, and temperature-based soft-label experiments. Several cells use a 40% poisoned fraction, while other later distillation examples use smaller poison factors. Temperature 10.0 appears repeatedly.

## Final manuscript additions not found in the recovered 2024 notebooks

The later manuscript describes a 30% random-uniform label-flipping attack plus a multi-strategy defense with teacher label smoothing, Isolation Forest sanitization, mixup, symmetric cross-entropy, and randomized smoothing. Searches of the four recovered notebooks did not find implementations of Isolation Forest, symmetric cross-entropy, mixup, or label smoothing.

## Crosswalk

| Component | Final manuscript | Recovered notebook evidence | Repository treatment |
|---|---|---|---|
| Dataset | IQ-OTH/NCCD, 1,190 CT images, 110 patients | IQ-OTH/NCCD path present | Implemented |
| Input | 256 x 256 grayscale, normalized | Present | Implemented |
| Class balancing | SMOTE | Present | Implemented as helper |
| Baseline CNN | 2 Conv blocks, 64 filters each, Dense 16, Dropout 0.5 | Present | Implemented |
| Baseline training | Adam 0.001, batch 8, 50 epochs | Present | Published config |
| Poison fraction | 30% final manuscript | archived main cells include 40% in one baseline experiment | Separate configs |
| Label flipping | manuscript contains both cyclic +2 and random-uniform k in {1,2} descriptions | archived poison code randomly changes to another class in one section | Both implemented |
| Teacher/student | clean teacher to soft-label student | Present in archived form | Implemented |
| Distillation T | 10.0 | Present | Implemented |
| Label smoothing | 0.1 | not found in archived notebooks | Implemented from manuscript |
| Isolation Forest | contamination 0.1 | not found | Implemented from manuscript |
| Mixup | formula supplied, alpha not numerically resolved | not found | Function implemented, config value unset |
| SCE | 0.1 CE + 1.0 RCE | not found | Implemented from manuscript |
| Randomized smoothing | Gaussian sigma 0.01 | not found | Implemented; sample count must be supplied |
| Reported robust accuracy | 99% clean, 95-96% poisoned | archived outputs vary substantially | Reference only |

## Reproducibility caution

The final manuscript evolved beyond the archived notebooks. This reconstructed package should therefore be described as a paper-aligned reconstruction grounded in the archived code and manuscript, not as an untouched original release from the experiment date.
