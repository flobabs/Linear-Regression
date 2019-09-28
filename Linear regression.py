#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


# In[2]:


Data = pd.read_csv('cost-revenue-dirty.csv')


# In[3]:


Data.describe()


# In[4]:


x = DataFrame(data, columns=['Production_budget_usd'])
y = DataFrame(data, columns=['worldwide_gross_usd'])


# In[ ]:


regression = LinearRegression()
regression.fit(x,y)


# In[ ]:


plt.figure(figsize=(20,16))
plt.scatter(x, y, alpha=0.5)
plt.title('Film cost vs Global Revenue')
plt.xlabel('production budget $')
plt.ylabel('Worldwide Gross $')
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()


# Slope Coefficient

# In[ ]:


regression.coef_


# In[ ]:


#Intercept
regression.intercept_


# In[ ]:





# In[ ]:


plt.figure(figsize=(20,16))
plt.scatter(x, y, alpha=0.5)
#calculating the predicted value 
plt.plot(x, regression.predict(x), color='green', linewidth=4)
#plt.plot(y, regression.predict(y))
plt.title('Film cost vs Global Revenue')
plt.xlabel('production budget $')
plt.ylabel('Worldwide Gross $')
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()


# In[ ]:


#Goodness of Fit (Finding R Squred)
regression.score(x, y)


# In[ ]:


type(Data)


# In[10]:


a = 20
b = 20


# In[11]:


a


# In[12]:


b


# In[ ]:


import collections


# In[ ]:


plt.pie(data.values(), labels=day.keys(),autopct='%1.1f%%')
plt.axis('equal');


# In[ ]:





# In[ ]:




