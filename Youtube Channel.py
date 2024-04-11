import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('top-5000-youtube-channels.csv')
data.head()
data.tail()
data.dtypes
data.shape
print('Number of Rows',data.shape[0])
print('Number of Columns',data.shape[1])
data.info()
data.isnull().sum()
sns.heatmap(data.isnull())
dup_data = data.duplicated().sum()
dup_data
data.describe()
data.replace('--',np.NaN,regex=True,inplace=True)
# Clean Rank column
data.columns
data['Rank'] = data['Rank'].str[0:-2]
data['Rank'] = data['Rank'].str.replace(',','')
data['Rank'].dtypes
data['Rank'] = data['Rank'].astype(float)
data['Rank'].dtypes
# Convert numerical columns to float
data.columns
data['Video Uploads'].dtypes
data['Video Uploads']= data['Video Uploads'].astype(float)
data['Video Uploads'].dtypes
data['Subscribers'] = data['Subscribers'].astype(float)
data['Subscribers'].dtypes
data['Video views'] = data['Video views'].astype(float)
data['Video views'].dtypes
# Clean Grade column
data['Grade'].unique()
data['Grade'] = data['Grade'].map({'A++ ':5,'A+':4,'A ':3,'A- ':2,'B+ ':1})
data['Grade'].dtypes
data.dtypes
# 1 Find average subscription for each channel
data['avg_subscription']=data['Subscribers']/data['Video Uploads']
data.head(1)

#2 Find out the last 5 channels with minimum number of views
last_5 = data.sort_values(by='Video views').head()
last_5
# Visualize
x = last_5['Channel name']
y = last_5['Video views']
plt.xlabel('Channel name',fontsize=20,color='purple')
plt.ylabel('Video views',fontsize=20,color='purple')
plt.title('Channels with minimum number of video views',size=20)
plt.bar(x,y,color='red')
plt.xticks(rotation=60)
plt.show()
# Result: ItsHARSH007 Gaming, Bollywood Event Talkies, VideoClipVietNam, GumTea TV, DICHARA

#3 Which Grade a minimum number of video uploads
data.columns
grade = data.groupby('Grade')['Video Uploads'].sum().sort_values()
grade
# Visualize
ax = grade.plot(kind='bar',color='brown',logy=True,figsize=(10,6))
plt.xlabel('Grades',fontsize=20,color='green')
plt.ylabel('Video Uploads',fontsize=20,color='green')
plt.title('Grades with minimum number of Video Uploads',size=20,color='green')
plt.show()
# Result: 5.0
 
#4 Which Grade has the lowest number of subscribers
data.columns
grade_sub = data.groupby('Grade')['Subscribers'].sum().sort_values()
grade_sub
# Visualize
ax = grade.plot(kind='bar',color='black',logy=True,figsize=(10,6))
plt.xlabel('Grades',fontsize=20,color='brown')
plt.ylabel('Subscribers',fontsize=20,color='brown')
plt.title('Grades with lowest number of Subscribers',size=20,color='brown')
plt.show()
# Result: 5.0

#5 Find out the last 5 channels with minimum number of Subscribers
data.columns
last_S= data.sort_values(by='Subscribers').head()
last_S
# Visualize
x = last_S['Channel name']
y = last_S['Subscribers']
plt.xlabel('Channel name',fontsize=20,color='red')
plt.ylabel('Subscribers',fontsize=20,color='red')
plt.title('Channels with minimum number of subscribers',size=20,color='red')
plt.bar(x,y,color='black')
plt.xticks(rotation=60)
plt.show()
#Result: Xiaomi France, hairong zheng, Jianpeng Li, Ron Funches - Topic, Ron Funches - Topic

#6 Which grade has the lowest Video Views 
data.columns
grade_views = data.groupby('Grade')['Video views'].sum().sort_values()
grade_views
# Visualize
ax = grade.plot(kind='bar',color='purple',logy=True,figsize=(10,6))
plt.xlabel('Grades',fontsize=20,color='hotpink')
plt.ylabel('Video views',fontsize=20,color='hotpink')
plt.title('Grades with lowest number of Video Views',size=20,color='hotpink')
plt.show()
# Result: 5.0


