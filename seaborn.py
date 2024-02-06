# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:09:02 2023

@author: ASUS
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.head()



'''
for categorization countplot is used 

'''
sns.countplot(x ='sex', data=df)

sns.countplot(x = 'sex', hue = 'survived', data= df)

sns.countplot(x = 'sex', hue = 'survived', data= df, palette = 'Set1')

sns.countplot(x = 'sex', hue = 'survived', data= df, palette = 'Set2')

sns.countplot(x = 'sex', hue = 'survived', data= df, palette = 'Set3')






sns.kdeplot(x = 'age', data = df, color = 'black')



sns.displot(x = 'age', kde =  True, bins = 6, data = df)


sns.displot(x = 'age', kde = True, bins = 5, hue =df['survived'],
            palette = 'Set1', data= df)



df = sns.load_dataset('iris')
df.head()

sns.scatterplot(x = 'sepal_length',y = 'sepal_width', data = df,
                hue = 'species')




sns.jointplot(x = 'sepal_length', y='petal_length', data = df, hue = 'species')


sns.jointplot(x = 'sepal_length', y = 'petal_length', data = df, kind = 'reg')

sns.jointplot(x = 'sepal_length', y='petal_length', data = df, kind = 'hist')


sns.jointplot(x = 'sepal_length', y = 'petal_length', data = df, kind = 'kde')



'''
plotting the pairplot

'''
sns.pairplot(df)




'''
heat map

'''
corr = df.corr()
sns.heatmap(corr)























