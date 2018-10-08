
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
# <<credenciais removidas>>

body = client_540ee8ee01ba4bce9e7f486fce77ee01.get_object(Bucket='irisexample-donotdelete-pr-td2giiumxpocf1',Key='iris.csv')['Body']
# add missing __iter__ method, so pandas accepts body as file-like object
if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )

df = pd.read_csv(body)


# In[2]:


df.head()


# In[3]:


df.describe()


# In[4]:


df.dtypes


# In[5]:


df['Species'].head()


# In[6]:


df['Species'] = df['Species'].astype('category')


# In[7]:


df.dtypes


# In[8]:


df.head()


# In[9]:


pd.isna(df).sum()


# In[11]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
colors = {'setosa':'red', 'versicolor':'blue', 'virginica':'green'} 
ax.scatter(df['Sepal.Length'], df['Sepal.Width'], color= df['Species'].apply(lambda x: colors[x]))
ax.set_xlabel(r'Sepal.Length', fontsize=10)
ax.set_ylabel(r'Sepal.Width', fontsize=10)
ax.set_title('Iris', fontsize=15)
ax.grid(True)
fig.tight_layout()
plt.show()


# In[14]:


fig, ax = plt.subplots()
colors = {'setosa':'red', 'versicolor':'blue', 'virginica':'green'} 
ax.scatter(df['Petal.Length'], df['Petal.Width'], color= df['Species'].apply(lambda x: colors[x]))
ax.set_xlabel(r'Sepal.Length', fontsize=10)
ax.set_ylabel(r'Sepal.Width', fontsize=10)
ax.set_title('Iris', fontsize=15)
ax.grid(True)
fig.tight_layout()
plt.show()

