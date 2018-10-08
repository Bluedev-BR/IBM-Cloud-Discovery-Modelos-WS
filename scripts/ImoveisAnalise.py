
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
# add missing __iter__ method, so pandas accepts body as file-like object
if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )

df = pd.read_csv(body)
df.head()


# In[2]:


df = df.loc[:,['bairro','preco','area','suites','dormitorios','banheiros','vagas']]


# In[3]:


df.dtypes


# In[4]:


df['bairro'] = df['bairro'].astype('category')


# In[5]:


df.describe()


# In[6]:


df[df.preco == 0]


# In[7]:


df = df[df.preco > 0]


# In[8]:


df.shape


# In[9]:


df.preco.describe()


# In[10]:


pd.isna(df.preco).sum()


# In[11]:


pd.isna(df.area).sum()


# In[12]:


df = df.dropna()


# In[13]:


df.shape


# In[14]:


pd.isna(df).sum()


# In[15]:


df.describe()


# In[16]:


import matplotlib.pyplot as plt
plt.hist(df.area)


# In[17]:


min(df.area)


# In[18]:


df.area.describe()


# In[19]:


df = df[df.area > 84]


# In[20]:


df = df[df.area < 196]


# In[21]:


df.shape


# In[22]:


plt.hist(df.area)


# In[23]:


plt.hist(df.suites)


# In[24]:


plt.hist(df.dormitorios)


# In[25]:


df.describe()


# In[26]:


df = df[df.dormitorios < 10]


# In[27]:


df.describe()


# In[28]:


df =df[df.banheiros < 10]


# In[29]:


df.describe()


# In[30]:


df = df[df.vagas < 34]


# In[31]:


df.describe()


# In[32]:


# @hidden_cell
# The project token is an authorization token that is used to access project resources like data sources, connections, and used by platform APIs.

# In[34]:


project.save_data("imoveis-tratados3.csv", df.to_csv(header=True, encoding='utf-8', index=False), overwrite=True)

