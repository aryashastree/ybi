# -*- coding: utf-8 -*-
"""Ybi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SYNj5eE2pGJxuLRXHWf4Uf7iAUok4XFe

**Movie Recommendation System**

**Recommender System:** is a system that seeks to predict or filter preferences according to the user's choices. Recommender systems are
utilized in a variety of areas including movies, music, news, books, research articles, search queries, social tags, and products in general.
Recommender systems produce a list of recommendations in any of the two ways-

**Collaborative filtering:** Collaborative filtering approaches build a model from the user's past behavior (ie. items purchased or searched by the user) as well as similar decisions made by other users. This model is then used to predict items (or ratings for items) that users may have an interest in

**Content-based filtering:** Content-based filtering approaches uses a series of discrete characteristics of an item in order to recommend additional iterns with similar properties. Content-based filtering methods are totally based on a description of the item and a profile of the user's preferences. It recommends items based on the user's past preferences. Let's develop a basic recommendation system using Python and Pandas.

Let's develop a basic recommendation system by suggesting items that are most similar to a particular item, in this case, movies. It just tells what movies/items are most similar to the user's movie choice.
"""

import pandas as pd

import numpy as np

"""**Import Library**"""

df = pd.read_csv('https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Movies%20Recommendation.csv')

df.head()

df.info()

df.shape

df.columns

df_features = df[['Movie_Genre','Movie_Keywords','Movie_Tagline','Movie_Cast','Movie_Director']].fillna('')

df_features.shape

df_features

x=df_features['Movie_Genre']+ ' '+df_features['Movie_Keywords']+ ' ' + df_features['Movie_Tagline']+' '+ df_features['Movie_Cast'] + ' '+ df_features['Movie_Director']

x

x.shape

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()

x = tfidf.fit_transform(x)

x.shape

print(x)

"""cosine_similarity computes the L2 normalized product of vectors .Euclidean(L2) normalization project the vectors onto the unit sphere, and their dot product is then the cosine of the angle between the points denoted by the vectors."""

from sklearn.metrics.pairwise import cosine_similarity

similarity_Score = cosine_similarity(x)

similarity_Score

similarity_Score.shape

favourite_Movie_Name = input('Enter youyr favourite movie name : ')

All_Movie_Title_List = df['Movie_Title'].tolist()

import difflib

Movie_Recommendation = difflib.get_close_matches(favourite_Movie_Name,All_Movie_Title_List)
print(Movie_Recommendation)

Close_Match = Movie_Recommendation[0]
print(Close_Match)

Index_of_Close_Match_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]

#getting a list of similar movies
Movie_Recommendation_score = list(enumerate(similarity_Score[Index_of_Close_Match_Movie]))
print(Movie_Recommendation_score)

len(Movie_Recommendation_score)

#sorting the movie based on their similarity score
Sorted_Similar_Movies = sorted(Movie_Recommendation_score,key = lambda x:x[1], reverse = True)
print(Sorted_Similar_Movies)

i =1
for movie in Sorted_Similar_Movies:
  index = movie[0]
  title_from_index = df[df.index == index]['Movie_Title'].values[0]
  if (i<30):
    print(i,'.',title_from_index)
    i+=1

Movie_Name = input("Enter your favourite movie name : ")

list_of_all_titles = df['Movie_Title'].tolist()

Find_Close_Match = difflib.get_close_matches(Movie_Name,list_of_all_titles)

Close_Match = Find_Close_Match[0]

Index_of_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]

Movie_Recommendation_score = list(enumerate(similarity_Score[Index_of_Movie]))

Sorted_Similar_Movies = sorted(Movie_Recommendation_score,key = lambda x:x[1], reverse = True)

print('Top 10 Movies suggested for you : \n')

i = 1

for movie in Sorted_Similar_Movies:
  index = movie[0]
  title_from_index = df[df.Movie_ID==index]['Movie_Title'].values
  if (i<10):
    print(i,'.',title_from_index)
    i+=1