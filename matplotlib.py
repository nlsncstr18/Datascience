#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
x = np.arange(0, 100)
y = x*2
z = x**2


# In[10]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,z)


# In[17]:


fig1 = plt.figure()
ax1 = fig1.add_axes([0,0,1,1])
ax2 = fig1.add_axes([0.2,0.5,0.2,0.2])

ax2.set_ylim(1000,4000)
ax2.set_xlim(40,60)

ax1.plot(x,z)
ax2.plot(x,z)






# In[20]:


fig, axes = plt.subplots(nrows = 1, ncols =2, figsize = (8,2))
axes[0].plot(x,y, color = "red", lw =5, ls = "-.")
axes[1].plot(x,y, color = "green", lw = 3, ls = "-.")


# In[ ]:




