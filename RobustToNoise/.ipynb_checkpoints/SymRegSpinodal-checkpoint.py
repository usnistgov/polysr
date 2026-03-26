import numpy as np
import pysr
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import sympy as sp

# set error
errscal = 10**-100
errortype = "y"

# load data
data = np.loadtxt("spin.csv", delimiter=",", dtype=float)
x = data[:, 0:2]
y = data[:, 2]

# add error
delta = np.random.normal(loc=0, scale=errscal, size=len(y))

if errscal > 10**-10:
    if yerror:
        y = y + delta
    else:
        x[:, 0] = x[:, 0] + delta


# loop over dataset sizes
for p in np.array([200, 100, 50, 20, 10, 5, 3]):

    print(p)

    for i in np.arange(20):
        # set up symbolic regrssion
        modelsr = pysr.PySRRegressor(
            niterations=2000,
            binary_operators=["+", "*", "-", "/"],
            unary_operators=["tanh", "square", "cube"],
            maxsize=20,
            maxdepth=5,
            populations=500,
            complexity_of_constants=1,
            temp_equation_file=False,
            progress=False,
            verbosity=0,
        )

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, train_size=p, shuffle=True
        )

        try:

            modelsr.fit(x_train, y_train)
            modelsr.equations_.to_csv(
                "symreg/d" + errortype
                + "p" + str(p) + "i" + str(i)
                + "e" + str(-1 * np.log10(errscal))
                + ".csv"
            )

        except:

            print("Warning on p=", p, "i=", i)
            i = i - 1
