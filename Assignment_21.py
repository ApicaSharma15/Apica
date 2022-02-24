#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Add the current date to the text file today.txt as a string.
import datetime
from datetime import date
now = date.today()
cur_date = now.isoformat()
cur_date


# In[2]:


#2. Read the text file today.txt into the string today_string
with open('today.txt','w') as file:
    file.write(cur_date)


# In[3]:


#3. Parse the date from today_string.
with open('today.txt','r') as file:
    today_string = file.read()
today_string


# In[4]:


#4. List the files in your current directory
from datetime import datetime
format = '%Y-%m-%d'
datetime.strptime(today_string,format)


# In[5]:


#5. Create a list of all of the files in your parent directory (minimum five files should be available).
import os
os.listdir('.')


# In[6]:


#6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.
import multiprocessing

def printsec(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())
    
if __name__ == '__main__':
    import random    
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=printsec, args=(seconds,))
        proc.start()


# In[ ]:





# In[12]:


#7. Create a date object of your day of birth.
my_dob = date(1991,6,15)
my_dob


# In[13]:


#8. What day of the week was your day of birth?
my_dob.weekday()


# In[14]:


#9. When will you be (or when were you) 10,000 days old?
from datetime import timedelta
day10000 = my_dob + timedelta(days=10000)
day10000


# In[ ]:





# In[ ]:




