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
from IPython.display import display
from sympy import *
from sympy.plotting import plot3d

# %%
x, y, z = symbols("x y z")
f = x**2 + 1
display(f)
plot(f)

# %%
f2 = (2 * x) ** 2 + y**2
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
area_f = integrate(f, x)
display(area_f)
plot(area_f)

# %%
f3 = f.subs(x, 5)
display(f3)
l = lambdify(x, f)
l(5)

# %%
