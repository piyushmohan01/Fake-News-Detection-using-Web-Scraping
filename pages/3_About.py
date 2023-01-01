import streamlit as st

st.title("About")

st.markdown('<div style="text-align: justify;">In today’s fast paced world, news articles have been growing hastier with flashy headlines and vague content. A fair percentage of readers do not consider making an effort to go a step further and confirm if the news they read holds any actual significance. We are aware of the consequences that might follow the spread of fake news and should avoid the same. The spread of fake news directly impacts the society as one often feels the need to share what he/she feels to be important and by doing so, without checking the authenticity of what they’re reading, they fall into the circle of passing misleading information. In this project, we present a solution that would check the authenticity of the news making it easier for the readers to know what to and what not to share ahead.</div>', unsafe_allow_html=True)

st.write("")

st.markdown('<div style="text-align: justify;">This project proposes an automatic fake news detecting system that will make use of a predictive model built with the help of thousands of news articles (both fake and true) that will take the URL of any news article as input and return a percentage score indicating the authenticity of the particular news article. We start by forming a dataset which consists of 20800 articles in total. Once the model is trained and produces a good score, we would place it behind an interface through which the user would be able to input the link to the news article which would be scraped by our system. The scraped content would then be passed onto the model to predict the authenticity of the news entered. With the help of the interface, users would be able to find out the authenticity of their articles in no time. The project uses different machine learning models and the strml. library to build the aforementioned parts. Once the project is ready and tested sufficient times, it would be deployed on the web for all users to access and use at will.</div>', unsafe_allow_html=True)

st.write("")

st.write("Made by Piyush Mohan (RA1911032010056) & Shubham Patil (RA1911032010045) with the help & guidance of Dr. A. Arokiaraj Jovith (Assistant Professor-SG)")