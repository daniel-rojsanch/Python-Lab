#!/usr/bin/env python
# coding: utf-8

# # 🐍 The Quick Python Books

# ### List
# ---

# In[55]:


## Una lista es asi
x = [1, 2, 5]
x


# In[7]:


x = [1, "Hola Maria", [1, 4, 5]]
x


# In[10]:


len(x) ## Retorna el numero de elemntos de una lista


# In[12]:


x = [3, 
     [3, 5, [5, 6, 7]],
     "Maria"]
len(x)


# In[20]:


x = ["diana","Maria","Brenda","Rubi"]
len(x)


# In[16]:


x[0]


# In[18]:


x[3]


# In[21]:


x[-1]


# In[24]:


x[-2]


# In[35]:


x[1:4]


# In[36]:


x[1:2]


# In[37]:


x[1:-1]


# In[38]:


x


# In[39]:


x


# In[40]:


x[1:]


# In[43]:


x[:3]


# In[44]:


x[3]


# In[45]:


x = [1, 2, 4]


# In[46]:


y = x


# In[47]:


y[0] = 10


# In[48]:


x


# In[49]:


y


# In[50]:


x


# In[51]:


y1 = x[:]


# In[52]:


y1[0] = 100


# In[53]:


y1


# In[54]:


x


# In[56]:


del x, y


# In[ ]:




