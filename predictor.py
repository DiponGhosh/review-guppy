#classifier.py
import pickle
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def Predictor(list_of_review):

    classifier_model = pickle.load(open('trained_model.pkl', 'rb'))
    vectorizer_model = pickle.load(open('vectorized_model.pkl', 'rb'))


    '''
    for item in list_of_review:
        print(item + "\n\n")
    '''

    #nltk.download('stopwords')

    input = np.array(list_of_review)
    input_test = np.array([])

    for i in range(0, input.size):
        rev = input[i]
        rev = rev.lower()
        rev = rev.split()
        ps = PorterStemmer()
        rev = [ps.stem(word) for word in rev if not word in set(stopwords.words('english'))]
        rev = ' '.join(rev)
        input_test = np.append(input_test, rev)

    T_in = vectorizer_model.transform(input_test).toarray()
    T_out = classifier_model.predict(T_in)

    cnt_pos = 0
    cnt_neg = 0
    cnt_neu = 0

    for i in range(0, len(T_out)):
        if T_out[i] == 0.0:
            cnt_pos = cnt_pos + 1
        if T_out[i] == 1.0:
            cnt_neg = cnt_neg + 1
        if T_out[i] == 2.0:
            cnt_neu = cnt_neu + 1


    pos = format( ((cnt_pos / len(T_out)) * 100), '.2f' )
    neg = format( ((cnt_neg / len(T_out)) * 100), '.2f' )
    neu = format( ((cnt_neu / len(T_out)) * 100), '.2f' )


    list_result = [pos, neg, neu]

    return list_result
