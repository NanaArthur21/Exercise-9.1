#!/usr/bin/env python
# coding: utf-8

# In[1]:


fin = open('words.txt')


# In[2]:


for line in fin:
    word = line.strip()
    if len(word) > 20:
        print (word)


# In[4]:


for line in fin:
    word = line.strip()
    if len(word) > 10:
        print (word)


# In[5]:


fin = open('words.txt')


# In[6]:


for line in fin:
    word = line.strip()
    if len(word) > 10:
        print (word)


# In[ ]:




