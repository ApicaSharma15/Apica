#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. What exactly is []?
#The empty list value, which is a list value that contains no items. This is similar to how '' is the empty string value.


# In[ ]:


#2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
##Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

##spam[2] = 'hello' (Notice that the third value in a list is at index 2 because the first index is 0.)


# In[3]:


#3. What is the value of spam[int(int('3' * 2) / 11)]?
spam = ['a', 'b', 'c', 'd']
spam[int(int('3' * 2) / 11)]


# In[ ]:


#3 'd' (Note that '3' * 2 is the string '33', which is passed to int() before being divided by 11. This eventually evaluates to 3. Expressions can be used wherever values are used.)


# In[4]:


#4. What is the value of spam[-1]?
spam[-1]


# #4 'd' (Negative indexes count from the end.)

# In[5]:


#5. What is the value of spam[:2]?
##Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
spam[:2]


# In[ ]:


#5 ['a', 'b']


# In[7]:


#6. What is the value of bacon.index('cat')?
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.index('cat')


# In[ ]:


#6 1 


# In[30]:


#7. How does bacon.append(99) change the look of the list value in bacon?

bacon.append(99)
bacon


# In[ ]:


#7 [3.14, 'cat', 11, 'cat', True, 99]


# In[31]:


#8. How does bacon.remove('cat') change the look of the list in bacon?
bacon.remove('cat')
bacon


# In[ ]:


#8 [3.14, 11, 'cat', True, 99]


# In[19]:


#9. What are the list concatenation and list replication operators?
# The operator for list concatenation is +, while the operator for replication is *. (This is the same as for strings.)


# In[20]:


#10. What is difference between the list methods append() and insert()?
# While append() will add values only to the end of a list, insert() can add them anywhere in the list.


# In[ ]:


#11. What are the two methods for removing items from a list?
#The del statement and the remove() list method are two ways to remove values from a list.


# In[ ]:


#12. Describe how list values and string values are identical.
# Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.


# In[ ]:


#13. What's the difference between tuples and lists?
# Lists are mutable; they can have values added, removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, ( and ), while lists use the square brackets, [ and ].


# In[ ]:


#14. How do you type a tuple value that only contains the integer 42?
#(42,) (The trailing comma is mandatory.)


# In[ ]:


#15. How do you get a list value's tuple form? How do you get a tuple value's list form?
#The tuple() and list() functions, respectively


# In[ ]:


#16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
#They contain references to list values.


# In[ ]:


#17. How do you distinguish between copy.copy() and copy.deepcopy()?
#The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.

