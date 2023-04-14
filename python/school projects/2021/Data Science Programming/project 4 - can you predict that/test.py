#%%
from numpy.core.fromnumeric import ravel
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

#load data
url = "https://byuistats.github.io/CSE250-Course/skill_builders/ml_sklearn/machine_learning.csv"
data = pd.read_csv(url)

#split data

def classify(data,test_percent,target,data_columns):

    data = data.to_numpy()

    split = train_test_split(data,.34,random_state=76)

    print(split)

    train_data = split[0][data_columns]
    test_data = split[1][data_columns]
    train_targets = split[0][target]
    test_targets = split[1][target]

    train_data = train_data.to_numpy()
    test_data = test_data.to_numpy()
    train_targets = train_targets.to_numpy().ravel()
    test_targets = test_targets.to_numpy().ravel()

    # classify data
    classifier = GaussianNB()
    classifier.fit(train_data, train_targets)
    targets_predicted = classifier.predict(test_data)

    return(list(targets_predicted))

print(classify(data,.3,['survived'],["pclass",'sex','age']))

# %%
