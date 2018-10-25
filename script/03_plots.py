#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas #import library needed to read in csv files


# In[4]:


anz = pandas.read_csv("../data/gapminder_gdp_oceania.csv", index_col = "country")
europe = pandas.read_csv("../data/gapminder_gdp_europe.csv", index_col = "country")


# In[5]:


get_ipython().run_line_magic('who', '')


# Import plotting library and assure that plotting occurs in the same chunck

# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 


# Add a plot of transformed data

# In[33]:


anz.T.plot()


# In[29]:


europe.T.plot()


# In[13]:


anz.columns


# In[14]:


europe.columns


# Format column names to only the numbers by stripping off the preceding string

# In[59]:


years = anz.columns.str.strip('gdpPercap_')
anz.columns = years
europe.columns = years


# In[77]:


anz.T.plot()
plt.ylabel("GDP per Capita")
plt.style.use("seaborn")


# In[34]:


plt.style.available


# In[69]:


plt.style.use('default')
europe.plot(kind = 'box')


# In[72]:


gdp_i = europe.loc[('Italy', 'Ireland', 'Iceland'),]


# In[75]:


gdp_i


# In[88]:


plt.plot(years, gdp_i.iloc[0], 'g--', label = 'Italy')
plt.plot(years, gdp_i.iloc[1], 'b--', label = 'Ireland')
plt.plot(years, gdp_i.iloc[2], 'r-', label = 'Iceland')
plt.legend(loc = "best")
plt.xlabel('Years')
plt.ylabel('GDP per Capita')
plt.title('GDP per Capita in European countries starting with I')

plt.savefig('../plots/GDP_i_countries.png')


# In[ ]:





# In[ ]:




