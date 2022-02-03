#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
years_list = [1991,1992,1993,1994,1995,1996]


# In[ ]:


#2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.
years_list[1993]


# In[ ]:


#3.In the years list, which year were you the oldest?
years_list[-1]


# In[1]:


#4. Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
things_list =["mozzarella", "cinderella", "salmonella"]


# In[3]:


#5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
for i in range(len(things_list)):
   
    if things_list[i] == 'cinderella': 
        things_list[i] = things_list[i].capitalize()
print (things_list) 

#yes the first letter in Cinderella is capitalised


# In[4]:


#6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."
Surprise_list=["Groucho", "Chico", "Harpo"]


# In[28]:


#7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
for i in range(len(Surprise_list)):
   
        Surprise_list[-1] == Surprise_list[-1].lower()
        Surprise_list[-1] = Surprise_list[-1][::-1]
        Surprise_list[-1][::-1].capitalize()

        print (Surprise_list) 


# In[29]:


#8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
e2f ={'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
e2f


# In[31]:


#9. Write the French word for walrus in your three-word dictionary e2f.
e2f['walrus']


# In[32]:


#10. Make a French-to-English dictionary called f2e from e2f. Use the items method.
f2e= {}
for english, french in e2f.items():
    f2e[french]= english
f2e 


# In[34]:


#11. Print the English version of the French word chien using f2e.
f2e["chien"]


# In[35]:


#12. Make and print a set of English words from the keys in e2f.
set(e2f.keys())


# In[58]:


#13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.


dict =  {"animals" : {"cats" :[ "Henry", "Grumpy", "Lucy"],"octopi":{""},"emus"  :{""}}, "plants" :{""},"others" :{""}} 
print (dict)


# In[59]:


#14. Print the top-level keys of life.
print(list(dict.keys()))


# In[61]:


#15. Print the keys for life['animals'].
print(dict['animals'].keys())


# In[62]:


#16. Print the values for life['animals']['cats']
print(dict['animals']['cats'])


# In[ ]:





# In[ ]:




