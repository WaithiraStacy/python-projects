# Columns and responding variables
#cp: Chest pain
#tresbps: resting blood pressure
#chol: serum cholestrol
#fbs: fasting blood pressure
#restecg: resting electocardiographic results
#thalach: maximum heart rate achieved
#extang: exercise induced agina
#ca: number of major vessels colored by flourscopy

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('heart.csv')
data.head()
data.tail()
data.shape
print('Number of Rows',data.shape[0])
print('Number of Columns',data.shape[1])
data.info()
data.isnull().sum()
dup_data = data.duplicated().sum()
dup_data
data = data.drop_duplicates()
data.shape
data.describe()
# Classify numerical and categorical data
categorical_values = []
numerical_values = []

for column in data.columns:
    if data[column].nunique() <10:
        categorical_values.append(column)
    else:
        numerical_values.append(column)
        
categorical_values
numerical_values

#Distribution Analysis of numerical data
#age
sns.set(style="whitegrid")
sns.displot(data['age'], kde=True, rug=True, color='purple')
plt.title('Distribution of Age',fontsize=20, fontweight='semibold')
plt.xlabel('Age', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.show()

#2 Distribution of resting blood pressure
sns.set(style="whitegrid")
sns.displot(data['trestbps'], kde=True, rug=True, color='green')
plt.title('Distribution of Resting Blood Pressure', fontsize=20, fontweight='semibold')
plt.xlabel('trestbps', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.show()

#3 Distributrion of serum cholesterol
sns.set(style="whitegrid")
sns.displot(data['chol'], kde=True, rug=True, color='brown')
plt.title('Distribution of Serum Cholesterol', fontsize=20, fontweight='semibold')
plt.xlabel('chol', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.show()

#4 Distribution of maximum heart rate achieved
sns.set(style='whitegrid')
sns.displot(data['thalach'], kde=True, rug=True, color='red')
plt.title("Distribution of Maximum Heart Rate Achieved", fontsize=20, fontweight='semibold')
plt.xlabel("thalach", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.show()

#5 Distribution of oldpeak
sns.set(style='whitegrid')
sns.displot(data['oldpeak'], kde=True, rug=True, color='maroon', bins=30)
plt.title("Distribution of Oldpeak", fontsize=16, fontweight='semibold')
plt.xlabel("oldpeak", fontsize=15)
plt.ylabel("Frequency",fontsize=15)
plt.show()

# Distribution analysis for categorical data
for column in categorical_values:
    value_counts = data[column].value_counts()
    print(f"Values and Counts for {column}:\n{value_counts}\n{'-'*50}\n")
    
# Renaming of Categorical values
#sex column:  1:'M'(Male),0:'F'(Female),
#Target column(Heart disease): 1:'Y'(Yes),0:'N(No)',
#Fasting blood sugar(fbs): 1:'Y'(Yes),0:'N(No)'
#Exercise induced agina(extang): 1:'Y'(Yes),0:'N'(No)

data['sex'] = data['sex'].replace({1:'M',0:'F'})
data['target'] = data['target'].replace({1:'Y',0:'N'})
data['fbs'] = data['fbs'].replace({1:'Y',0:'N'})
data['exang'] = data['exang'].replace({1:'Y',0:'N'})

converted_data = ['sex', 'target', 'fbs', 'exang']
for column in converted_data:
    valuecount = data[column].value_counts()
    print(f"The Value and Count of {column}\n{valuecount}\n{'-'*50}")
    
categorical_values

#6 Distribution of sex
colors = ['brown','yellow']
plt.pie(data['sex'].value_counts(), labels=data['sex'].unique(), autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Distribution of Sex', fontweight='semibold')
plt.show()

#7 Distribution of target
colors = ['purple','pink']
plt.pie(data['target'].value_counts(), labels=data['target'].unique(), autopct='%1.1f%%', startangle=90, colors=colors)
plt.title("Distribution of target", fontweight='semibold')
plt.show()

#8 Distribution of Fasting Blood Sugar
colors=['grey','orange']
plt.pie(data['fbs'].value_counts(), labels=data['fbs'].unique(), colors=colors, startangle=90, autopct="%1.1f%%")
plt.title("Distribution of Fasting Blood Sugar", fontweight='semibold')
plt.show()

#9 Distribution of Exercise Induced Angina
colors = ['green','blue']
plt.pie(data['exang'].value_counts(), labels=data['exang'].unique(), autopct="%1.1f%%", startangle=90, colors=colors)
plt.title("Distribution of Exercise Induced Angina", fontweight='semibold')
plt.show()

#10 Distribution of Chest Pain
sns.set(style="whitegrid")
sns.countplot(x='cp', data=data, palette=colors)
plt.title("Distribution of Chest Pain", fontsize=20, fontweight='semibold')
plt.xlabel("Chest Pain Types")
plt.ylabel("Count")
plt.show()

#11 Distribution of Resting Electrocardiographic
sns.set(style="whitegrid")
colors = ['purple', 'pink', 'red']
sns.countplot(x='restecg', data=data, palette=colors)
plt.title("Distribution of Resting Electrocardiographic", fontsize=20, fontweight='semibold')
plt.xlabel("Resting Electrocardiographic types")
plt.show()

#12 Distribution of Slope
sns.set(style='whitegrid')
colors = ['green','blue','grey']
sns.countplot(x='slope', data=data,palette=colors)
plt.title("Distribution of Slope", fontsize=20, fontweight='semibold')
plt.xlabel("Slope types")
plt.show()

#12 Distribution of Number of Major Vessels
sns.set(style='whitegrid')
colors = ['brown','yellow','green']
sns.countplot(x='ca', data=data,palette=colors)
plt.title("Distribution of Number of Major Vessels", fontsize=20, fontweight='semibold')
plt.xlabel("Number of Major Vessels")
plt.show()

#13 Distribution of Thal
sns.set(style='whitegrid')
colors = ['blue','black','orange']
sns.countplot(x='thal', data=data,palette=colors)
plt.title("Distribution of Thal", fontsize=20, fontweight='semibold')
plt.xlabel("thal types")
plt.show()

# Distribution of Numerical varibales across different categories
numerical_values
categorical_values

# Age vs. Categorical Values
sns.set(style='whitegrid')
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(16, 12))

# Flatten the axes array for easy iteration
axes = axes.flatten()

for i, cat_value in enumerate(categorical_values):
    sns.boxplot(x=cat_value, y='age', data=data, ax=axes[i])
    axes[i].set_title(f'Age vs. {cat_value}')

plt.suptitle("Boxplot of Age vs. Categorical Values", fontweight='semibold')
plt.tight_layout()
plt.show()

# trestbps vs. Categorical Values
sns.set(style='whitegrid')
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(16,12))

axes = axes.flatten()

for i, cat_value in enumerate(categorical_values):
    sns.barplot(x=cat_value, y='trestbps', data=data, ax=axes[i])
    axes[i].set_title(f"trestbps vs. {cat_value}")

plt.suptitle("BarPlot of trestbps vs. categorical values", fontweight='semibold')
plt.tight_layout()
plt.show()

# chol vs. Categorical Value
sns.set(style="whitegrid")
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(16,12))

axes = axes.flatten()

for i, cat_value in enumerate(categorical_values):
    sns.violinplot(x=cat_value, y='chol', data=data, ax=axes[i])
    axes[i].set_title(f"chol vs. {cat_value}")
    
plt.suptitle("Violin Plot of chol vs. Categorical Values", fontweight='semibold')
plt.tight_layout()
plt.show()

# thalach vs. Categorical values
sns.set(style="whitegrid")
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(16,12))

axes = axes.flatten()

for i, cat_value in enumerate(categorical_values):
    sns.pointplot(x=cat_value, y='thalach', data=data, ax=axes[i])
    axes[i].set_title(f"thalach vs. {cat_value}")
    
plt.suptitle("Point Plot of thalach vs. Categorical Values", fontweight='semibold')
plt.tight_layout()
plt.show()

# oldpeak vs. categorical value
sns.set(style='whitegrid')
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(16,12))
axes = axes.flatten()

for i, cat_value in enumerate(categorical_values):
    sns.stripplot(x=cat_value, y='oldpeak', data=data, jitter=True, ax=axes[i])
    axes[i].set_title(f"oldpeak vs. {cat_value}")
    
plt.suptitle("Strip Plot of oldpeak vs. Categorical values", fontweight='semibold')
plt.tight_layout()
plt.show()

# Relationship between Categorical values and Heart disease(Target)
numerical_values
categorical_values
new_categorical = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
new_categorical

# target vs. Categorical Values
sns.set(style="whitegrid")
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(12,16))
axes = axes.flatten()

for i, cat in enumerate(new_categorical):
    sns.countplot(x=cat, hue='target', data=data, ax=axes[i], palette='cividis')
    axes[i].set_title(f"Target vs. {cat}")
    
plt.suptitle("Count Plot of target vs. Categorical Values", fontweight='semibold')
plt.tight_layout()
plt.show()

# Visualize relationship between numerical variables
data = pd.read_csv('heart.csv')
data
data.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.suptitle("Correlation Heatmap of Dataset", fontsize=20, fontweight='semibold')
plt.tight_layout()
plt.show()

# Age vs. Cholesterol with Target
red_shade = "#FF0000"
green_shade = "#00FF00"
sns.set(style='whitegrid')
fig, (ax0,ax1) = plt.subplots(nrows=2, ncols=1, figsize=(15,12))

sns.scatterplot(x='age', y='chol', hue='target', data=data, ax=ax0, palette=[green_shade,red_shade])
ax0.axhline(y=219, linestyle='--', color='red', label='Cholesterol Threshold: 219')
ax0.legend()
ax0.set_title('Scatter Plot of Age vs Cholesterol with Target', fontweight='semibold')

sns.barplot(x='age', y='chol', hue='target', data=data, ax=ax1, palette=[green_shade,red_shade])
ax1.axhline(y=219, linestyle='--', color='red', label='Cholesterol Threshold: 219')
ax1.legend()
ax1.set_title('Bar Plot of Age vs Cholesterol with Target', fontweight='semibold')

plt.tight_layout()
plt.show()