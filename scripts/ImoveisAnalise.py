
# coding: utf-8

# In[1]:


import sys
import types
import pandas as pd
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0

# @hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. It includes your credentials.
# You might want to remove those credentials before you share your notebook.

<<falta codigo aqui - com credenciais>>

df = pd.read_csv(body)
df.head()


# In[3]:


df = df.loc[:,['bairro','preco','area','suites','dormitorios','banheiros','vagas']]


# In[5]:


df.dtypes


# In[6]:


df['bairro'] = df['bairro'].astype('category')


# In[7]:


df.describe()


# In[9]:


df[df.preco == 0]


# In[10]:


df = df[df.preco > 0]


# In[11]:


df.shape


# In[12]:


df.preco.describe()


# In[14]:


pd.isna(df.preco).sum()


# In[15]:


pd.isna(df.area).sum()


# In[26]:


df = df.dropna()


# In[27]:


df.shape


# In[28]:


pd.isna(df).sum()


# In[29]:


df.describe()


# In[37]:


import matplotlib.pyplot as plt
plt.hist(df.area)


# In[34]:


min(df.area)


# In[36]:


df.area.describe()


# In[38]:


df = df[df.area > 84]


# In[39]:


df = df[df.area < 196]


# In[40]:


df.shape


# In[41]:


plt.hist(df.area)


# In[42]:


plt.hist(df.suites)


# In[43]:


plt.hist(df.dormitorios)


# In[45]:


df.describe()


# In[46]:


df = df[df.dormitorios < 10]


# In[47]:


df.describe()


# In[48]:


df =df[df.banheiros < 10]


# In[49]:


df.describe()


# In[50]:


df = df[df.vagas < 34]


# In[52]:


df.describe()


# In[53]:


df.to_csv('imoveis_tratados.csv', encoding='utf-8')

