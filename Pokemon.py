#!/usr/bin/env python
# coding: utf-8

# #### In this project, we'll use a dataset from Kaggle that contains information about Pokemon.
# 
# #### Link to dataset: https://www.kaggle.com/rounakbanik/pokemon
# 
# ### Step 1: Defining the Problem
# 
# #### Our goal is to analyze the Pokemon dataset and gain insights into the characteristics of different types of Pokemon. Specifically, we want to answer the following questions:
# 
# #### 1- Which type of Pokemon is the strongest based on their overall stats?
# #### 2- How does the distribution of different Pokemon types compare?
# #### 3- What is the correlation between the different Pokemon stats?
# #### 4- What is the most common primary and secondary type combination?
# #### 5- Which Pokemon has the highest and lowest total stats?
# #### 6- How does the 'Total' stat vary for each Pokemon type?
# #### 7- Which Pokemon has the highest and lowest speed?
# #### 8- How does the 'Speed' stat vary for each Pokemon type?
# #### 9- Is there a correlation between the 'Legendary' status of a Pokemon and its 'Total' stats?
# 
# 
# ### Step 2: Loading the Dataset
# 
# 
# #### Let's start by loading the Pokemon dataset into a Pandas DataFrame:
# #### I created a new column as Total equal sum of attack, defense and speed.

# In[24]:


import pandas as pd

df = pd.read_csv(r'C:\Users\Baazz\Downloads\pokemon.csv')


# ### Step 3: Exploratory Data Analysis
# 
# #### Before we start answering our questions, let's take a look at the dataset and perform some exploratory data analysis to gain insights and identify any issues or missing data. Here are some questions we can ask:
# 

# #### 1. How many rows and columns does the dataset have?
# 

# In[25]:


print('Shape of dataset:', df.shape)


# #### 2. What are the data types of each column?

# In[26]:


print('Data types of columns:')
print(df.dtypes)


# #### 3. Are there any missing values in the dataset?

# In[27]:


print('Missing values in dataset:')
print(df.isnull().sum())


# #### 4. What are the unique values in each column?

# In[28]:


print('Unique values in each column:')
for col in df.columns:
    print(col, df[col].nunique())


# #### 5. What are the summary statistics for each column?

# In[29]:


print('Summary statistics for each column:')
print(df.describe())


# ### Step 4: Answering the Questions
# 
# #### Now that we have a better understanding of the dataset, let's start answering our questions:
# 
# #### 1- Which type of Pokemon is the strongest based on their overall stats?
# 
# #### To answer this question, we'll create a new column in our DataFrame called 'Total', which is the sum of all the Pokemon's stats. Then, we'll group the DataFrame by the 'Type 1' column and find the mean 'Total' value for each type. Finally, we'll sort the values in descending order to find the strongest type.

# In[30]:


df['Total'] = df.iloc[:, 4:10].sum(axis=1)
type_totals = df.groupby('type1')['Total'].mean()
strongest_type = type_totals.sort_values(ascending=False).index[0]

print('The strongest type of Pokemon is', strongest_type)


# #### 2- How does the distribution of different Pokemon types compare?
# 
# #### To answer this question, we can create a bar chart that shows the count of each Pokemon type in the dataset.

# In[31]:


import matplotlib.pyplot as plt

type_counts = df['type1'].value_counts()
plt.bar(type_counts.index, type_counts.values)
plt.xticks(rotation=90)
plt.xlabel('Type')
plt.ylabel('Count')
plt.title('Distribution of Pokemon Types')
plt.show()


# #### The output of this code shows us a bar chart that visualizes the distribution of Pokemon types in the dataset.

# #### 3- What is the correlation between the different Pokemon stats?
# 
# #### To answer this question, we can create a correlation matrix that shows the correlation between each pair of stats.

# In[32]:


import seaborn as sns

corr_matrix = df.iloc[:, 4:10].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix for Pokemon Stats')
plt.show()


# #### The output of this code shows us a heatmap that visualizes the correlation matrix.

# #### 4- What is the most common primary and secondary type combination?
# 
# #### To answer this question, we can create a new column in our DataFrame called 'Type Combination', which combines the 'Type 1' and 'Type 2' columns. Then, we can count the number of Pokemon for each type combination and find the most common one.

# In[33]:


df['Type Combination'] = df['type1'] + '-' + df['type2'].fillna('')
type_comb_counts = df['Type Combination'].value_counts()
most_common_comb = type_comb_counts.index[0]

print('The most common primary and secondary type combination is', most_common_comb)


# #### 5- Which Pokemon has the highest and lowest total stats?
# 
# #### To answer this question, we can find the Pokemon with the highest and lowest 'Total' values in our DataFrame.

# In[35]:


highest_total_pokemon = df.loc[df['Total'].idxmax(), 'name']
lowest_total_pokemon = df.loc[df['Total'].idxmin(), 'name']

print('The Pokemon with the highest total stats is', highest_total_pokemon)
print('The Pokemon with the lowest total stats is', lowest_total_pokemon)


# #### 6- How does the 'Total' stat vary for each Pokemon type?
# 
# #### To answer this question, we can create a box plot that shows the distribution of 'Total' values for each Pokemon type.

# In[36]:


sns.boxplot(x='type1', y='Total', data=df)
plt.xticks(rotation=90)
plt.title('Distribution of Total Stats for Each Pokemon Type')
plt.show()


# #### The output of this code shows us a box plot that visualizes the distribution of 'Total' values for each Pokemon type.
# 
# #### These additional analyses help us gain a deeper understanding of the Pokemon dataset and the characteristics of different Pokemon.

# #### 7- Which Pokemon has the highest and lowest speed?
# 
# #### To answer this question, we can find the Pokemon with the highest and lowest 'Speed' values in our DataFrame.

# In[37]:


highest_speed_pokemon = df.loc[df['speed'].idxmax(), 'name']
lowest_speed_pokemon = df.loc[df['speed'].idxmin(), 'name']

print('The Pokemon with the highest speed is', highest_speed_pokemon)
print('The Pokemon with the lowest speed is', lowest_speed_pokemon)


# #### 8- How does the 'Speed' stat vary for each Pokemon type?
# 
# #### To answer this question, we can create a box plot that shows the distribution of 'Speed' values for each Pokemon type.

# In[38]:


sns.boxplot(x='type1', y='speed', data=df)
plt.xticks(rotation=90)
plt.title('Distribution of Speed Stats for Each Pokemon Type')
plt.show()


# #### The output of this code shows us a box plot that visualizes the distribution of 'speed' values for each Pokemon type.

# #### 9- Is there a correlation between the 'Legendary' status of a Pokemon and its 'Total' stats?
# 
# #### To answer this question, we can create a scatter plot that shows the relationship between the 'Legendary' and 'Total' columns.

# In[39]:


sns.scatterplot(x='is_legendary', y='Total', data=df)
plt.title('Relationship Between Legendary Status and Total Stats')
plt.show()


# #### The output of this code shows us a scatter plot that visualizes the relationship between the 'Legendary' and 'Total' columns.

# ### Step 5: Insights:
# 
# #### 1. The most common primary type among Pokemon is Water, followed by Normal and Grass.
# #### 2.The most common secondary type among Pokemon is Flying, followed by Ground and Poison.
# #### 3.The most common primary and secondary type combination is Water-.
# #### 4.The Pokemon with the highest total stats is Arceus, while the Pokemon with the lowest total stats is Sunkern.
# #### 5.The Pokemon with the highest speed is Deoxys Speed Forme, while the Pokemon with the lowest speed is Shuckle.
# #### 6.Legendary Pokemon tend to have higher total stats compared to non-legendary Pokemon.
# #### 7.The distribution of total stats varies for each Pokemon type, with some types having a wider range of total stats than others.
# #### 8.The distribution of speed stats also varies for each Pokemon type, with some types having a wider range of speed stats than others.

# In[ ]:




