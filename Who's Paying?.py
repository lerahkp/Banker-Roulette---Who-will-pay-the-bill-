#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
num_people = len(names)
print(num_people)
bill_payee = random.randint(0,num_people)
print(bill_payee)
print(f"{names[bill_payee-1]} is going to buy the meal today")


# In[ ]:





# In[ ]:




