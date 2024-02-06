#!/usr/bin/env python
# coding: utf-8

# In[2]:


import joblib


# In[4]:


def predict(data):
    clf=joblib.load("reg.sav")
    return clf.prediction(data)


# In[ ]:




