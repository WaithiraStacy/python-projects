# import python libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# import the data
data = pd.read_csv('tracks.csv')
# Check the first 5 rows of the dataset
data.head()
# Check the last 5 rows of the dataset
data.tail()
# Check for null values
data.isnull().sum()
# Check for information about the dataset
data.info()
# Find the first 5 most least popular artists
data.columns
data1 = data.sort_values('popularity',ascending=False).head()
data1
# Overall statistics about the data
data.describe().transpose()
# Find the most popular song
data.columns
data2 = data.groupby('name')['popularity'].sum().sort_values(ascending=False).reset_index().head(1)
data2
# Get the artist who is in the 20th row in the dataset
data.columns
data3 = data[['artists']].iloc[20]
data3
# Convert ms to seconds
data.columns
data['duration'] = data['duration_ms'].apply(lambda x: round(x/1000))
data.drop('duration_ms',inplace=True,axis=1)
data.duration.head()
# import the second data
data = pd.read_csv('SpotifyFeatures.csv')
# Check the first 10 rows of the dataset
data.head()
# Check for duplicated values in the dataset
data.duplicated().sum()
