#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. What does an empty dictionary's code look like?

#Two curly brackets: {}


# In[ ]:


#2. What is the value of a dictionary value with the key 'foo' and the value 42?
#{'foo': 42}


# In[ ]:


#3. What is the most significant distinction between a dictionary and a list?
#The items stored in a dictionary are unordered, while the items in a list are ordered.


# In[1]:


#4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
spam = {'bar': 100}
spam['foo']


# In[ ]:


#4 You get a KeyError error


# In[ ]:


#5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
#There is no difference. The in operator checks whether a value exists as a key in the dictionary.


# In[ ]:


#6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
#'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.


# In[ ]:


#7. What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'

# spam.setdefault('color', 'black')


# In[ ]:


#8. How do you "pretty print" dictionary values using which module and function?
# pprint.print()
#Use pprint() to Pretty Print a Dictionary in Python
#Within the pprint module there is a function with the same name pprint() , which is the function used to pretty-print the given string or object.

