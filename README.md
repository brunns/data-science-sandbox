# Data Scence Sandbox

Data Scence Sandbox

## Useful links

* [Jupyter](https://pinboard.in/u:brunns/t:jupyter), particularly [Jupyter Notebook: An Introduction](https://realpython.com/jupyter-notebook-introduction/).
* [Numpy](https://pinboard.in/u:brunns/t:numpy)
* [Pandas](https://pinboard.in/u:brunns/t:pandas), particularly [Using Pandas and Python to Explore Your Dataset](https://realpython.com/pandas-python-explore-dataset/).
* [matplotlib](https://pinboard.in/u:brunns/t:matplotlib)
* [SymPy](https://pinboard.in/u:brunns/t:sympy)

### Using Direnv to populate credentials

Install [direnv](https://direnv.net/) if necessary.

Copy `.envrc.template` to `.envrc` and populate. (Do not commit `.envrc`!)

## Tasks

### setup

All setup

```sh
python -V  # Any version after 3.6 is probably fine.
python -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
```

### start

Start notebook

```sh
jupyter lab --port=8989
```
