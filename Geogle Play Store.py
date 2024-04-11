import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('googleplaystore.csv')
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
data.shape
dup_data = data.duplicated().sum()
dup_data
data = data.drop_duplicates()
data.describe()
# Convert size,installs, and price from object to numerical data types
data['Size'].unique()
data['Size'].value_counts().sum()

# Converting size column function
#This function will convert the size column to numeric by multiplying the values with 1024  if it has 'k' in it and 1024*1024 if it has 'M' in it
def convert_size(size):
    if isinstance(size, str):
        if 'k' in size:
            return float(size.replace('k','')) * 1024
        elif 'M' in size:
            return float(size.replace('M', '')) * 1024 *1024
        elif 'Varies with device' in size:
            return np.nan
    return (size)
data['Size'] = data['Size'].apply(convert_size)
data.head()

# Changing the size column name from 'Size' to 'Size_in_bytes'
data.rename(columns={'Size' : 'Size_in_bytes'}, inplace=True)
data.head()

# Convert size_in_bytes to numeric
data['Size_in_bytes'].dtype
data['Size_in_bytes'] = pd.to_numeric(data['Size_in_bytes'], errors='coerce')
data['Size_in_Mb'] = data['Size_in_bytes'] / (1024 * 1024)
data['Size_in_Kb'] = data['Size_in_bytes'].apply(lambda x : x/(1024))

# Installs column
data['Installs'].unique()
data['Installs'].value_counts().sum()
print(data['Installs'].dtype)
import re
# Convert 'Installs' column to string type
data['Installs'] = data['Installs'].astype(str)

# Remove non-numeric values ('Free') from the 'Installs' column
data['Installs'] = data['Installs'].apply(lambda x: x.replace('Free', '0') if 'Free' in x else x)

# Remove the '+' character from the values
data['Installs'] = data['Installs'].apply(lambda x: x.replace('+', ''))

# Remove commas from the 'Installs' values
data['Installs'] = data['Installs'].str.replace(',', '')

# Convert 'Installs' values to integers
data['Installs'] = data['Installs'].astype(int)
data['Installs'].dtype

# making a new column called 'Installs_category' which will have the category of the installs
bins = [-1, 0, 10, 1000, 10000, 100000, 1000000, 10000000, 10000000000]
lables = ['no', 'Very Low', 'Low', 'Moderate', 'More than moderate', 'High', 'Very High','Top Notch']
data['Installs_category'] = pd.cut(data['Installs'],bins=bins,labels=lables)
data.head()

# Price column
data['Price'].unique()

# Remove non-numeric values ('Everyone') from the 'Price' column
data['Price'] = data['Price'].apply(lambda x: x.replace('Everyone', '0') if 'Everyone' in str(x) else x)

# Remove the dollar sign from the 'Price' values
data['Price'] = data['Price'].str.replace('$', '')

# Convert 'Price' values to floats
data['Price'] = data['Price'].astype(float)

data['Price'].dtype

# Use f string to print min, max, average of price
print(f"Min price is :{data['Price'].min()}$")
print(f"Max price is :{data['Price'].max()}$")
print(f"Average price is :{data['Price'].mean()}$")

# Convert 'Size_in_bytes' to numeric, handling 'M' suffix
data['Size_in_bytes'] = data['Size_in_bytes'].apply(lambda x: float(x.replace('M', '')) * 1024 * 1024 if isinstance(x, str) and 'M' in x else float(x))

# Recalculate 'Size_in_Mb' after the conversion
data['Size_in_Mb'] = data['Size_in_bytes'] / (1024 * 1024)

# Check if conversion was successful
print(data['Size_in_bytes'].dtype)

#Reviews column
# Convert 'Reviews' column to numeric
data['Reviews'] = pd.to_numeric(data['Reviews'], errors='coerce')

# Check the data type after conversion
print(data['Reviews'].dtype)
data['Reviews'] = data['Reviews'].astype(float)
print(data['Reviews'].dtype)

# Plot numerical columns
plt.figure(figsize=(16,10))
numeric_cols = ['Rating', 'Reviews',  'Size_in_bytes', 'Installs', 'Price', 'Size_in_Mb']
sns.heatmap(data[numeric_cols].corr(),annot=True)

data[numeric_cols].corr()

#plot Installs category and Reviews
plt.figure(figsize=(16,6))
sns.boxplot(x='Installs_category', y=np.log10(data['Reviews'],),color='brown', data=data)

# plot Reviews and Installs category to show number of reviews increases with increase in the number of installs
plt.figure(figsize=(16, 6)) 
sns.lmplot(x='Reviews', y='Installs', data=data) 

#1` Which category has the highest number of apps?
data.columns
data['Category'].value_counts().head(1)
#Result: Family

#2 Which category has the highest rating?
data.groupby('Category')['Rating'].mean().sort_values(ascending=False).head(1)
#Result: Events

#3 Which app has the highest content rating?
data['Content Rating'].value_counts()

plt.figure(figsize=(16, 7))
sns.barplot(x='Content Rating', y='Installs',color='pink', data=data)
#Result: Everyone

#4 Which are the top 3 paid apps with the highest number of reviews
data.columns
plt.figure(figsize=(16, 7)) 
sns.barplot(x='App', y='Reviews', color='red', data=data[data['Type'] == 'Paid'].sort_values(by='Reviews', ascending=False).head(3)) 

#5 Which is the range of rating in most apps?
plt.figure(figsize=(16,7))
sns.kdeplot(data['Rating'],color='purple',shade=True)

#6 Which type has the highest installs?
plt.figure(figsize=(16,6))
sns.barplot(x='Type',y='Installs',color='green',data=data)
#Result: Free


