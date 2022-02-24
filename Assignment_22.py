#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. What is the result of the code, and explain?


## >>> X = 'iNeuron'
## >>> def func():
## print(X)


## >>> func()

X = 'iNeuron'
def func():
    print(X)
func()

#Ans. The global variables are accessible inside the functions in python. 
#But we can not access function variable out side function. 
#Since x is global variable we are able to print it inside the function solution : 'iNeuron'


# In[2]:


#2. What is the result of the code, and explain?


## >>> X = 'iNeuron'
## >>> def func():
## X = 'NI!'


## >>> func()
## >>> print(X)

X = 'iNeuron'
def func():
    X = 'NI!'

func()
print(X)

#Ans. The global variables are access inside the functions in python. But we can not access function variable outside function.
# Since x is golbal variable we are able to print it outside of the function solution = 'iNeuron'


# In[3]:


#3. What does this code print, and why?


## >>> X = 'iNeuron'
## >>> def func():
## X = 'NI'
## print(X)


## >>> func()
## >>> print(X)

X = 'iNeuron'
def func():
    X = 'NI!'
    print(X)

func()
print(X)

#Ans. The global variables are access inside the functions in python. But we can not access function variable outside function.
# X is updated with 'NI' which is local to function and its immutable. Its name space is with in the function solution = 'NI!', 'iNeuron'


# In[4]:


#4. What output does this code produce? Why?


## >>> X = 'iNeuron'
## >>> def func():
## global X
## X = 'NI'


## >>> func()
## >>> print(X)

X = 'iNeuron'
def func():
    global X
    X = 'NI!'
    print(X)

func()
print(X)
#Ans. since the X inside function is made Global, it will be accesible outside of the function too. 
#now X will have new value.

 #solution : 'NI!', 'NI!'


# In[5]:


#5. What about this code—what’s the output, and why?


## >>> X = 'iNeuron'
## >>> def func():
## X = 'NI'
## def nested():
## print(X)
## nested()


## >>> func()
## >>> X

X = 'iNeuron'
def func():
    X = 'NI'
def nested():
    print(X)
    
nested()
func()
X

#Ans. the nested() function will print 'iNeuron', Then func() does not display anything,
# and x ='NI' is not accessible out 
#side the function.
#Solution : 'iNeuron'


# In[6]:


#6. How about this code: what is its output in Python 3, and explain?


## >>> def func():
## X = 'NI'
## def nested():
## nonlocal X
## X = 'Spam'
## nested()
## print(X)


## >>> func()

def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'spam'
    nested()
    print(X)

func()

#Nonlocal variables are used in nested functions whose local scope is not defined. 
#This means that the variable can be neither in the local nor the global scope. it print the updated value from nested 
#function

#Sol : 'spam'


# In[ ]:




