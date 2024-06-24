#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df= pd.read_csv("Deepawali Sales Data.csv")


# In[3]:


df.shape # To know number of rows and columns in data


# In[4]:


df.head()


# In[5]:


df.head(10)


# In[6]:


df.info()


# In[7]:


df.drop({'Status' , 'unnamed1'}, axis=1, inplace=True) # To delete Status and unnamed1 row because it has null value


# In[8]:


df.info()


# In[9]:


pd.isnull(df) # True means null and False means non-null


# In[10]:


pd.isnull(df).sum() # To sum all null value present in data


# In[11]:


df.shape # Give total number of rows and columns


# In[12]:


df.dropna(inplace=True) # To remove null values that we have found in [10]


# In[13]:


pd.isnull(df).sum() # Now we can see, Amount is Zero means null value has been deleted


# In[14]:


df['Amount'] = df['Amount'].astype('int') # To change the data type of Amount(float) to Amount(int) and for that astype is used.


# In[15]:


df['Amount'].dtypes


# In[16]:


df.columns # To check how many columns are there in data


# In[17]:


df.rename(columns = {'Marital_Status':'Shadi'}) # To rename the Marital_Status to Shadi. This change will not save in data
# because We have not place inplace = True after Curly bracket.


# In[18]:


df.describe() # describe() method returns description of data in dataFrame


# In[19]:


df[['Age', 'Orders', 'Amount']].describe() # Using describe() method for particular columns


# # Gender

# In[20]:


sns.countplot(x ='Gender', data=df) # To show Gender column in X-Y graph.This graph shows F have bought more in comparision to M


# In[21]:


ax = sns.countplot(x = 'Gender', data=df) 

for bars in ax.containers:  # To show numbers of F and M in above graph
    ax.bar_label(bars)     
    
# In a Seaborn (sns) plot using Matplotlib, ax.containers holds the collections of bar elements created by a bar plot. 
# The loop for bars in ax.containers: iterates over these collections. The function ax.bar_label(bars) then labels each bar in 
# the current collection with its height, adding numerical labels to the tops of the bars for clarity. 


# In[22]:


df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by='Amount', ascending=False)
# This code groups the data by 'Gender', calculates the total 'Amount' for each gender, and then sorts the results in 
# descending order of the total 'Amount'.


# In[23]:


sales_gen = df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Gender', y = 'Amount', data = sales_gen)
# From this graph, we can see that most of the expenditures are done by females.


# # Age

# In[24]:


df.columns


# In[25]:


sns.countplot(data = df, x = 'Age Group') 
# This graph is saying which age group has done more shopping


# In[26]:


sns.countplot(data = df, x = 'Age Group', hue = 'Gender')
# This graph is saying which age group has done more shopping on the basis of gender.


# In[27]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[28]:


df.groupby(['Age Group'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False)
# This code says, Which age group has invested how much amount of money.


# In[29]:


sales_age = df.groupby(['Age Group'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group', y = 'Amount', data = sales_age)
# This code says, Which age group has invested how much amount of money in graphical format.


# # State

# In[30]:


df.columns


# In[31]:


df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
# This code tells which state has done how many orders.


# In[32]:


sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)}) # This line of code sets the default figure size for all subsequent Seaborn plots to 15 by
# 5 inches, making them wider than the default size, which can be useful for better visibility and presentation of data.
sns.barplot(data = sales_state, x = 'State', y = 'Orders')
# This code tells which state has done how many orders in graphical format.


# In[33]:


df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
# This code tell, which state has invested how much amount.


# In[34]:


state_amount = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(18,5)}) # This line of code sets the default figure size for all subsequent Seaborn plots to 15 by
# 5 inches, making them wider than the default size, which can be useful for better visibility and presentation of data.
sns.barplot(data = state_amount, x = 'State', y = 'Amount')
# This code tells which state has invested how much amount of money in graphical format.


# # Marital Status

# In[35]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(4,5)})
for bars in ax.containers:
    ax.bar_label(bars)
# As we can see, married people have done more shopping.


# In[36]:


df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
# this code groups the data by both 'Marital_Status' and 'Gender', calculates the total '
# Amount' for each group, and then sorts the results in descending order of the total 'Amount'. 


# In[37]:


purchasing_Status = df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = purchasing_Status, x = 'Marital_Status', y= 'Amount', hue= 'Gender')
# this code groups the data in graphical form by both 'Marital_Status' and 'Gender', calculates the total '
# Amount' for each group, and then sorts the results in descending order of the total 'Amount'. 


# # Occupation

# In[38]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)
# this code sets a custom figure size, creates a count plot for the 'Occupation' column in the DataFrame df, 
# and adds numerical labels to each bar to indicate the count of each occupation.


# In[39]:


df.groupby(['Occupation'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False)
# This says Which sector has how much purchased(in Rs)


# In[40]:


purchase_By_Occupation= df.groupby(['Occupation'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = purchase_By_Occupation, x ='Occupation', y='Amount')
# This says Which sector has how much purchased(in Rs) in graphical form


# # Product Category

# In[46]:


df.groupby(['Product_Category'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False)
# This says, on which product, Expenditure is more.


# In[49]:


purchase_By_Product=df.groupby(['Product_Category'], as_index=False) ['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = purchase_By_Product, x ='Product_Category', y='Amount')
# This says, on which product, Expenditure is more in graph.


# In[50]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)
    
# This says, Which product has been sold most.


# In[51]:


df.groupby(['Product_ID'], as_index=False) ['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
# This says , which product ID is sold how many times.


# In[52]:


purchase_By_ProductID=df.groupby(['Product_ID'], as_index=False) ['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = purchase_By_ProductID, x ='Product_ID', y='Orders')
# This says , which product ID is sold how many times in graph.


# In[ ]:




