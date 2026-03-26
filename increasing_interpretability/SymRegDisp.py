import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pysr as pysr
from sklearn.preprocessing import StandardScaler
import json

# Choose fold and feature set. Also specify prefix of name for saving results.
f = 0
prefix = "Test1"
allfeat = True
extend = False

# Adjust prefixes
if allfeat:
    prefix += ""
elif extend:
    prefix += "_totals_fracs"
else:
    prefix += "_totals"

# Get the data
df = pd.read_csv("data/disp_dataset.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values * (-1)

# Split the data
train_mask = np.genfromtxt(
    "data/data_split.csv", delimiter=",", skip_header=1, dtype=bool, usecols=f
)
mask = np.zeros(len(df.columns) - 1).astype(bool)
mask[8:12] = True

# Full feature set
if allfeat:
    X_adjust = X

elif extend:
    X_adjust = np.multiply(X[:, mask], X[:, 13][:, np.newaxis])
    X_adjust = np.concatenate(
        [X[:, 13].reshape(-1, 1), X_adjust, X[:, mask]], axis=1
    )  # length is first, then actual values, then fractions

else:
    X_adjust = np.multiply(X[:, mask], X[:, 13][:, np.newaxis])
    X_adjust = np.concatenate(
        [X[:, 13].reshape(-1, 1), X_adjust], axis=1
    )  # length is first, then actual values

X_train = X_adjust[train_mask, :]
X_test = X_adjust[np.logical_not(train_mask), :]
y_train = y[train_mask]
y_test = y[np.logical_not(train_mask)]

# Perform preprocessig if necessary
if allfeat:
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

# Perform Sym Reg
params = {
    "niterations": 2000,
    "binary_operators": ["+", "*", "-", "/"],
    "unary_operators": ["exp", "sin", "tanh", "log", "square", "cube"],
    "maxsize": 30,
    "maxdepth": 10,
    "complexity_of_constants": 1,
    "temp_equation_file": False,
    "populations": 500,
    "progress": False,
    "verbosity": 0,
}
with open("symreg/" + prefix + "_fold" + str(f) + ".json", "w") as json_file:
    json.dump(params, json_file, indent=4)

modelsr = pysr.PySRRegressor(**params)

modelsr.fit(X_train, y_train)

modelsr.equations_.to_csv("symreg/" + prefix + "_fold" + str(f) + ".csv")
print("saved.")
