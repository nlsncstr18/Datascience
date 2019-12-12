#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dataset = pd.read_csv("C:\ProgramData\Anaconda3\wine-dataset.csv")
print("Dataset:{}".format(dataset.shape))
print("Columns:{}".format(dataset.columns))
dataset.head(5)


# In[2]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import seaborn as sns 
dataset


# In[4]:


dataset[dataset['points']>80]


# In[9]:


sns.distplot(dataset['points'],kde=False,color="red",bins=50)


# In[10]:


sns.countplot(x='variety',data=dataset)


# In[11]:


sns.heatmap(dataset.corr())


# In[ ]:




