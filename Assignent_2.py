#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 What are the two values of the Boolean data type? How do you write them?
# A variable of the primitive data type boolean can have two values: true and false (Boolean literals).
#Python boolean type is one of the built-in data types provided by Python, which represents one of the two values i.e. True or False. Generally, it is used to represent the truth values of the expressions. For example, 1== 0 is True whereas 2<1 is False


# In[2]:


#2 What are the three different types of Boolean operators?
# The three basic boolean operators are: AND, OR, and NOT.


# In[ ]:


#3 Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate.
# A truth table is a small table that allows us to list all the possible inputs, and to give the results for the logical operators. Because the and and or operators each have two operands, there are only four rows in a truth table that describes the semantics of and.
#a       b     a and b
False	False	False
False	True	False
True	False	False
True	True	True
#In a Truth Table, we sometimes use T and F as shorthand for the two Boolean values: here is the truth table describing or:
#a	b	a or b
F	F	F
F	T	T
T	F	T
T	T	T
#The third logical operator, not, only takes a single operand, so its truth table only has two rows:
#a	not a
F	T
T	F


# In[ ]:


#4 What are the values of the following expressions?
(5 > 4) and (3 == 5) ---- FALSE
not (5 > 4) --- FALSE
(5 > 4) or (3 == 5) -----TRUE

not ((5 > 4) or (3 == 5)) ----- FALSE
(True and True) and (True == False) -----FALSE
(not False) or (not True) ------TRUE


# In[ ]:


#5 What are the six comparison operators?
# x == y               # Produce True if ... x is equal to y
# x != y               # ... x is not equal to y
# x > y                # ... x is greater than y
# x < y                # ... x is less than y
# x >= y               # ... x is greater than or equal to y
# x <= y               # ... x is less than or equal to y


# In[ ]:


#6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# The Python symbols are different from the mathematical symbols. A common error is to use a single equal sign (=) instead of a double equal sign (==). Remember that = is an assignment operator and == is a comparison operator.
The ‘==’ operator checks whether the two given operands are equal or not. If so, it returns true. Otherwise it returns false.
For example:

5==5

This will return true

The “=” is an assignment operator is used to assign the value on the right to the variable on the left.

For example:

a = 10;
b = 20;
ch = 'y';


# In[ ]:


#7 
1)spam = 0
if spam == 10:
2)print('eggs')
if spam > 5:
3)print('bacon')
else:
3)print('ham')
2)print('spam')
1)print('spam')


# In[14]:


#8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam = int(input())

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')


# In[ ]:


#9 If your programme is stuck in an endless loop, what keys you’ll press?
Ctrl + C 


# In[ ]:


#10 How can you tell the difference between break and continue?
#In Python, break and continue statements can alter the flow of a normal loop.

Loops iterate over a block of code until the test expression is false, but sometimes we wish to terminate the current iteration or even the whole loop without checking test expression.

The break and continue statements are used in these cases.

#Python break statement
The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.

If the break statement is inside a nested loop (loop inside another loop), the break statement will terminate the innermost loop.

#The continue statement is used to skip the rest of the code inside a loop for the current iteration only. 
Loop does not terminate but continues on with the next iteration.


# In[ ]:


#11 In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# range(10) ---- range (stop),When user call range() with one argument, user will get a series of numbers that starts at 0 and includes every whole number up to, but not including, the number that user have provided as the stop.
                 output 0 1 2 3 4 5 6 7 8 9
# range (0,10) ----range(start, stop)
When user call range() with two arguments, user get to decide not only where the series of numbers stops but also where it starts, so user don’t have to start at 0 all the time. User can use range() to generate a series of numbers from X to Y using a range(X, Y).
output here 1 2 3 4 5 6 7 8 9
#range (0,10,1) ----range(start, stop, step)
 ----- When the user call range() with three arguments, the user can choose not only where the series of numbers will start and stop but also how big the difference will be between one number and the next. If the user doesn’t provide a step, then range() will automatically behave as if the step is 1.
output 0 1 2 3 4 5 6 7 8 9


# In[15]:


#12 Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

i = 1
while(i<=10):
    print(i)
    i += 1


# In[16]:


for i in range(1, 11):
    print(i)


# In[ ]:


#13 If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
import spam
spam.bacon()

