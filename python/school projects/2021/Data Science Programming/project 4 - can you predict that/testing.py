from numpy.core.fromnumeric import ravel
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


data = data = pd.read_csv("dwellings_denver.csv")


values = train_test_split(data,test_size=.34,random_state=76)

table = values[0]
df = pd.DataFrame(table)


print(np.average([620000,714000,244500,98000,17113000,432500,485000,724500,185700,702500]))
#print(df.head(10))
#classifier = GaussianNB()
#classifier.fit(train_data, train_targets)
#targets_predicted = classifier.predict(test_data)

#print(list(targets_predicted))