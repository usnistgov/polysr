# polysr: Symbolic Regression applied to Polymeric Use Cases

The repository supports the following manuscript:

Debra J. Audus and Jonathan E. Seppala, "Extracting Knowledge from Polymeric Data"

which demonstrates the utility of symbolic regression for understanding polymer data. Specifically, three distinct use cases are considered. Each of these use cases is contained in its own folder with its own `README.md`, code, data, and environment details. The use cases are as follows. The code is meant to ensure that the results of the mansucript are reproducible and also serve as examples for more complicated uses of symbolic regression, which can be modified for a particular user's needs.


### Robust to Noise

This use case demonstrates the robustness of symbolic regression to noise. We consider both the case where noise is added to the predicted quantity and the case where noise is added to one of the features. Specifically, we generate synthetic data from the Flory Huggins spinodal equation for our tests.

### Leveraging Complexity

This use case demonstrates the power of symbolic regression to learn an equation where the constants depend on the class. Specifically, the WLF equation is learned directly from experimental data where the constants are chemistry dependent.

### Increasing Interpretibility

This use case demonstrates the power of using symbolic regression to find a simple model that is interpretable and combining it with a traditional machine learning model to get accuracy. This approach also provides insight into when the simple model may fail. Specifically, the adsoprtion free energy of sequence defined polymers is used. Data is taken from [Jablonka et al. *Nature Communications* 2021](https://doi.org/10.1038/s41467-021-22437-0)

## Running the code

All code is written in Python and requires Python >= 3.7. It can be used on any operating system. Other requirements are listed in `requirements.txt` or similarly named files in each of the use case folders. The `README.md` files in each use case file provides additional details.

First clone the code via

```bash
git clone https://github.com/usnistgov/polysr.git
```

and navigate to the directory of the use case of interest

```bash
cd polysr/<use case folder>
```

Next, one needs to create a virtual environment. This can be done using Python virtual environments.

### Create a Python virtual environment

First, make sure you are using Python 3.7 or later.

```bash
python3 -m venv <name of virtual environment>
```

It is recommended to name the virtual environment based on the use case.

Activate the virtual environment

```bash
source <name of virtual environment>/bin/activate
```

Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

In some cases `requirement.txt` should be replaced with a similar file as specified in the use case `README.md`.


## Contact

Debra J. Audus, PhD
Data Science and AI Group
Materials Data Division  
Material Measurement Laboratory  
National Institute of Standards and Technology  

Email: debra.audus@nist.gov  
GithubID: @debraaudus  
Staff website: https://www.nist.gov/people/debra-audus  

## How to cite

If you use the code, please cite our manuscript once it is published.
