#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import pandas
import glob


# You can save your functions (e.g. print_hello) in a text file ending in .py (e.g. utils.py) and import the function (e.g. from utils import print_hello)

# Writing an in-code comment in 3 x double quotes inludes it in the documentation for the created function

# In[5]:


def print_hello():
    """This function provides me a hello"""
    print("hello")


# In[6]:


print_hello()


# In[19]:


def print_date(year, month, day):
    assert month <= 12
    assert day <= 31 # months have a maximum of 31 days 
    print(year, month, day)


# In[17]:


print_date(2000, 11, 25)


# TIP: it is good pratice not to use spaces before or after an equal (=) sign

# In[18]:


print_date(month=11, year=1970, day=25)


# In[35]:


def return_combined_date(year, month, day):
    """Returns a date string in ISO8601 (yyy-mm-dd) format
    
    https://nl.wikipedia.org/wiki/ISO_8601
    
    Parameters
    ----------
    year: int
        the year of interest
    month: int
        the month of interest (! between 1 and 12)
    day: int
        the day of interest (! between 1 and 31)
    """
    assert month <= 12
    assert month >0
    assert day <= 31
    assert day >0
    return str(year) + '-' + str(month)  + '-' + str(day)


# In[36]:


return_combined_date(2018, 10, 24)


# In[57]:


def min_in_data(filename, column_name='gdpPercap_1977'):
    """Provide country and value with minimal value
    
    Parameters
    ----------
    
    
    """
    data = pandas.read_csv(filename, index_col="country")
    min_data = data[column_name].min()
    min_country = data[column_name].idxmin()
    return min_data, min_country


# In[58]:


min_in_data(filename='../data/gapminder_all.csv', column_name="gdpPercap_1972")


# In[59]:


min_in_data(filename='../data/gapminder_all.csv')


# Store two outputs at the same time in two different objects

# In[60]:


value, country = min_in_data("../data/gapminder_gdp_europe.csv", "gdpPercap_1972")


# In[61]:


value


# In[62]:


country


# In[ ]:




