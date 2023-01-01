import streamlit as st
from scrape import *
import pickle
import math
import time

st.title("Fake News Detector")

model_filename = 'pickles/PA.pickle'
vectorizer_filename = 'pickles/tfidf_vectorizer.pickle'
vectorizer = pickle.load(open(vectorizer_filename, 'rb'))
model = pickle.load(open(model_filename, 'rb'))

import re
import string
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

perc = 0
url = st.text_area("Enter URL")
if url != '':
    test = c(url)
    test_x = wordopt(test)
    tfidf_x = vectorizer.transform([test_x])
    pred = model.predict(tfidf_x)
    result = math.ceil(model._predict_proba_lr(tfidf_x)[0][1]*100)
    print(result,"% True.")
    perc = result

    col1, col2 = st.columns([3, 1])
    with col1:
        my_bar = st.progress(0)
        for percent_complete in range(perc):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
    with col2:
        st.write(perc, "% True.")

st.markdown("---")

st.write("Steps to continue: ")
st.write("1. Find URL of News article.")
st.write("2. Copy and Paste the URL in text area.")
st.write("3. Press CTRL+Enter to run the model.")
st.write("4. Obtain results in slider and text form.")
st.write("5. Paste new URL over text area to re-use.")
st.write("6. Check other pages for more info and help.")
