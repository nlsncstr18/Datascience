#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
x = np.arange(0,100)
y = x*2
z=x**2


# In[4]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,z)


# In[6]:


fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_title("summary")
ax.set_xlabel("investment")
ax.set_ylabel("profit")
ax.plot(x,z)


# In[10]:


figl = plt.figure()
ax1=figl.add_axes([0,0,1,1])
ax2=figl.add_axes([0.2,0.5,0.2,0.2])


# In[11]:


figl = plt.figure()
ax1=figl.add_axes([0,0,1,1])
ax2=figl.add_axes([0.2,0.5,0.2,0.2])

ax1.plot(x,z)
ax2.plot(x,z)


# In[14]:


figl = plt.figure()
ax1=figl.add_axes([0,0,1,1])
ax2=figl.add_axes([0.2,0.5,0.2,0.2])

ax2.set_ylim(1000,4000)
ax2.set_xlim(40,60)

ax1.plot(x,z)
ax2.plot(x,z)


# In[18]:


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8,2))
axes[0].plot(x,y, color = "red",lw=5, ls= "-.")
axes[1].plot(x,z, color ="green", lw=3)


# In[30]:


import seaborn as sns
titanic = sns.load_dataset("titanic")
titanic


# In[20]:


sns.jointplot(x='fare',y='age',data=titanic)


# In[38]:


titanic[titanic['fare']>1]


# In[25]:


sns.distplot(titanic['fare'], kde = False,color = "red",bins=30)


# In[26]:


sns.distplot(titanic['fare'], kde = True,color = "red",bins=30)


# In[39]:


sns.boxplot(x="sex",y="age",data=titanic)


# In[28]:


sns.swarmplot(x="class",y="age",data=titanic)


# In[29]:


sns.countplot(x='sex',data=titanic)


# In[31]:


sns.heatmap(titanic.corr())


# In[32]:


g = sns.FacetGrid(titanic, col = 'sex')
g.map(plt.hist, 'age')


# In[ ]:




