import pandas as pd
data = pd.read_csv('file (3).csv')
data.head()
data.tail()
data.shape
print('Number of Rows',data.shape[0])
print('Number of Columns',data.shape[1])
data.info()
data.isnull().sum()
dup_data = data.duplicated().sum()
dup_data
data.describe()

#1 Show the records related to districts 'Kargil','Kathua' and 'Bandipore'
data.head(10)
data[data['District_name'].isin(['Kargil','Kathua','Bandipore'])]

#2 Display total number of poplulation by;
 # Statename
data.columns
data.groupby('State_name')['Population'].sum().reset_index()
# Districtname
data.groupby('District_name')['Population'].sum().reset_index()

#3 Find the most populated district and the least populated district
data.groupby('District_name')['Population'].sum().sort_values(ascending=False).reset_index().head(1)
data.groupby('District_name')['Population'].sum().sort_values().reset_index().head(1)
#Result:Thane(Most populated)
#       Dibang Valley(Least populated)

#4 How many female workers are there in 'Nicobars' District
data.tail()
data[data['District_name'] == 'Nicobars']['Female_Workers'].sum()
# Result: 4411

# 5 Display the first 5 districts with the highest number of literate people
data.columns
data.groupby('District_name')['Literate'].sum().sort_values(ascending=False).reset_index().head()

#6 Display the number of females(statewise)
data.columns
data.groupby('State_name')['Female'].sum()

#7 Show the last 5 Districts with the least number of workers
data.columns
data.groupby('District_name')['Workers'].sum().sort_values().reset_index().head()

#8 Which State has the highest number of cultivator_workers
data.columns
data.groupby('State_name')['Cultivator_Workers'].sum().sort_values(ascending=False).reset_index().head(1)
#Result: UTTAR PRADESH

#9 Display the first 4 states with the highest number of christians
data.columns
data.groupby('State_name')['Christians'].sum().sort_values(ascending=False).reset_index().head(4)

#10 Which district has the highest number of graduates and which district has the least number of graduates
data.columns
data.groupby('District_name')['Graduate_Education'].sum().sort_values(ascending=False).reset_index().head(1)
data.groupby('District_name')['Graduate_Education'].sum().sort_values().reset_index().head(1)
#Result: Bangalore(Highest)
#        Dibang Valley(least)

#11 Which state has the highest number of youngest people
data.columns
data.groupby('State_name')['Age_Group_0_29'].sum().sort_values(ascending=False).reset_index().head(1)
#Result: UTTAR PRADESH

#12 Which state has the highest number of old people
data.columns
data.groupby('State_name')['Age_Group_50'].sum().sort_values(ascending=False).reset_index().head(1)
#Result: UTTAR PRADESH

#13 Display the first 10 districts with the highest number of male workers
data.columns
data.groupby('District_name')['Male_Workers'].sum().sort_values(ascending=False).reset_index().head(10)

#14 Which state has the highest number of household workers?
data.columns
data.groupby('State_name')['Household_Workers'].sum().sort_values(ascending=False).reset_index().head(1)
#Result: UTTAR PRADESH

#15 How many people are there in BIHAR state?
data.columns
data[data['State_name'] == 'BIHAR'].sum()

