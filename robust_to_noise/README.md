# Robust to Noise

This folder contains the code and results from the "Robust to Noise" use case in the paper. This use case demonstrates the robustness of symbolic regression to noise. We consider both the case where noise is added to the predicted quantity and the case where noise is added to one of the features. Specifically, we generate synthetic data from the Flory Huggins spinodal equation for our tests.

# Enviroment

The code was run using Python 3.12.8 and packages used as as specified in requirements.txt

# Notebooks and python files

The following is a list of all the Jupyter notebooks and python files. They are listed in order of the models being built and then analyzed.

## GenerateSpinodalData.ipynb

This notebook generates the synthetic data and saves it as `spin.csv`.

## SymRegSpinodal.py

This python file performs symbolic regression for a given type of noise added (phi or chi). Results are saved to the `symreg` folder.

## CompileResults.ipynb

This notebook takes the results from running symbolic regression and summarizes the data into `.csv` files. Different files are created based on uncertainty source (x or y) and how success is measured (equation on the pareto front matchs or best equation).

## Plots.ipynb

This notebook generates heatmap plots of the results. 

# Folders

## symreg

Contains results of symbolic regression runs.

## results

Contains the compiled results of symbolic regression.

## figures

Contains the figures generated.