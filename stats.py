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
# # Playing with stats

# %%
import duckdb
import pandas as pd

mydf = pd.DataFrame({"a": [1, 2, 3]})
print(duckdb.query("SELECT SUM(a) FROM mydf").to_df())

# %%
