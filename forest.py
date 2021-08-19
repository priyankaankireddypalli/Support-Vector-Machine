# 2
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
v1 = pd.read_csv("C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\Black box\\forestfires.csv")
v1.describe()
v1.dtypes
v1['month']= labelencoder.fit_transform(v1['month'])
v1['day'] = labelencoder.fit_transform(v1['day'])
v1['size_category'] = labelencoder.fit_transform(v1['size_category'])
v1=pd.get_dummies(v1)
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
train,test = train_test_split(v1, test_size = 0.20)
train_X = train.iloc[:, 0:30]
train_y = train.iloc[:, -1]
test_X  = test.iloc[:, 0:30]
test_y  = test.iloc[:, -1]

# kernel = linear
help(SVC)
model_linear = SVC(kernel = "linear")
model_linear.fit(train_X, train_y)
pred_test_linear = model_linear.predict(test_X)
np.mean(pred_test_linear == test_y)

# kernel = rbf
model_rbf = SVC(kernel = "rbf")
model_rbf.fit(train_X, train_y)
pred_test_rbf = model_rbf.predict(test_X)
np.mean(pred_test_rbf==test_y)

# kernel = poly
model_linear = SVC(kernel = "poly")
model_linear.fit(train_X, train_y)
pred_test_linear = model_linear.predict(test_X)
np.mean(pred_test_linear == test_y)

# kernel = sigmoid
model_rbf = SVC(kernel = "sigmoid")
model_rbf.fit(train_X, train_y)
pred_test_rbf = model_rbf.predict(test_X)
np.mean(pred_test_rbf==test_y)
