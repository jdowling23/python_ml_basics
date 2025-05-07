import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

#read in csv file seperated by ;
data = pd.read_csv("student-mat.csv", sep=";")
#print(data.head())

#create list using only selected attributes of data
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
data = shuffle(data) #optional - shuffles the data
#print(data.head())

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

#train multiple models and save best one
best = 0
for _ in range(20):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print('Accuracy: ' + str(acc))

    if acc > best:
        best = acc
        # save model and write to new file using pickle.dump()
        with open('studentgrades.pickle', 'wb') as f:
            pickle.dump(linear, f)

#loads our model
pickle_in = open('studentgrades.pickle', 'rb')
linear= pickle.load(pickle_in)

print(acc)
print('------------------')
print('Coefficient: \n', linear.coef_) #each slope value
print('Intercept: \n', linear.intercept_)  #y intercept
print('------------------')

predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

plot = 'G1' # change to G1, G2, studytime or absences to see other graphs
plt.scatter(data[plot], data['G3'])
plt.legend(loc=4)
plt.xlabel(plot)
plt.ylabel('Final Grade')
plt.show()
