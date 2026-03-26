# Robust to Noise

This folder contains the code and results from the "Robust to Noise" use case in the paper. This use case demonstrates the robustness of symbolic regression to noise. We consider both the case where noise is added to the predicted quantity and the case where noise is added to one of the features. Specifically, we generate synthetic data from the Flory Huggins spinodal equation for our tests.

# Notebooks and python files

The following is a list of all the Jupyter notebooks and python files. They are listed in order of the models being built and then analyzed.

## GenerateSpinodalData.ipynb

This notebook generates the synthetic data and saves it as `spin.csv`.

## SymRegSpinodal.py

This python file performs symbolic regression for a given type of noise added (phi or chi). Results are saved to the `symreg` folder.

## CompileResults.ipynb

*UPDATE ME* This notebook takes the results from running symbolic regression and compiles them into `.csv` files/

## Plots.ipynb

*UPDATE ME* This notebook generates heatmap plots of the results. 

# Folders

## symreg

Contains results of symbolic regression.