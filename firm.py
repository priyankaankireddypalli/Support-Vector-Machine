# 1
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
labelencoder = LabelEncoder()
salary_Train=pd.read_csv("C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\Black Box (SVM)\\SalaryData_Train (1).csv")
salary_Train.dtypes
salary_Train['workclass']= labelencoder.fit_transform(salary_Train['workclass'])
salary_Train['education'] = labelencoder.fit_transform(salary_Train['education'])
salary_Train['maritalstatus'] = labelencoder.fit_transform(salary_Train['maritalstatus'])
salary_Train['occupation']= labelencoder.fit_transform(salary_Train['occupation'])
salary_Train['relationship'] = labelencoder.fit_transform(salary_Train['relationship'])
salary_Train['race'] = labelencoder.fit_transform(salary_Train['race'])
salary_Train['sex']= labelencoder.fit_transform(salary_Train['sex'])
salary_Train['native'] = labelencoder.fit_transform(salary_Train['native'])
salary_Train['Salary'] = labelencoder.fit_transform(salary_Train['Salary'])
salary_train_x=salary_Train.iloc[:,0:13]
salary_train_y=salary_Train.iloc[:,-1]

salary_Test=pd.read_csv("C:\\Users\\rammo\\Downloads\\DS\\Black Box (SVM)\\SalaryData_Test (1).csv")
salary_Test['workclass']= labelencoder.fit_transform(salary_Test['workclass'])
salary_Test['education'] = labelencoder.fit_transform(salary_Test['education'])
salary_Test['maritalstatus'] = labelencoder.fit_transform(salary_Test['maritalstatus'])
salary_Test['occupation']= labelencoder.fit_transform(salary_Test['occupation'])
salary_Test['relationship'] = labelencoder.fit_transform(salary_Test['relationship'])
salary_Test['race'] = labelencoder.fit_transform(salary_Test['race'])
salary_Test['sex']= labelencoder.fit_transform(salary_Test['sex'])
salary_Test['native'] = labelencoder.fit_transform(salary_Test['native'])
salary_Test['Salary'] = labelencoder.fit_transform(salary_Test['Salary'])
salary_test_x=salary_Test.iloc[:,0:13]
salary_test_y=salary_Test.iloc[:,-1]

# kernel = linear
model_linear = SVC(kernel = "linear")
model_linear.fit(salary_train_x, salary_train_y)
pred_test_linear = model_linear.predict(salary_test_x)
np.mean(pred_test_linear == salary_test_y)

# kernel = rbf
model_rbf = SVC(kernel = "rbf")
model_rbf.fit(salary_train_x, salary_train_y)
pred_test_rbf = model_rbf.predict(salary_test_x)
np.mean(pred_test_rbf==salary_test_y)

# kernel = poly
model_rbf = SVC(kernel = "poly")
model_rbf.fit(salary_train_x, salary_train_y)
pred_test_rbf = model_rbf.predict(salary_test_x)
np.mean(pred_test_rbf==salary_test_y)

# kernel = sigmoid
model_rbf = SVC(kernel = "sigmoid")
model_rbf.fit(salary_train_x, salary_train_y)
pred_test_rbf = model_rbf.predict(salary_test_x)
np.mean(pred_test_rbf==salary_test_y)

