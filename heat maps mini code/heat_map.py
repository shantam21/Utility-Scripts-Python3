# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:16:49 2019

@author: shansaxena
"""

import pandas as pd

df= pd.read_csv('heat_map.csv')


import matplotlib.pyplot as plt
import seaborn as sns


df = df.set_index('Product')

heat_map = sns.heatmap(df,cmap="BuGn_r")
fig= heat_map.get_figure()
fig.savefig("output.png",bbox_inches="tight")

