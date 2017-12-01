import pandas as pd
import numpy as np

X = pd.read_csv('titanic_data.csv')
# print X.head()
X = X.select_dtypes(include=[object])


from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

le = LabelEncoder()

aa = le.fit_transform(X['Embarked'])



# print le.transform(X['Embarked'])
# print X['Embarked'].head()	
ohe = OneHotEncoder()



dd = le.fit_transform(X['Embarked'])
ohe.fit(le.fit_transform(X['Embarked']))
print ohe.n_values_

# print ohe.n_values_

# print onehotlabels