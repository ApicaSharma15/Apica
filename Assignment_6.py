#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. What are escape characters, and how do you use them?
# Escape characters represent characters in string values that would otherwise be difficult or impossible to type into code.
#In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return. Conversely, prefixing a special character with "\" turns it into an ordinary character.


# In[ ]:


#2. What do the escape characters n and t stand for?
#"\t" is a tab, "\n" is a newline,


# In[ ]:


#3. What is the way to include backslash characters in a string?
#The \\ escape character will represent a backslash character.


# In[ ]:


#4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?

# The single quote in Howl's is fine because you’ve used double quotes to mark the beginning and end of the string.


# In[ ]:


#5. How do you write a string of newlines if you don't want to use the n character?
# Multiline strings allow you to use newlines in strings without the \n escape character.


# In[1]:


#6. What are the values of the given expressions?
'Hello, world!'[1]


# In[2]:


'Hello, world!'[0:5]


# In[3]:


'Hello, world!'[:5]


# In[4]:


'Hello, world!'[3:]


# In[ ]:


#'Hello, world!'[1] ------ 'e'
#'Hello, world!'[0:5]----- 'Hello'
#'Hello, world!'[:5] -----  'Hello'
#'Hello, world!'[3:] -----  'lo, world!'


# In[5]:


#7. What are the values of the following expressions?
'Hello'.upper()


# In[6]:


'Hello'.upper().isupper()


# In[7]:


'Hello'.upper().lower()


# In[ ]:


#'Hello'.upper() --- 'HELLO'
#'Hello'.upper().isupper() --- 'True'
#'Hello'.upper().lower() ---- 'hello'


# In[8]:


#8. What are the values of the following expressions?
'Remember, remember, the fifth of July.'.split()


# In[9]:


'-'.join('There can only one.'.split())


# In[ ]:


#'Remember, remember, the fifth of July.'.split() --['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']
#'-'.join('There can only one.'.split()) -- 'There-can-only-one.'


# In[ ]:


#9. What are the methods for right-justifying, left-justifying, and centering a string?
# The rjust(), ljust(), and center() string methods, respectively


# In[ ]:


#10. What is the best way to remove whitespace characters from the start or end?
# The lstrip() and rstrip() methods remove whitespace from the left and right ends of a string, respectively.


# In[ ]:




