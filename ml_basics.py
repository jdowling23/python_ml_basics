from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
#validating a ML model
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.metrics import confusion_matrix
#splitting data into training and test sets
from sklearn.model_selection import train_test_split

#linear regression
your_model = LinearRegression()
your_model.fit(x_training_data, y_training_data)
predictions = your_model.predict(your_x_data)


#Naive Bayes classification
your_model = MultinomialNB()
your_model.fit(x_training_data, y_training_data)
#returns a list of predicted classes - one prediciton for every data point
predictions = your_model.predict(your_x_data)
#for every data point, returns a list of probabilities of each class
probabilities = your_model.predict_proba(your_x_data)


#K-nearest neighbors (KNN)
your_model = KNeighborsClassifier()
your_model.fit(x_training_data, y_training_data)
#returns a list of predicted classes - one prediction for every data point
predictions = your_model.predict(your_x_data)
#for every data point, returns a list of probablities of each class
probabilities = your_model.predict_proba(your_x_data)


#K-means clustering
your_model = KMeans(n_clusters=4, init='random')    #number of clusters and number of centroids to generate
#random = K-means
#k-means++ = K-means++[default]
your_model.fit(x_training_data)
predictions = your_model.predict(your_x_data)

#validates ML model
print(accuracy_score(true_labels, guesses))
print(recall_score(true_labels, guesses))
print(precision_score(true_labels, guesses))
print(f1_score(true_labels, guesses))
#confusion matrix
print(confusion_matrix(true_labels, guesses))

#training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)
#train_size = proportion of the dataset to include in the train split
#test_size = proportion of the dataset to include in the test split
#random_state = seed used by the random number generator [optional]
