# Healthcare Delivery Optimization

Research code associated with **“Optimizing Healthcare Delivery: A Model for Staffing, Patient Assignment, and Resource Allocation”** (*Applied System Innovation*, 2023).

This project formulates healthcare staffing, patient assignment, resource allocation, and overtime decisions as a mathematical optimization problem implemented with Gurobi. The code here is reconstructed from the recovered HTML export of the original Jupyter notebook and is presented with provenance notes rather than rewritten as if it were a new implementation.

## What is included

- `src/recovered_notebook_model.py` preserves the principal optimization model recovered from the notebook export.
- `FORMULATION_NOTES.md` explains important modeling and reproducibility details that should be understood before interpreting or extending the code.
- `requirements.txt` lists the core Python dependencies.

## Model elements

The recovered notebook defines:

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

## Important reproducibility note

The recovered notebook generates simulated coefficients using Python's `random.randint` without a fixed random seed. Therefore a fresh run will not necessarily regenerate the exact numerical objective values reported in the paper unless the original generated inputs are also recovered.

The objective also contains products of binary variables `x[i,t] * x[j,t]`. Although the publication describes the model as mixed-integer linear programming, that term is quadratic as written in the recovered code. This repository preserves the recovered formulation and documents the issue rather than silently changing the published model.

## Running

A working Gurobi installation and license are required.

```bash
pip install -r requirements.txt
python src/recovered_notebook_model.py
```

## Data

The study uses simulated input data. No patient-level confidential dataset is required for the recovered model.

## Research integrity

This release is intended to make the actual computational artifact inspectable. Corrections, linearizations, deterministic replicas, or alternative formulations should be developed as clearly labeled extensions rather than silently replacing the recovered research model.

## Authors

**Ahmeed Adekunle Yinusa** and **Misa Faezipour**
