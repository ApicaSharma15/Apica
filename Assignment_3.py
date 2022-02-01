#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Why are functions advantageous to have in your programs?
# A function is a block of reusable code that is used to perform a specific action .
#Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update. 
# Decomposing complex problems into simpler pieces.
# improving clarity of the code
# reusing code
# information hiding


# In[ ]:


#2. When does the code in a function run: when it's specified or when it's called?
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. Functions are used to perform certain actions, and they are important for reusing code: Define the code once, and use it many times.


# In[ ]:


#3. What statement creates a function?
# The “def” keyword is a statement for defining a function in Python. You start a function with the def keyword, specify a name followed by a colon (:) sign. The “def” call creates the function object and assigns it to the name given. You can further re-assign the same function object to other names.


# In[ ]:


#4. What is the difference between a function and a function call?
# A function call means invoking or calling that function. Unless a function is called there is no use of that function. 
# So the difference between the function and function call is, A function is procedure to achieve a particular result while function call is using this function to achive that task.


# In[ ]:


#5. How many global scopes are there in a Python program? How many local scopes?
#There's only one global Python scope per program execution. This scope remains in existence until the program terminates and all its names are forgotten. 
#Each function has its local scope. 


# In[ ]:


#6. What happens to variables in a local scope when the function call returns?
#When the execution of the function terminates (returns), the local variables are destroyed. Codelens helps you visualize this because the local variables disappear after the function returns.


# In[ ]:


#7. What is the concept of a return value? Is it possible to have a return value in an expression?
# return statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller. The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned.
#If you define a function with an explicit return statement that has an explicit return value, then you can use that return value in any expression


# In[ ]:


#8. If a function does not have a return statement, what is the return value of a call to that function?
#If a function doesn't specify a return value, it returns None . In an if/then conditional statement, None evaluates to False.


# In[ ]:


#9. How do you make a function variable refer to the global variable?
#If you want to refer to a global variable in a function, you can use the global keyword to declare which variables are global.


# In[ ]:


#10. What is the data type of None?
#None is used to define a null value. It is not the same as an empty string, False, or a zero. It is a data type of the class NoneType object. Assigning a value of None to a variable is one way to reset it to its original, empty state.


# In[ ]:


#11. What does the sentence import areallyourpetsnamederic do?
#That import statement imports a module named areallyourpetsnamederic .(This isn’t a real Python module, by the way.)


# In[ ]:


#12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
#This function can be called with spam.bacon().


# In[ ]:


#13. What can you do to save a programme from crashing if it encounters an error?
#Place the line of code that might cause an error in a try clause.


# In[ ]:


#14. What is the purpose of the try clause? What is the purpose of the except clause? 
#The code that could potentially cause an error goes in the try clause.

#The code that executes if an error happens goes in the except clause.


# In[ ]:





# In[ ]:





# In[ ]:




