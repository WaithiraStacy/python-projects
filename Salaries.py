import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('Salaries.csv')
data.head()
data.tail()
data.shape
print('Number of Rows',data.shape[0])
print('Number of Columns',data.shape[1])
data.info()
data.isnull().sum()
sns.heatmap(data.isnull())
per_missing = data.isnull().sum()*100/len(data)
per_missing
data.dropna(axis=0, inplace = True)
data.shape
dup_data = data.duplicated().sum()
dup_data
data.describe()
data.dtypes
data.drop(['Id','Year','Notes','Agency'],axis=1, inplace = True)
data.columns
#1 Find the name of the employee with the highest total pay
data.columns
data['TotalPay'] = data['TotalPay'].astype(int)
data.dtypes
data1 = data.groupby('EmployeeName')['TotalPay'].sum().sort_values(ascending= False).reset_index()
data1
# Result: Kelvin Lee

#2 Which Job Title has the highest other pay?
data.columns
data['OtherPay'] = data['OtherPay'].astype(bool)
data['OtherPay'] = data['OtherPay'].astype(int)
data.dtypes
data2 = data.groupby('JobTitle')['OtherPay'].sum().sort_values(ascending=False).reset_index()
data2
# Result: Transit Operator

#3 Which job has the highest Basepay?
data.columns
data['BasePay'] = data['BasePay'].astype(bool)
data['BasePay'] = data['BasePay'].astype(int)
data.dtypes
data3 = data.groupby('JobTitle')['BasePay'].sum().sort_values(ascending=False).reset_index()
data3
# Result: Transit operator

# 4 Which job has the highest overtime pay?
data.columns
data['OvertimePay'] = data['OvertimePay'].astype(bool)
data['OvertimePay'] = data['OvertimePay'].astype(int)
data.dtypes
data4 = data.groupby('JobTitle')['OvertimePay'].sum().sort_values(ascending=False).reset_index()
data4
# Result: Transit Operator

# Conclusion: Kelvin Lee is  the highest basically paid employee and Transit Operator is the best job