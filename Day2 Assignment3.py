#!/usr/bin/env python
# coding: utf-8

# In[1]:


thisdict = {"brand": "Ford","model": "Mustang", "year": 1964,"year": 2020}
thisdict


# In[2]:


len(thisdict)


# In[3]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
type(thisdict)


# In[4]:


thisdict = {"brand": "Ford","model": "Mustang", "year": 1964}
thisdict.pop("model")
thisdict


# In[5]:


thisdict = { "brand": "BMW", "model": "Mustang", "year": 1970}
mydict = thisdict.copy()
mydict


# In[6]:


car = {"brand": "Ford","model": "Mustang","year": 1964}

x = car.items()

x


# In[7]:


car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.items()

car["year"] = 2018

x


# In[ ]:




