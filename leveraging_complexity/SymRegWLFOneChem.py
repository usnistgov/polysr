import numpy as np
import pandas as pd
import pysr as pysr

dfclass = pd.read_csv("data/WLF_data_folds.csv")

for c in np.arange(6) + 1:

    dfall = dfclass[dfclass["class"] == c]

    x_in = dfall.iloc[:, 1].to_numpy().reshape(-1, 1)
    y_in = dfall.iloc[:, 4].to_numpy()

    modelsr = pysr.PySRRegressor(
        niterations=2000,
        binary_operators=["+", "*", "-", "/"],
        maxsize=30,
        maxdepth=10,
        complexity_of_constants=1,
        temp_equation_file=False,
        populations=500,
        progress=False,
        verbosity=0,
        optimizer_iterations=500,
        optimizer_nrestarts=5,
    )

    modelsr.fit(x_in, y_in)

    modelsr.equations_.to_csv("symreg/eqns_class" + str(c) + ".csv")
    print("saved.")
    print(modelsr)