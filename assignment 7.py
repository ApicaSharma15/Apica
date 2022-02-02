#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. What is the name of the feature responsible for generating Regex objects?

#The re.compile() function returns Regex objects.


# In[ ]:


#2. Why do raw strings often appear in Regex objects?
# Raw strings are used so that backslashes do not have to be escaped.


# In[ ]:


#3. What is the return value of the search() method?
#The search() method returns Match objects. The Python find() is an in-built string method that returns the index position of the character if found; else it returns value -1.


# In[ ]:


#4. From a Match item, how do you get the actual strings that match the pattern?
#The group() method returns strings of the matched text.


# In[ ]:


#5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover? Group 2? Group 1?
# Group 0 is the entire match, group 1 covers the first set of parentheses, and group 2 covers the second set of parentheses.


# In[ ]:


#6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell a regex that you want it to fit real parentheses and periods?
# Periods and parentheses can be escaped with a backslash: \., \(, and \).


# In[ ]:


#7. The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options?
# If the regex has no groups, a list of strings is returned. If the regex has groups, a list of tuples of strings is returned.


# In[ ]:


#8. In standard expressions, what does the | character mean?
# The | character signifies matching “either, or” between two groups.


# In[ ]:


#9. In regular expressions, what does the character ? stand for?
# The ? character can either mean “match zero or one of the preceding group” or be used to signify nongreedy matching.


# In[ ]:


#10.In regular expressions, what is the difference between the + and * characters?
# The + matches one or more. The * matches zero or more.


# In[ ]:


#11. What is the difference between {4} and {4,5} in regular expression?
#The {4} matches exactly four instances of the preceding group. The {4,5} matches between four and five instances.


# In[ ]:


#12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular expressions?
# The \d, \w, and \s shorthand character classes match a single digit, word, or space character, respectively.


# In[ ]:


#13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?
# The \D, \W, and \S shorthand character classes match a single character that is not a digit, word, or space character, respectively.


# In[ ]:


#14. What is the difference between .*? and .*       ?
# The .* performs a greedy match, and the .*? performs a nongreedy match.
#The greedy match will try to match as many repetitions of the quantified pattern as possible. The non-greedy match will try to match as few repetitions of the quantified pattern as possible.


# In[ ]:


#15. What is the syntax for matching both numbers and lowercase letters with a character class?
# Either [0-9a-z] or [a-z0-9]


# In[ ]:


#16. What is the procedure for making a normal expression in regax case insensitive?
# Passing re.I or re.IGNORECASE as the second argument to re.compile() will make the matching case insensitive.


# In[ ]:


#17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?
# The . character normally matches any character except the newline character. If re.DOTALL is passed as the second argument to re.compile(), then the dot will also match newline characters.


# In[3]:


#18. If numReg = re.compile(r'\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return?
import re
numReg = re.compile(r'\d+')
numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')


# In[ ]:


'X drummers, X pipers, five rings, X hen'


# In[ ]:


#19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?
# The re.VERBOSE argument allows you to add whitespace and comments to the string passed to re.compile().


# In[ ]:


#20. How would you write a regex that match a number with comma for every three digits? It must match the given following:
'42'
'1,234'
'6,368,745'
but not the following:
'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)
# re.compile(r'\d{1,3}(,\d{3})*') will create this regex, but other regex strings can produce a similar regular expression.


# In[4]:


#This program is to validate the regular expression for this scenerio. 
#Any properly formattes number (w/Commas) will match.
#Parsing through a document for this regex is beyond my capability at this time.

print('Type a number with commas')
sentence = input() 

import re

pattern = re.compile(r'\d{1,3}(,\d{3})*')

matches = pattern.match(sentence)
if matches.group(0) != sentence:
    #Checks to see if the input value
    #does NOT match the pattern.
    print ('Does Not Match the Regular Expression!')

else:
    print(matches.group(0)+ ' matches the pattern.')
    #If the values match it will state verification.


# In[ ]:


#21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
but not the following:
'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)


# In[7]:


name_regex = re.compile(r'[A-Z](?:\w)+\sWatanabe')

text = "The regex must match the following: 'Haruto Watanabe' 'Alice Watanabe' 'RoboCop Watanabe' but not the following: 'haruto Watanabe' (where the first name is not capitalized) 'Mr. Watanabe' (where the preceding word has a nonletter character) 'Watanabe'(which has no first name) 'Haruto watanabe'."

print("\n\n\t*************\n\nThis is the result I get using my regex with search in text:")
mo0 = name_regex.search(text)
found = mo0.group()
print(found + '\n\n')

mo1 = name_regex.search('Haruto Watanabe')
mo2 = name_regex.search('Alice Watanabe')
mo3 = name_regex.search('RoboCop Watanabe')
mo4 = name_regex.search('Watanabe')
mo5 = name_regex.search('Mr. Watanabe')
mo6 = name_regex.search('Haruto watanabe')
mo7 = name_regex.search('haruto watanabe')

mo_l = [mo1, mo2, mo3, mo4, mo5, mo6, mo7]

print("Next, the result of using my regex with search over each possible name to match:")
try:
    for mo_x in mo_l:
        mo = mo_x.group()
        print(mo)
except AttributeError:
    pass

print("\n\nFinally, the result of using the same regex with findall (same text as in first search):")

all_matches = re.findall(name_regex, text)

for match in all_matches:
    print(match)


# In[ ]:


#22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:
'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'


# In[25]:


import regex as re 
str = 'Alice|Bob|Carol|eats|pets|throws|apples|cats|baseballs'
regex=re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
mo=regex.search(str)

mo


# In[ ]:





# In[ ]:





# In[ ]:




