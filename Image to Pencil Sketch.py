#!/usr/bin/env python
# coding: utf-8

# 
# # Image to Pencil Sketch with Python:

# ### 1. Importing Required Libraries

# In[17]:


import  cv2
import numpy as np


# ### 2. Loading Image
# 

# In[26]:


image=plt.imread("Compress.jpg")
show("image",image,'RdGy')


# ### 3. Convert Into GrayScale Image 

# In[19]:


gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
show("Gray_image",gray_image,'gray')


# ### 4. Invert The GrayScale Image

# In[27]:


Inverted_Image =255-gray_image
show("Inverted_Image",Inverted_Image,'gray')


# ### 4. Blur The Inverted Image

# In[29]:


Blurred_Image =cv2.GaussianBlur(Inverted_Image,(21,21), sigmaX=0, sigmaY=0)
show("Blurred_Image",Blurred_Image,'gray')


# ### 5. Create Pencil Sketch Image

# In[22]:


Inverted_Blurred=255-Blurred_Image
Pencil_Sketch=cv2.divide(gray_image,Inverted_Blurred,scale=256.0)
show("Pencil_Sketch",Pencil_Sketch,'gray')


# # THANK YOU! 
