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
# # Playing with [SymPy](https://pinboard.in/u:brunns/t:sympy)

# %%
from sympy import *
from sympy.plotting import plot3d
from IPython.display import display

# %%
x, y = symbols("x y")
f = x**2 + 1
plot(f)

# %%
f2 = (2*x)**2 + y**2
display(f2)
plot3d(f2)


# %%
dx_f = diff(f, x)
display(dx_f)

# %%
dx_f = diff(f2, x)
dy_f = diff(f2, y)
display(dx_f)
display(dy_f)

# %%
