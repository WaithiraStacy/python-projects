# import python libraries
import pandas as pd
import matplotlib.pyplot as plt
# import the datasets
confirmed = pd.read_csv('covid19 confirmed .csv')
deaths = pd.read_csv('covid19 deaths .csv')
recovered = pd.read_csv('covid19 recovered .csv')

# Drop uneceassary columns in the  dataset
confirmed = confirmed.drop(['Province/State','Lat','Long'], axis=1)
confirmed.head(1)
deaths = deaths.drop(['Province/State','Lat','Long'], axis=1)
deaths.head(1)
recovered = recovered.drop(['Province/State','Lat','Long'], axis=1)
recovered.head(1)

# Group columns by Country/Region
confirmed = confirmed.groupby(['Country/Region']).aggregate('sum')
confirmed.head(1)
deaths = deaths.groupby(['Country/Region']).aggregate('sum')
deaths.head(1)
recovered = recovered.groupby(['Country/Region']).aggregate('sum')
recovered.head(1)

# Return a tronsposed version of the dataframe
confirmed = confirmed.T
confirmed.head(1)
deaths = deaths.T
deaths.head(1)
recovered = recovered.T
recovered.head(1)

# Calculate the number of new cases
new_cases = confirmed.copy()

for day in range(1, len(confirmed)):
  new_cases.iloc[day] = confirmed.iloc[day] - confirmed.iloc[day-1]
    
print(new_cases.tail(10))
print(confirmed.tail(10))

