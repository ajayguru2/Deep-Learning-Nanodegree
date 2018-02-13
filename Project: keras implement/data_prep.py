import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


admissions = pd.read_csv('binary.csv')


#making dummy variables for ranks

data = pd.concat([admissions, pd.get_dummies(admissions['rank'], prefix='rank')], axis=1)


data = data.drop('rank',axis=1)

#standardizing data

for field in ['gre', 'gpa']:
    mean, std = data[field].mean(), data[field].std()
    data.loc[:,field] = (data[field]-mean)/std

#split 10% data for testing at random

np.random.seed(21)
sample = np.random.choice(data.index, size=int(len(data)*0.95), replace=False)
data, test_data = data.ix[sample], data.drop(sample)

#split into features and targets

features, targets = data.drop('admit', axis=1), data['admit']
features_test, targets_test = test_data.drop('admit', axis=1), test_data['admit']

