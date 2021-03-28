#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pyttsx3')
print('Library installed')


# In[4]:


import pyttsx3
print('Function imported')


# In[8]:


#Human input the variable
name = input("What's your name? ")


# In[10]:


engine = pyttsx3.init()
engine.say(f"hello, {name}, how are you?")
engine.runAndWait()


# In[ ]:




