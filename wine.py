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
import numpy as np
import pandas as pd

# %%
red = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
    sep=";",
)
white = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv",
    sep=";",
)

# %%
red.head()

# %%
red.info()

# %%
red.describe()

# %%
