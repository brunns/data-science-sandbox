# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Predicting wine quality using chemical properties
#
# See [Predicting wine quality using chemical properties](https://spiralizing.github.io/DSEntries/WineQuality/)

# %%
import pandas as pd
import numpy as np 

# %%
url_red = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
url_white = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"

rwine = pd.read_csv(str(url_red), sep=';')
wwine = pd.read_csv(str(url_white), sep=';')

# %%
rwine.head()

# %%
rwine.info()

# %%
rwine.describe()

# %%
