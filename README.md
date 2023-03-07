# Data Scence Sandbox

Data Scence Sandbox

[Useful links](https://pinboard.in/u:brunns/t:jupyter), particularly [Jupyter Notebook: An Introduction](https://realpython.com/jupyter-notebook-introduction/) and [Using Pandas and Python to Explore Your Dataset](https://realpython.com/pandas-python-explore-dataset/).

## Set up

```bash
python -V  # Any version after 3.6 is probably fine.
mkdir -p ~/temp/jupyter
cd ~/temp/jupyter
python -m venv venv
source venv/bin/activate
pip install -U -r requirements.txt
```
### Using Direnv to populate credentials

Install [direnv](https://direnv.net/) if necessary.

Copy `.envrc.template` to `.envrc` and populate. (Do not )

## Start

```bash
jupyter notebook
```
