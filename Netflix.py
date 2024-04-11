import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('file (5).csv')
data.head()
data.tail()
data.shape
print('Number of Rows',data.shape[0])
print('Number of Columns',data.shape[1])
data.info()
data.isnull().sum()
per_missing = data.isnull().sum()*100/len(data)
per_missing
data.dropna(axis=0,inplace=True)
dup_data = data.duplicated().sum()
dup_data
data.describe()

#1 How many movies and Tv shows are in the dataset. Show in bargraph
data.head(1)
data.groupby('Category').Category.count()
#Visualize
sns.countplot(data['Category'])
#Result: Movies=4675
       # Tv shows=136

#2 Show top 5 directors who gave the highest number of Tv shows and movies on netflix
data.head(1)
data['Director'].value_counts().head()

#3 Show all the records where category is movie and type is music or country is India
data.head(1)
data[(data['Category']=='Movie')&(data['Type']=='Music')|(data['Country']=='India')]

#4 In how many movies/Tv shows Chevy Chase was cast
data.head(1)
data[data['Cast'].str.contains('Chevy Chase')]
#Result: 4

#5 What are the different ratings defined by Netflix
data.head(1)
data['Rating'].nunique()
data['Rating'].unique()
#Result: TV-MA', 'R', 'PG-13', 'TV-14', 'TV-G', 'TV-PG', 'NR', 'PG', 'G','TV-Y7', 'TV-Y', 'NC-17', 'TV-Y7-FV', 'UR'

#6 What is the minimum duration of a movie show on Netflix?
data.head(1)
data.Duration.unique()
data.Duration.dtypes
data[['min','unit']] = data['Duration'].str.split(' ',expand=True)
data.head(1)
data['min'].min()
#Result: 1 minute
  
#7 Which indivitual country has the highest number of movies
data.head(1)  
data_movie = data[data['Category']=='Movie']
data_movie.Country.value_counts().head(1)
#Result: United States

#8 Sort the data by rating
data.head(1)
data.sort_values(by='Rating')

#9 Display where category is movie and type is horror or category is Tv show and type is crime Tv
data.head(1)
data[(data['Category']=='Movie') & (data['Type'] =='Dramas')|(data['Category']=='TV Show')&(data['Type']=='kids Tv')]

                 