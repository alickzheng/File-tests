import tkinter as tk


def lcg_num(n, m = 9, a = 4, b = 1, seed = 0, res=[]):
    if n == 0:
        return res + [seed]
    else:
        res += [(a*lcg_num(n-1)[-1] + b)%m]
        return res

