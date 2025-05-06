import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle


#read in csv file seperated by ;
data = pd.read_csv("student-mat.csv", sep=";")
print(data.head())

#create list using only selected attributes of data
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
print(data.head())

#label = G3, what we want to project
predict = "G3"

#create array without the G3 attribute
x = np.array(data.drop([predict], axis=1)) #features
#create array with only our desired projection (G3)
y = np.array(data[predict]) #labels

#split into arrays for training and test data of size 0.1 of total data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

linear = linear_model.LinearRegression()
#produces a best fit line using x and y training data
linear.fit(x_train, y_train)
#returns accuracy of our model
acc = linear.score(x_test, y_test)

print(acc)
print('Coefficient: \n', linear.coef_) #each slope value
print('Intercept: \n', linear.intercept_)  #y intercept

predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])
