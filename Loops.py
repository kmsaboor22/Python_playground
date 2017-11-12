
# coding: utf-8

# In[1]:

Foods = ['Bacon', 'Eggs', 'Tuna', 'Lemon Cake', 'Apples', 'Grapes']


# In[2]:

print(Foods[1])


# In[14]:

# for each item in foods
for i in Foods:
# print every item in the list and the length    
    print(i+',','The length of',i, 'is',len(i),'characters')


# In[15]:

#to loop through part/slice of the 
#List/array you would do the following

for i in Foods[:3]:
    print(i+',','The length of',i, 'is',len(i),'characters')


# In[ ]:



