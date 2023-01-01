import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import numpy as np
import pickle
import math
from scrape import c

model_filename = 'pickles/PA.pickle'
vectorizer_filename = 'pickles/tfidf_vectorizer.pickle'
vectorizer = pickle.load(open(vectorizer_filename, 'rb'))
model = pickle.load(open(model_filename, 'rb'))

import re
import string
def wordopt(text):
    text 
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

link = input("")
test = c(link)
test_x = wordopt(test)
tfidf_x = vectorizer.transform([test_x])
pred = model.predict(tfidf_x)
result = math.ceil(model._predict_proba_lr(tfidf_x)[0][1]*100)
print(result,"% True.")
