# Increasing Interpretability

This folder contains the code and results from the "Increasing interpretability" use case in the paper. This use case demonstrates the power of using symbolic regression to find a simple model that is interpretable and combining it with a traditional machine learning model to get accuracy. This approach also provides insight into when the simple model may fail. Specifically, the adsoprtion free energy of sequence defined polymers is used. Data is taken from [Jablonka et al. *Nature Communications* 2021](https://doi.org/10.1038/s41467-021-22437-0)

# Environment

`SymRegDisp.py` was run on a cluster using Python 3.9.21, Julia 1.10.5 and packages as specified in `sr_requirements.txt`.

The remainder of the code was run locally using Python 3.12.8 and packages as specified in `requirements.txt`. However, the `SymRegDisp.py` should also be able to be run with this environment assuming Julia is installed.

# Notebooks and python files

The following is a list of all the Jupyter notebooks and python files. They are listed in order of the models being built and then analyzed.

## DataSplit.ipynb

This notebook pulls the data directly from the [Github repository associated with Jablonka et al. *Nature Communications* 2021](https://github.com/byooooo/dispersant_screening_PAL), splits the data into 5 categories based on its deltaGmin value and then performs a stratified 5 fold split. Resulting data is saved in `data/disp_dataset.csv` and splits are saved in `data/data_split.csv`. Please note that the splits used in the publication are already saved in `data`, so running this script will overwrite them.

## SymRegDisp.py

This python file performs symbolic regression on a specified fold for a given feature test. Results are saved to the `symreg` folder along with the parameters used.

## ViewSymReg.ipynb

This notebook views the results from running symbolic regression. Test 5 uses the full feature set with z-score standardization. Test 8 uses the length, amounts of each bead type and fractions of each bead type as the feature set. No pre-processing is done. Test 7 uses the length and amounts of each bead type as the feature set.

## GPR.ipynb

This notebook trains a Gaussian process regressor to predict $-\Delta G_{abs}$. The prior is taken to be a constant. Results are saved in the `models` folder. SHAP values are also computed. There is an option to use full feature set or a reduced feature set. The reduced feature set is the max_[W] along with totals of each type of bead. The model in the publicaiton has the full dataset with ARD (a length scale for every dimension).

## HybridGPR.ipynb

This notebook trains a Gaussian process regressor to predict $-\Delta G_{abs}$. The prior is taken to be a linear function of total number of each bead type. Results are saved in the `modelsprior` folder. SHAP values are also computed. There is an option to use full feature set or a reduced feature set. The reduced feature set is the max_[W] along with totals of each type of bead. The model in the publicaiton has the full dataset with ARD (a length scale for every dimension). The prior is also saved and treated as the "learned equation" in the paper.

## CompressModels.ipynb

Compress models so they take up minimal space.

## ParityPlots.ipynb

This notebook generates parity plots for comparing the different methods (GPR, hybrid GPR, learned equation) across all of the folds.

## SHAPplots.ipynb

This notebook generates SHAP plots for GPR and hybrid GPR for the first fold.

# Folders

## data

Contains the training data and splits.

## symreg

Contains results of symbolic regression.

## models

Contains results of `GPR.ipynb`.

## hybridmodels

Contains results of `HybridGPR.ipynb`.
