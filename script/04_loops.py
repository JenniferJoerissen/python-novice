#!/usr/bin/env python
# coding: utf-8

# ### Import Libraries

# In[25]:


import pandas
import glob


# ### For loops

# Columnscontain only one type of data.
# Lists can contain mixed types of data

# In[1]:


my_list = [2, 3, 'a', [2,5]]


# Indentation matters in Python

# In[3]:


for item in my_list:
    print(item)


# In[4]:


filenames = ['../data/gapminder_gdp_europe.csv', '../data/gapminder_gdp_asia.csv']


# TIP: To get information about the function, hit Shift + Tab or Shift + Tab + Tab within the function

# Import the two data frames for which the path is stored in 'filenames'

# In[13]:


for filename in filenames:
    print(filename)
    data = pandas.read_csv(filename, index_col = 'country')
    print(data.head())


# In[14]:


data


# For in  range: the end of the range is not included

# In[15]:


for counter in range(1, 10):
    print(counter)


# In[19]:


colours = ['red', 'green', 'blue']


# In[20]:


total = 0
for word in colours:
    total += len(word)
print(total)


# In[24]:


length = []
for word in colours: 
    length.append(len(word))
print(length)


# In[27]:


glob.glob('../data/*')


# In[34]:


for filename in glob.glob('../data/*gdp*.csv'):
    print(filename)


# In[ ]:




