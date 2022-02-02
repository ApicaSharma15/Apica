#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. In what modes should the PdfFileReader() and PdfFileWriter() File objects will be opened?
#PdfFileReader() needs to be opened in read-binary mode by passing 'rb' as the second argument to open(). Likewise, the File object passed to PyPDF2. 
#PdfFileWriter() needs to be opened in write-binary mode with 'wb'.


# In[ ]:


#2. From a PdfFileReader object, how do you get a Page object for page 5?
# To extract text from a page, you need to get a Page object, which represents a single page of a PDF, from a PdfFileReader object. You can get a Page object by calling the getPage() method on a PdfFileReader object and passing it the page number of the page you're interested in—in our case,5 .
#pdfReader.getPage(4). Calling getPage(4) will return a Page object for page 5, since page 0 is the first page


# In[ ]:


#3. What PdfFileReader variable stores the number of pages in the PDF document?
#The total number of pages in the document is stored in the numPages attribute of a PdfFileReader object


# In[ ]:


#4. If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?
#Call decrypt('swordfish').


# In[ ]:


#5. What methods do you use to rotate a page?
#The rotateClockwise() and rotateCounterClockwise() methods. The degrees to rotate is passed as an integer argument


# In[ ]:


#6. What is the difference between a Run object and a Paragraph object?
# A document contains multiple paragraphs. 
#A paragraph begins on a new line and contains multiple runs. 
#Runs are contiguous groups of characters within a paragraph.


# In[ ]:


#7. How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc?
 doc.paragraphs.


# In[ ]:


#8. What type of object has bold, underline, italic, strike, and outline variables?
# A Run object has these variables (not a Paragraph).


# In[ ]:


#9. What is the difference between False, True, and None for the bold variable?
# True always makes the Run object bolded and False makes it always not bolded, no matter what the style’s bold setting is. None will make the Run object just use the style’s bold setting.


# In[ ]:


#10. How do you create a Document object for a new Word document?
#Call the docx.Document() function


# In[ ]:


#11. How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc?
doc.add_paragraph('Hello there!')


# In[ ]:


#12. What integers represent the levels of headings available in Word documents?
# The integers 0, 1, 2, 3, and 4

