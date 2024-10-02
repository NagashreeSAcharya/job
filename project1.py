#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
import re
from nltk.corpus import stopwords
import string
data = pd.read_excel("C:\\Users\\nagashree s acharya\\Downloads\\Jobs.xlsx")


# In[2]:



import matplotlib.pyplot as plt

jobs = ['Software Engineer', 'Data Scientist', 'UX Designer', 'Project Manager', 'Business Analyst']
recommendation_scores = [8, 9, 6, 7, 5]  # Sample recommendation scores for each job

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.barh(jobs, recommendation_scores, color='skyblue')
plt.xlabel('Recommendation Score')
plt.title('Job Recommendation Scores')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest score on top
plt.show()


# In[5]:




import matplotlib.pyplot as plt
job_categories = ['media planning executive', 'sales executive', 'R&D executive', 'technical support engineer','testing engineer']
job_counts = [25, 20, 15, 10,25]

plt.figure(figsize=(5, 5))
plt.pie(job_counts, labels=job_categories, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  
plt.title('Job Recommendations System')
plt.show()


# In[2]:


print(data.head())


# In[2]:


data.isnull().sum()


# In[3]:


text = " ".join(i for i in data["Key Skills"])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, 
background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[4]:


text = " ".join(i for i in data["Functional Area"])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords,background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[5]:


text = " ".join(i for i in data["Job Title"])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords,background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[24]:


def jobs_recommendation(Title, similarity = similarity):
    index = indices[Title]
    similarity_scores = list(enumerate(similarity[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[::], reverse=True)
    similarity_scores = similarity_scores[0:5]
    newsindices = [i[0] for i in similarity_scores]
    return data[['Job Title', 'Job Experience Required','Key Skills']].iloc[newsindices]
   
print(jobs_recommendation("Software Developer"))

