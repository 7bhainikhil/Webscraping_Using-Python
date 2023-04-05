#!/usr/bin/env python
# coding: utf-8

# In[34]:


from bs4 import BeautifulSoup as bs
import requests
import pandas as pd 


# In[35]:


response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': '22426d46-949d-43eb-8341-b95904982db6',
      'url': 'https://collegedunia.com/university/18416-mit-world-peace-university-mitwpu-pune/reviews/page-2',
      
  },
)


# In[36]:


soup=bs(response.content,'html.parser')


# In[37]:


names = soup.find_all('a',class_='user-name')
names


# In[38]:


cust_name = []
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())
cust_name


# In[39]:


head =soup.find_all('a',class_='review-card-title')
head
len(head)


# In[40]:


title_head = []
for i in range(0,len(head)):
    title_head.append(head[i].get_text())
title_head


# In[41]:


df = pd.DataFrame()


# In[42]:


df=pd.DataFrame()


# In[43]:


df['Name']=cust_name
df['Head_Comment']=title_head
df


# In[ ]:




