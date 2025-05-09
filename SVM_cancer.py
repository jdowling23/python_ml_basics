import sklearn
from sklearn import svm
from sklearn import datasets
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

cancer = datasets.load_breast_cancer()

#print('Features: ', cancer.feature_names)
#print('Labels: ', cancer.target_names)

#split data into training and test
x = cancer.data     #features
y = cancer.target   #labels

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

#print(x_train[:5], y_train[:5])

#compare KNN with SVM, KNN acc = 92, SVM acc = 95
#clf = KNeighborsClassifier(n_neighbors=11)
clf = svm.SVC(kernel='linear', C=2) #soft margin value C=2
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test) # predict values for our test data

acc = metrics.accuracy_score(y_test, y_pred)    # test prediction against correct values
print(acc)
