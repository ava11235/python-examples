
"""
KNN classifier with multple classes
This data is the result of a chemical analysis of wines 
grown in the same region in Italy using
three different cultivars (a grape variety which has been selectively cultivated.
The analysis determined the quantities of 13 constituents found 
 in each of the three types of wines.
"""

#Import scikit-learn dataset library
from sklearn import datasets
# Import train_test_split function
from sklearn.model_selection import train_test_split
#Import knearest neighbors Classifier model
from sklearn.neighbors import KNeighborsClassifier
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

#Load dataset
wine = datasets.load_wine()

# print features 
print("Wine features", wine.feature_names)

# print the labels (class_0, class_1, class_2)
print("Wine classes", wine.target_names)

# print the wine data 
print("First 5 records wine data", wine.data[0:5])

# print the wine labels (0:Class_0, 1:Class_1, 2:Class_3)
print("Winte labels for the 3 classes", wine.target)

# print data(feature)shape
print(wine.data.shape)


# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3) # 70% training and 30% test


#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=5)

#Train the model with the training sets
knn.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = knn.predict(X_test)
print("Response", y_pred)


# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))