import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error as mse
import gpflow
from gpflow.utilities import print_summary

fold = pd.read_csv("data/WLF_data_folds.csv")
gpmse = []

for f in range(4):

    print("Fold:", f)

    # get datasets
    train = fold[fold["fold"] != f]
    test = fold[fold["fold"] == f]

    x_train = train.iloc[:, 1:3].to_numpy()
    c_train = train.iloc[:, 3].to_numpy().reshape(-1, 1)
    y_train = train.iloc[:, 4].to_numpy()

    scaler = StandardScaler()
    scaler.fit(x_train)
    xs_train = scaler.transform(x_train)

    x_test = test.iloc[:, 1:3].to_numpy()
    xs_test = scaler.transform(x_test)
    c_test = test.iloc[:, 3].to_numpy().reshape(-1, 1)
    y_test = test.iloc[:, 4].to_numpy()

    # perform one hot encoding
    ohe = OneHotEncoder(sparse_output=False).fit(c_train)

    xs_train = np.concatenate((xs_train, ohe.transform(c_train)), axis=1)
    xs_test = np.concatenate((xs_test, ohe.transform(c_test)), axis=1)

    # build gp model
    gpmodel = gpflow.models.GPR(
        (xs_train, y_train.reshape(-1, 1)),
        kernel=gpflow.kernels.SquaredExponential(
            lengthscales=[0.5, 0.1, 1, 1, 1, 1, 1, 1]
        ),
    )

    print_summary(gpmodel)

    opt = gpflow.optimizers.Scipy()
    opt.minimize(gpmodel.training_loss, gpmodel.trainable_variables)

    print_summary(gpmodel)

    p_train, _ = gpmodel.predict_y(xs_train)
    p_test, _ = gpmodel.predict_y(xs_test)

    mse_train = mse(y_train, p_train.numpy())
    mse_test = mse(y_test, p_test.numpy())

    print("MSEs:", mse_train, mse_test)
    gpmse.append([f, mse_train, mse_test])

    # save data
    np.savetxt("results/gp_train_f" + str(f) + ".csv", p_train)
    np.savetxt("results/gp_test_f" + str(f) + ".csv", p_test)

mseres = pd.DataFrame(data=gpmse, columns=["fold", "mse_train", "mse_test"])
mseres.to_csv("results/gp_mse.csv", index=False)