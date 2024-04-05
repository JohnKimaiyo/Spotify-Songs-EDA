#!/usr/bin/env python
# coding: utf-8

# # Spotify Songs EDA
# 
# 
# EXPLORATORY DATA ANALYSIS: INTRODUCTION¶
# 
# 
# In this notebook we will take a look at the datasets available in this repository. We will focus on the dataset 1950.csv, which contains:
# 
# all the songs from the Spotify's playlist "All out 50s" that you can find here. This playlist collects the most popular and iconic songs from a given decade, in this case it collects the most popular songs from the 50s (1950-1959).
# for each listed song, a series of attributes are collected in every column of the dataset, as explained in the description of the dataset.
# The objective is to better understand the data, and study some relationships between the various attributes.

# # 1: LOAD PACKAGES AND DATA¶
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
spotify_df = pd.read_csv(r"C:\Users\jki\Downloads\sportify songs.csv")

# Show info and description of dataset
print(spotify_df.head(5))
spotify_df.info()
spotify_df.describe()


# In[2]:


# Set column Number as index
spotify_df.set_index('Number', inplace=True)

# Drop year column
spotify_df.drop(['year'], axis=1, inplace=True)

# Show updated dataframe
spotify_df.head(5)


# In[3]:


# Find missing values
spotify_df.isna().sum()


# # 2: GENRE ANALYSIS

# First, let's focus on the analysis of the categorical variable top genre. We can show a pie chart of the distribution of the genre. The pie chart shows that more than 50% of the most popular songs in the 50s are adult standards songs (whatever that means, I guess it's pop music). Clearly, we don't have any electronic music, or rap/hip-hop for that matter

# In[6]:


# Find percent of each genre
spotify_df_genre = spotify_df['top genre'].value_counts() / len(spotify_df)
sizes = spotify_df_genre.values.tolist()
labels = spotify_df_genre.index.values.tolist()

# Pie chart for genre
fig1, ax1 = plt.subplots(figsize=(10,10))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, textprops={'fontsize': 14})
ax1.axis('equal')
plt.show()


# # 3 BOXPLOT

# In[7]:


# Plot boxplot (variables only)
sns.boxplot(data=spotify_df.drop(['title', 'artist', 'top genre'], axis=1))
plt.xlabel('Features')
plt.ylabel('Value')
plt.show()


# # 4 PAIRPLOT

# In[9]:


sns.pairplot(data=spotify_df.drop(['title', 'artist'], axis=1), hue='top genre')
plt.show()


# # 5 CORRELATION MATRIX

# Finally, we can study the correlation matrix. This is one of the most commonly used tools to quickly understand how and how much the variables' behavior are related to each other. Furthermore, it allows us to better understand the observations/hypotheses we did when looking at the pairplot.
# 
# The correlation matrix shown below confirms what we already noticed previoulsy: most of the variables are positively related, meaning that they show a similar trend/behavior. The only variables showing a different behavior are dur and acous. Looking at the correlation matrix, one could infer that:
# 
# the longer the song, the less is has energy, danceability, loudness, liveness. This is understandable in terms of enery and danceability, less so in terms of loudness.
# the longer the song, the more it is popular. This is somewhat counter-intuitive, since most viral songs are short and catchy, at least nowadays. Almost certainly, music taste has changed from the 50s to today, and will change in the future as well.

# In[10]:


# Plot linear correlation matrix
fig, ax = plt.subplots(figsize=(15,10))
sns.heatmap(spotify_df.corr(), annot=True, cmap='YlGnBu', vmin=-1, vmax=1, center=0, ax=ax)
plt.title('LINEAR CORRELATION MATRIX')
plt.show()


# This wraps up this notebook. We took a good look at the attributes that define the most popular songs from the 50s.
# 
# The steps showed can be applied to the other available datasets, with the intent of tracking how the human music taste changed from the 50s to today.

# In[ ]:




