# Healthcare Delivery Optimization

Research code associated with **“Optimizing Healthcare Delivery: A Model for Staffing, Patient Assignment, and Resource Allocation”** (*Applied System Innovation*, 2023).

This project presents the computational optimization framework used to study healthcare staffing, patient assignment, resource allocation, and overtime decisions with Gurobi.

## What Is Included

- `src/recovered_notebook_model.py` contains the principal optimization model available from the original computational workflow.
- `FORMULATION_NOTES.md` documents modeling and reproducibility details that should be understood before interpreting or extending the code.
- `requirements.txt` lists the core Python dependencies.

## Model Elements

The computational model includes:

- 30 staff members
- 5 time slots
- 20 patients
- 15 resources
- 10 tasks
- binary staff assignment variables `x[i,t]`
- binary patient scheduling variables `y[p,t]`
- binary resource variables `z[r,t]`
- overtime variables `o[i]`
- staff-patient assignment variables `v[i,p]`

The objective combines staff workload, staff interaction terms, patient costs, resource costs, patient-quality terms, overtime, staff-patient assignment costs, and staff-satisfaction terms.

## Reproducibility Note

The available computational workflow generates simulated coefficients using Python's `random.randint` without a fixed random seed. Therefore, a fresh run may not regenerate the exact numerical objective values reported in the paper unless the original generated inputs are also available.

The objective also contains products of binary variables `x[i,t] * x[j,t]`. Although the publication describes the model as mixed-integer linear programming, that term is quadratic as written in the available model. This is documented in `FORMULATION_NOTES.md` for transparency.

## Running

A working Gurobi installation and license are required.

```bash
pip install -r requirements.txt
python src/recovered_notebook_model.py
```

## Data

The study uses simulated input data. No patient-level confidential dataset is required for the available model.

## Code and Materials Availability

This repository contains the public computational implementation currently available for the study. **Additional or more complete scripts, notebooks, generated inputs, and supporting research materials may be requested from the author when available and shareable.** Availability may depend on what was retained from the original study and on applicable licensing or sharing restrictions.

## Research Use

Researchers extending this work should clearly distinguish the published formulation from any later corrections, linearizations, deterministic replicas, or alternative formulations.

## Authors

**Ahmeed Adekunle Yinusa** and **Misa Faezipour**
