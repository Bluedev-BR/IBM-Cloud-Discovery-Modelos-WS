
# coding: utf-8

# In[2]:


import sys
import types
import pandas as pd
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0

# @hidden_cell

df = pd.read_csv(body)
df.head()


# In[56]:


df = df.loc[:,['bairro','preco','area','suites','dormitorios','banheiros','vagas']]


# In[57]:


df.dtypes


# In[58]:


df['bairro'] = df['bairro'].astype('category')


# In[59]:


df.describe()


# In[60]:


df[df.preco == 0]


# In[61]:


df = df[df.preco > 0]


# In[62]:


df.shape


# In[63]:


df.preco.describe()


# In[64]:


pd.isna(df.preco).sum()


# In[65]:


pd.isna(df.area).sum()


# In[66]:


df = df.dropna()


# In[67]:


df.shape


# In[68]:


pd.isna(df).sum()


# In[69]:


df.describe()


# In[70]:


import matplotlib.pyplot as plt
plt.hist(df.area)


# In[71]:


min(df.area)


# In[72]:


df.area.describe()


# In[73]:


df = df[df.area > 84]


# In[74]:


df = df[df.area < 196]


# In[75]:


df.shape


# In[76]:


plt.hist(df.area)


# In[77]:


plt.hist(df.suites)


# In[78]:


plt.hist(df.dormitorios)


# In[79]:


df.describe()


# In[80]:


df = df[df.dormitorios < 10]


# In[81]:


df.describe()


# In[82]:


df =df[df.banheiros < 10]


# In[83]:


df.describe()


# In[84]:


df = df[df.vagas < 34]


# In[85]:


df.describe()


# In[1]:


# @hidden_cell
# The project token is an authorization token that is used to access project resources like data sources, connections, and used by platform APIs.

# In[3]:


project.save_data("imoveis-tratados3.csv", df.to_csv())

