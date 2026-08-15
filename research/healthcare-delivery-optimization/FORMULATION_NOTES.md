# Formulation and reproducibility notes

## Provenance

The source in `src/recovered_notebook_model.py` was reconstructed from the recovered HTML export of the original Jupyter notebook used for the healthcare-delivery optimization study.

## Simulated coefficients

The notebook generates multiple coefficients with `random.randint(...)` and does not set a random seed. This means repeated runs generate different instances. Exact reproduction of objective values reported in the publication therefore requires either the original generated instance data or another preserved record of those random draws.

## Linear-versus-quadratic formulation

The publication describes the approach as mixed-integer linear programming. However, the recovered objective contains the interaction term

```python
I[i, j, t] * x[i, t] * x[j, t]
```

which is quadratic in the binary decision variables. This repository preserves that expression because it appears in the recovered computational artifact. A future explicitly labeled extension may introduce auxiliary variables and linearization constraints if a strictly linear MILP version is desired.

## Constraint review

The recovered `Task_Staff` constraint is also preserved rather than silently corrected. Its indexing and aggregation should be reviewed before operational use. The goal of this public artifact is research transparency and reproducibility, not to imply that every historical notebook expression is production-ready.

## Recommended extension workflow

A rigorous follow-up implementation should:

1. separate instance generation from optimization,
2. fix and record random seeds,
3. save generated coefficients to a versioned data file,
4. clearly distinguish the recovered formulation from any corrected formulation,
5. add unit tests for assignment and capacity constraints, and
6. report solver version, Gurobi parameters, objective value, and optimality gap.
