#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def movieList(movie_name):
    df1 = pd.read_csv("movie_dataset.csv")
    movie_list = list(df1["original_title"])
    movie_list[0]

    def get_title_from_index(index):
        return df1[df1.index == index]["title"].values[0]
    def get_index_from_title(title):
        return df1[df1.title == title]["index"].values[0]

    features = ['keywords','cast','genres','director']

    for feature in features:
        df1[feature] = df1[feature].fillna('')

    def combine_features(row):
            return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]

    df1["combined_features"] = df1.apply(combine_features,axis=1)

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df1["combined_features"])

    df1["combined_features"] = df1.apply(combine_features,axis=1)
    #df["combined_features"].head()
    cv = CountVectorizer()
    cosine_sim = cosine_similarity(count_matrix)
    movie_user_like = "Avatar"
    movie_index = get_index_from_title(movie_user_like)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)
    l = []
    i=1
    for elements in sorted_similar_movies:
        l.extend([get_title_from_index(elements[0])])
        if i>5:
            break
    return l      
