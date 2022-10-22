#!/usr/bin/env python
# coding: utf-8

# In[19]:


addad=int(input())
barax=(str(addad%10) + str((addad//10)%10) + str(addad//100))
print(int(barax)*2)

