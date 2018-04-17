# Natural Language Processing
# Analysis of sentiment from reviews


# # Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud, STOPWORDS

import pickle

# # Importing dataset
dataset = pd.read_csv('ftd.txt', delimiter = '\t', quoting = 3)


# # Cleaning the dataset

# to download the stopwords
# nltk.download('stopwords')
#dataset = dataset[dataset['review-text'].notnull()]
#nan_rows = dataset[dataset['review-text'].isnull()]

dataset = dataset.fillna(' ')

corpus = []

for i in range(0, 999):
    review = re.sub('[^a-zA-Z]', ' ' , dataset['review-text'][i])
    header = re.sub('[^a-zA-Z]', ' ' , dataset['review-title'][i])
    review = header + ' ' + review
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)



# # Creating a bag of model and
# # get feature matrix for training

#cv = TfidfVectorizer(use_idf = True, strip_accents = 'ascii')
cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray()

pickle.dump(cv, open('vectorized_model_final.pkl', 'wb'))

#hence 0 is positive
# 1 is negative
# and 2 is neutral

y = np.array([])

for i in range(0, 999):
    if dataset['rating'][i][0] == '5'or dataset['rating'][i][0] == '4':
        y = np.append(y, 0)
    elif dataset['rating'][i][0] == '1'or dataset['rating'][i][0] == '2':
        y = np.append(y, 1)
    elif dataset['rating'][i][0] == '3':
        y = np.append(y, 2)



# Putting naive bayes classifier to the dataset
# Splitting the dataset into train and test set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10, random_state = 42)

'''
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
'''

# Fitting Naive Bayes to the trainig set

classifier = MultinomialNB()
classifier.fit(X_train, y_train)

pickle.dump(classifier, open('trained_model_final.pkl', 'wb'))

#roc_auc_score(y_test, classifier.predict_proba(X_test))


# Predicting the test set result
y_pred = classifier.predict(X_test)


# Making the confusion Matrix
cm = confusion_matrix(y_test, y_pred)

list_of_review = ["One Star idiot.. brand new coolpad note3 lite is for 6000"]

input = np.array(list_of_review)
input_test = np.array([])

for i in range(0, input.size):
    rev = input[0]
    rev = rev.lower()
    rev = rev.split()
    ps = PorterStemmer()
    rev = [ps.stem(word) for word in rev if not word in set(stopwords.words('english'))]
    rev = ' '.join(rev)
    input_test = np.append(input_test, rev)


T_in = cv.transform(input_test).toarray()
T_out = classifier.predict(T_in)


#visualizing training dataset

cleanWord = ""

for i in range(0, len(corpus)):
    cleanWord = cleanWord + corpus[i]

wordcloud = WordCloud(
                      relative_scaling = 1.0,
                      stopwords = STOPWORDS
                      ).generate(cleanWord)

fig = plt.figure(figsize=(10, 6))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()






