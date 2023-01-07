# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Importing the dataset
dataset = pd.read_csv('Tweet_result_ud.tsv', delimiter = '\t', quoting = 3)

# Cleaning the texts
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', str(dataset['Tweet'][i]))
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10, random_state = 0)


#-------------------------------------------Fitting Naive Bayes to the Training set
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
cm_nb = confusion_matrix(y_test, y_pred)
accuracy_nb = ((cm_nb[0][0]+cm_nb[1][1])/100)*100
print ("Accuracy for Naive Bayes Classifier :" , accuracy_nb )


#----------------------------------- Fitting Decision Tree Classification to the Training set
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
cm_dtc = confusion_matrix(y_test, y_pred)
accuracy_dtc = ((cm_dtc[0][0]+cm_dtc[1][1])/100)*100
print ("Accuracy form Decision Tree Classification  :" , accuracy_dtc )



#--------------------------------------------- Fitting Random Forest Classification to the Training set
classifier = RandomForestClassifier(n_estimators = 40, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
cm_rfc = confusion_matrix(y_test, y_pred)
accuracy_rfc = ((cm_rfc[0][0]+cm_rfc[1][1])/100)*100
print ("Accuracy form Random Foreset Classification  :" , accuracy_rfc )



#------------------------------------------------------Fitting SVM to the Training set
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
cm_svm = confusion_matrix(y_test, y_pred)
accuracy_svm = ((cm_svm[0][0]+cm_svm[1][1])/100)*100
print ("Accuracy for SVM   :" , accuracy_svm )
