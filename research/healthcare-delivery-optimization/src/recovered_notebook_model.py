import gurobipy as gp
from gurobipy import GRB
import random

# Input data recovered from the original notebook export.
N = range(1, 31)   # Staff members
T = range(1, 6)    # Time slots
P = range(1, 21)   # Patients
R = range(1, 16)   # Resources
K = range(1, 11)   # Tasks

W = {(i, t): random.randint(1, 10) for i in N for t in T}
I = {(i, j, t): random.randint(1, 10) for i in N for j in N for t in T if i != j}
C = {(p, t): random.randint(1, 10) for p in P for t in T}
D = {(r, t): random.randint(1, 10) for r in R for t in T}
Q = {(p, t): random.randint(1, 10) for p in P for t in T}
O = {i: random.randint(1, 10) for i in N}
U = {p: random.randint(1, 10) for p in P}
S = {i: random.randint(1, 5) for i in N}
M = {(i, p, k, t): random.randint(1, 5) for i in N for p in P for k in K for t in T}
H = {i: random.randint(8, 12) for i in N}
D_t = {t: random.randint(2, 5) for t in T}
B = 150
F = {(i, j): random.randint(1, 3) for i in N for j in N if i != j}

model = gp.Model("healthcare")

x = model.addVars(N, T, vtype=GRB.BINARY, name="x")
y = model.addVars(P, T, vtype=GRB.BINARY, name="y")
z = model.addVars(R, T, vtype=GRB.BINARY, name="z")
o = model.addVars(N, vtype=GRB.BINARY, name="o")
v = model.addVars(N, P, vtype=GRB.BINARY, name="v")

# Recovered objective. Note that the x[i,t] * x[j,t] term is quadratic as written.
obj = (
    gp.quicksum(W[i, t] * x[i, t] for i in N for t in T)
    + gp.quicksum(I[i, j, t] * x[i, t] * x[j, t] for i in N for j in N for t in T if i != j)
    + gp.quicksum(C[p, t] * y[p, t] for p in P for t in T)
    + gp.quicksum(D[r, t] * z[r, t] for r in R for t in T)
    + gp.quicksum(Q[p, t] * y[p, t] for p in P for t in T)
    + gp.quicksum(O[i] * o[i] for i in N)
    + gp.quicksum(U[p] * v[i, p] for i in N for p in P)
    + gp.quicksum(S[i] * x[i, t] for i in N for t in T)
)

model.setObjective(obj, GRB.MINIMIZE)

model.addConstrs((gp.quicksum(x[i, t] for t in T) <= H[i] for i in N), name="Staff_Hours")
model.addConstrs((gp.quicksum(x[i, t] for i in N) >= D_t[t] for t in T), name="Total_Staff")
model.addConstrs((gp.quicksum(y[p, t] for t in T) == 1 for p in P), name="Patient_Slot")
model.addConstrs((gp.quicksum(z[r, t] for t in T) == 1 for r in R), name="Resource_Slot")
model.addConstr((gp.quicksum(o[i] for i in N) <= B), name="Overtime_Budget")
model.addConstrs((gp.quicksum(v[i, p] for i in N) == 1 for p in P), name="Patient_Staff")

# Preserved from the recovered notebook export. This expression should be reviewed
# carefully before treating the model as a finalized operational formulation.
model.addConstrs(
    (gp.quicksum(v[i, p] for i in N) <= M[i, p, k, t]
     for i in N for p in P for k in K for t in T if (i, p, k, t) in M),
    name="Task_Staff",
)

model.optimize()

if model.Status == GRB.OPTIMAL:
    print("Optimal solution found!")

    for i, t in x:
        if x[i, t].X > 0.5:
            print(f"Staff member {i} assigned to time slot {t}")

    for p, t in y:
        if y[p, t].X > 0.5:
            print(f"Patient {p} assigned to time slot {t}")

    for r, t in z:
        if z[r, t].X > 0.5:
            print(f"Resource {r} allocated at time slot {t}")

    staff_overtime_hours = {
        i: max(0, sum(W[i, t] for t in T if x[i, t].X > 0.5) - H[i])
        for i in N
    }
    for i, overtime_hours in staff_overtime_hours.items():
        print(f"Staff member {i} overtime hours: {overtime_hours}")
