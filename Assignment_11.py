#!/usr/bin/env python
# coding: utf-8

# In[8]:


#1. Create an assert statement that throws an Assertion Error if the variable spam is a negative integer.
spam = -25
assert spam >=10, 'Only negative numbers are allowed'
print ('spam is a negative number')




# In[12]:


#2. Write an assert statement that triggers an Assertion Error if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
eggs = 'hello'
bacon = 'goodbye'
assert eggs.lower() != bacon.lower(), 'eggs/bacon should not be the same!'
assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'


# In[20]:


#3. Create an assert statement that throws an AssertionError every time.
# assert True, 'Always triggers an AssertionError.'


# In[22]:


#4. What are the two lines that must be present in your software in order to call logging.debug()?
# To be able to call logging.debug(), you must have these two lines at the start of your program:
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')


# In[ ]:


#5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
#To be able to send logging messages to a file named programLog.txt with logging.debug(), you must have these two lines at the start of youprogram:
import logging
>>> logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')


# In[ ]:


#6. What are the five levels of logging?
#DEBUG, INFO, WARNING, ERROR, and CRITICAL


# In[ ]:


#7. What line of code would you add to your software to disable all logging messages?
#logging.disable(logging.CRITICAL)


# In[ ]:


#8.Why is using logging messages better than using print() to display the same message?
#You can disable logging messages without removing the logging function calls. You can selectively disable lower-level logging messages. You can create logging messages. Logging messages provides a timestamp.


# In[ ]:


#9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
#The Step button will move the debugger into a function call. 
#The Over button will quickly execute the function call without stepping into it. 
#The Out button will quickly execute the rest of the code until it steps out of the function it currently is in.


# In[ ]:


#10.After you click Continue, when will the debugger stop ?
#After you click Go, the debugger will stop when it has reached the end of the program or a line with a breakpoint.


# In[ ]:


#11. What is the concept of a breakpoint?
#A breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line.


# In[ ]:




