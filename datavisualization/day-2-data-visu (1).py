# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HIuBK5niA3G8zrqhjgFhwpDaegc4AKYW
"""

import seaborn as sns

iris = sns.load_dataset('iris')

iris

sns.pairplot(iris)

sns.set(style="ticks", color_codes=True)
sns.pairplot(iris, hue="species")