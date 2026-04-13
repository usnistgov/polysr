import numpy as np
import pandas as pd
import pysr as pysr

df = pd.read_csv("data/WLF_data_folds.csv")

# options
weighted = False
Tref = True
chemconst3 = False
constpen = 2
fold = None

# define file prefix
prefix = "eqns"
if not (Tref):
    prefix += "_noTref"
if chemconst3:
    prefix += "_chemconst3"
if constpen == 2:
    prefix += "_constpen"
if weighted:
    prefix += "_weighted"
if fold != None:
    prefix += "_fold" + str(fold)

# choose the fold
if fold != None:
    df = df[df["fold"] != fold]

if Tref:
    x_in = df.iloc[:, 1:4].to_numpy()
    spec = pysr.TemplateExpressionSpec(
        expressions=["f"],
        variable_names=["x", "Tref", "class"],
        parameters={"p1": 6, "p2": 6},
        combine="f(x, Tref, p1[class], p2[class])",
    )
else:
    x_in = df.iloc[:, [1, 3]].to_numpy()
    spec = pysr.TemplateExpressionSpec(
        expressions=["f"],
        variable_names=["x", "class"],
        parameters={"p1": 6, "p2": 6},
        combine="f(x, p1[class], p2[class])",
    )
if chemconst3:
    x_in = df.iloc[:, 1:4].to_numpy()
    spec = pysr.TemplateExpressionSpec(
        expressions=["f"],
        variable_names=["x", "Tref", "class"],
        parameters={"p1": 6, "p2": 6, "p3": 6},
        combine="f(x, Tref, p1[class], p2[class], p3[class])",
    )

y_in = df.iloc[:, 4].to_numpy()

classcount = [int(df.groupby("class").count().iloc[i, 0]) for i in range(6)]
weights = np.concatenate([np.ones(i) / i for i in classcount])

print(x_in)
print(y_in)

modelsr = pysr.PySRRegressor(
    niterations=2000,
    binary_operators=["+", "*", "-", "/"],
    maxsize=30,
    maxdepth=10,
    complexity_of_constants=constpen,
    temp_equation_file=False,
    populations=500,
    expression_spec=spec,
    progress=False,
    verbosity=0,
    optimizer_iterations=500,
    optimizer_nrestarts=5,
)
if weighted:
    modelsr.fit(x_in, y_in, weights=weights)
else:
    modelsr.fit(x_in, y_in)

modelsr.equations_.to_csv("symreg/" + prefix + ".csv")
print("saved.")