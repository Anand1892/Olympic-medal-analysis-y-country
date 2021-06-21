#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #data processing and I/O operations
import numpy as np #Linear Algebra
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly


# In[2]:


winter = pd.read_csv('C://Users//deep//Desktop//Decodr//Case Studies_ Practice Files_ Reference Materials//Case Studies//Additional Solved Projects//In-depth Analysis of Olympic Dataset//winter.csv')
winter.head(10)


# In[3]:


winter.tail(10)


# In[4]:


summer = pd.read_csv("C://Users//deep//Desktop//Decodr//Case Studies_ Practice Files_ Reference Materials//Case Studies//Additional Solved Projects//In-depth Analysis of Olympic Dataset//summer.csv")
summer.head()


# In[5]:


summer.tail()


# In[6]:


summer.rename(columns={'Country' : 'Code'}, inplace=True)


# In[7]:


summer.head()


# In[12]:


dict = pd.read_csv('C://Users//deep//Desktop//Decodr//Case Studies_ Practice Files_ Reference Materials//Case Studies//Additional Solved Projects//In-depth Analysis of Olympic Dataset//dictionary.csv')
dict.head()


# In[13]:


summer=pd.merge(summer, dict, on="Code",how="outer" )


# In[14]:


summer.head()


# In[15]:


summer.describe()


# In[16]:


summer.describe(include=['O'])


# In[17]:


medals_map = summer.groupby(['Country', 'Code'])['Medal'].count().reset_index()
medals_map = medals_map[medals_map['Medal']>0]


# In[18]:


fig = px.choropleth(medals_map, locations="Code", color='Medal', hover_name='Country',
                   color_continuous_scale=px.colors.sequential.Plasma)

fig.show()


# In[ ]:




