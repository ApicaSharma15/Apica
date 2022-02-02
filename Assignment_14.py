#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. What does RGBA stand for?
RGBA(Red-Green-Blue-Alpha)
The RGB color model is extended in this specification to include “alpha” to allow specification of the opacity of a color.


# In[ ]:


#2. From the Pillow module, how do you get the RGBA value of any images?
from PIL import Image
  
img = Image.open('image.png')
rgba = img.convert("RGBA")
datas = rgba.getdata()
  
newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
        # storing a transparent value when we find a black colour
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)  # other colours remain unchanged
  
rgba.putdata(newData)
rgba.save("transparent_image.png", "PNG")


# In[ ]:


#3. What is a box tuple, and how does it work?
The box.tuple submodule provides read-only access for the tuple userdata type. It allows, for a single tuple: selective retrieval of the field contents, retrieval of information about size, iteration over all the fields, and conversion to a Lua table.
Many of Pillow’s functions and methods take a box tuple argument. This means Pillow is expecting a tuple of four integer coordinates that represent a rectangular region in an image. The four integers are, in order, as follows:

Left The x-coordinate of the leftmost edge of the box.

Top The y-coordinate of the top edge of the box.

Right The x-coordinate of one pixel to the right of the rightmost edge of the box. This integer must be greater than the left integer.

Bottom The y-coordinate of one pixel lower than the bottom edge of the box. This integer must be greater than the top integer.

Note that the box includes the left and top coordinates and goes up to but does not include the right and bottom coordinates. 


# In[ ]:


#4. Use your image and load in notebook then, How can you find out the width and height of an Image object?
# import required module
from PIL import Image
  
# get image
filepath = "Apica.png"
img = Image.open(filepath)
  
# get width and height
width = img.width
height = img.height
  
# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)


# In[ ]:


#5. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?
imageObj.crop((0, 50, 50, 50)). 
Notice that you are passing a box tuple to crop(), not four separate integer arguments.


# In[ ]:


#6. After making changes to an Image object, how could you save it as an image file?
Call the imageObj.save('new_filename.png') method of the Image object.


# In[ ]:


#7. What module contains Pillow’s shape-drawing code?
The ImageDraw module contains code to draw on images.


# In[ ]:


#8. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?
ImageDraw objects have shape-drawing methods such as point(), line(),
or rectangle(). They are returned by passing the Image object to the
ImageDraw.Draw() function.

