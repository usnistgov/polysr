import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy
import json
from pathlib import Path

import ConstrainedSimplifiction


directory = Path('symreg')

# Loop over files
for c, filename in enumerate(directory.iterdir()):
    
    if filename.is_file() and not 'class' in str(filename) and not 'simplified' in str(filename):
        
        print('~' * 50)
        print(filename)
        print('~' * 50)
        
        # Get the data and set parameters
        filename_simplified = str(filename)[:-4] + "_simplified.csv"
        df = pd.read_csv(filename, index_col=0)

        if filename_simplified in [str(file) for file in  directory.iterdir()]:
            print('Already analyzed.')
            continue
        
        
        const_pen = 1
        if "constpen" in str(filename):
            const_pen = 2
        
        df["simplification_justification"] = None
        df["original_complexity"] = df["complexity"]
        
        for i in np.arange(len(df)):
        
            # Large complexities are unlikely to be able to be simplified and are costly to evaluate
            if df.iloc[i].complexity > 15:
                continue
        
            eq = df.iloc[i].equation.split(";")[0].split("=")[1]

            if 'noTref' in str(filename):
                eq = eq.replace("#1", "x").replace("#", "c")
            else:
                eq = eq.replace("#1", "x").replace("#2", "t").replace("#", "c")
        
            simplifed_eq, start_score, best_score, path = ConstrainedSimplifiction.simplify_equation(eq, max_iterations=150, num_complexity=const_pen)
        
            if best_score < start_score:
                df.at[i, "complexity"] = best_score
                df.at[i, "simplification_justification"] = path
                print('+' * 50)
                print('Reduced!')
                print('+' * 50)
                
        # Remove losses that are not the lowest
        dfnew = df.copy()
        idxkeep = dfnew.groupby("complexity")["loss"].idxmin()
        dfnew = dfnew.loc[idxkeep]
        dfnew.sort_values(by='loss', ascending=False, inplace=True)
        running_min = dfnew['complexity'][::-1].cummin()[::-1]
        dfnew = dfnew[dfnew['complexity'] <= running_min]
        
        # Save the dataframe
        dfnew.to_csv(filename_simplified, index=False)
        
        # Plot the results
        fig, ax1 = plt.subplots(figsize=(6, 4))
        
        ax1.set_title(filename)
        ax1.plot(dfnew["complexity"], dfnew["loss"], "o")
        ax1.plot(df["original_complexity"], df["loss"], "s")
        
        ax1.set_yscale("log")
        ax1.set_xlabel("Complexity", fontsize=14)
        ax1.set_ylabel("Mean Squared Error (MSE)", fontsize=14)
        
        ax1.tick_params(axis="x", labelsize=12)
        ax1.tick_params(axis="y", labelsize=12)

        plt.show()