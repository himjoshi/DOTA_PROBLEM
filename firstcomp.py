# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
train9 = pd.read_csv('train9.csv')
train1 = pd.read_csv('train1.csv')
hero_data = pd.read_csv('hero_data.csv')

#merging train9 and train1
train = pd.concat([train9, train1], axis = 0)

#checking for any nullvalues
hero_data.isnull().any().describe()

#visualizing these columns
hero_data['base_health'].value_counts()
hero_data['base_mana'].value_counts()
hero_data['base_mana_regen'].value_counts()
hero_data['base_magic_resistance'].value_counts()

hero_data = hero_data.drop(labels = ['base_health', 'base_mana', 'base_mana_regen'], axis = 1)

#merging hero_data and train
dataset = pd.merge(left=train,right=hero_data, left_on='hero_id', right_on='hero_id')
Y = dataset['kda_ratio']
X = dataset.drop(labels= ['kda_ratio'], axis = 1)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)
