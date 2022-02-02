#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Is the Python Standard Library included with PyInputPlus?
#PyInputPlus is not a part of the Python Standard Library, so you must install it separately using Pip. To install PyInputPlus, run pip install --user pyinputplus from the command line.


# In[ ]:


#2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
#You can import the module with import pyinputplus as pyip so that you can enter a shorter name when calling the module's functions. PyInputPlus has functions for entering a variety of input, including strings, numbers, dates, yes/no, True/False, emails, and files.


# In[ ]:


#3. How do you distinguish between inputInt() and inputFloat()?
#inputInt() : Accepts an integer value. This also takes additional parameters 'min', 'max', 'greaterThan' and 'lessThan' for bounds. Returns an int. inputFloat() : Accepts a floating-point numeric value.


# In[ ]:


#4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
#By using pyip.inputint(min=0, max=99).


# In[ ]:


#5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
#You can also use regular expressions to specify whether an input is allowed or not. The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input. 


# In[4]:


#6. If a blank input is entered three times, what does inputStr(limit=3) do?
#inputStr() raises a TimeoutException exception. If the user answers incorrectly more than 3 times, it raises a RetryLimitException exception.


# In[ ]:


#7. If blank input is entered three times, what does inputStr(limit=3, default=&#39;hello&#39;) do?
 # PyInputPlus will keep asking the user for text until they enter valid input.


# In[ ]:




