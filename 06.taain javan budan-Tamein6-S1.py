#!/usr/bin/env python
# coding: utf-8

# In[5]:


sen1=int(input())
if sen1>0 and sen1<6:
    print('khordsal')
elif sen1>=6 and sen1<10:
    print('koodak')
elif sen1>=10 and sen1<14:
    print('nojavan')
elif sen1>=14 and sen1<24:
    print('javan')
elif sen1>=24 and sen1<40:
    print('bozorgsal')
else:
    print('miansal')

