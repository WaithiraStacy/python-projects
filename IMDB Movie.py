import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('IMDB-Movie-Data.csv')
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
data.dtypes

#1 Display title of movies having >=400000 votes
data.head(1)
data[data['Votes']>=400000]['Title']

#2 Which year has the highest votes and which year has the lowest votes?
data.columns
sns.barplot(x= 'Year',y='Votes',data=data)
plt.title("Votes by Year")
#Result: 2012 has the highest votes while 2016 has the lowest votes

#3 Which year has the highest and lowest Revenue?
sns.barplot(x= 'Year',y='Revenue (Millions)',data=data)
plt.title("Revenue by Year")
#Result: 2009 has the highest Revenue while 2016 has the lowest Revenue

#4 Which content has most movies? music or fantacy?
data[data['Genre'].str.contains('Music')]
data[data['Genre'].str.contains('Fantasy')]
#Result: fantacy

#5 Find average Metascore for each director
data.groupby('Director')['Metascore'].mean().sort_values(ascending=False)

#6 Display number of movies per year
sns.countplot(x='Year',data=data)
plt.title("Number of movies per year")

#7 Find the most popular movie(Highest Rating)
data[data['Rating'].max()== data['Rating']]['Title']
#Result: The Dark Knight

#8 Display top5 highest rated movie titles and their directors
top_5 = data.nlargest(5,'Rating')[['Title','Rating','Director']].set_index('Title')
top_5
#Visualize
sns.barplot(top_5['Rating'])
plt.title("Top 5 highest rated movie titles")
plt.xticks(rotation=60)


#9 Display top5 highest revenue  movies
data.sort_values(by='Revenue (Millions)',ascending=False).head()
top_5 = data.nlargest(5,'Revenue (Millions)')[['Title','Director','Revenue (Millions)']].set_index('Title')
#Visualize
data.columns
sns.barplot(top_5['Revenue (Millions)'],color='purple')
plt.title("Top 5 highest revenue movies",fontsize=20)
plt.xticks(rotation=60)
plt.show()

#10 Does rating affect revenue?
sns.scatterplot(x='Rating',y='Revenue (Millions)',data=data)
#Result: Yes

#11 Classify movies based on Ratings(Good,Better,Best)
def rating(rating):
    if rating >=8.0:
        return 'Best'
    elif rating >= 6.0:
        return 'Better'
    else:
        return 'Good'
    
data['rates']=data['Rating'].apply(rating)
data.head(1)

#12 Find the total number of movies with Best rates
data[data['rates'].str.contains('Best')]
#Result: 70


