#!/usr/bin/env python
# coding: utf-8

# # Our first notebook

# Here we are learning Python Variables and some useful methods

# ## Variables

# In[1]:


mycal = 2+2
mycal


# Python is zero based

# In[2]:


mystr = "Hello"
mystr[1]


# In[3]:


mystr[2:]


# In[4]:


mydiv = 37/3
mydiv


# ## types

# In[5]:


type(mycal)


# In[6]:


type(mystr)


# In[7]:


type(mydiv)


# In[8]:


hyphen = "this works"


# ## Libraries

# In[9]:


import pandas #library for data manipulation


# In[10]:


get_ipython().run_line_magic('who', '')


# In[11]:


help()


# In[12]:


get_ipython().run_line_magic('who', '')


# ## Reading table format files using pandas

# In[61]:


anz = pandas.read_csv("../data/gapminder_gdp_oceania.csv", index_col = "country")
africa = pandas.read_csv("../data/gapminder_gdp_africa.csv", index_col = "country")
europe = pandas.read_csv("../data/gapminder_gdp_europe.csv", index_col = "country")
asia = pandas.read_csv("../data/gapminder_gdp_asia.csv", index_col = "country")
america = pandas.read_csv("../data/gapminder_gdp_americas.csv", index_col = "country")


# In[ ]:





# In[ ]:





# In[22]:


anz


# In[23]:


africa


# In[24]:


europe


# In[26]:


asia


# In[29]:


asia.columns


# In[30]:


asia.index


# In[31]:


asia.axes


# In[32]:


asia.dtypes


# In[34]:


asia.shape


# In[36]:


asia.size


# In[38]:


asia.values


# In[40]:


asia.T


# In[46]:


del mydiv


# In[50]:


africa.info() #summarise information about the data


# In[52]:


africa.describe() #summary statistics per numeriacals (boxplot values)


# In[55]:


africa.gdpPercap_1952 #Select specific column


# In[56]:


africa.gdpPercap_1952.describe() #summary statistics of specific columsn


# In[54]:


africa.head(n = 3) #First 3 rows


# In[57]:


africa.tail() #last 5 rows


# In[63]:


help(america.head)


# In[64]:


america


# In[66]:


america.head(n = 3)


# In[81]:


america.T.tail(n = 3)


# In[71]:


america.describe()


# In[74]:


processed = america.T.tail(n = 3).T


# In[75]:


processed


# In[76]:


processed.columns.format()


# In[77]:


america.Peru


# In[78]:


america


# In[83]:


america.T.Peru.T


# In[84]:


america.iloc #subset part of the dataframe using index
america.loc #subset part of the dataframe by name
favourite_country = america.loc["Peru"]


# In[85]:


favourite_country


# In[87]:


europe.gdpPercap_2007.T.Greece


# In[104]:


iceland = europe.loc["Iceland"]
iceland.gdpPercap_1952


# In[117]:


europe.loc[["Greece", "Iceland"], ["gdpPercap_1997", "gdpPercap_2007"]]


# In[120]:


europe


# ## Save Files

# In[131]:


processed.to_excel("../results/processed.xlsx")


# In[124]:


processed


# ## Plots

# In[125]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[126]:


import matplotlib.pyplot as plt


# In[127]:


anz.plot()


# In[ ]:




