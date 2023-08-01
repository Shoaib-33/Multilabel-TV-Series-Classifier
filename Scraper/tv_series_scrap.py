#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


# In[1]:


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
series_list = []
y=1
for y in range(1,500):
    print(y)
    url = f"https://www.imdb.com/search/title/?title_type=tv_series&start={y}&ref_=adv_nxt"
    driver = webdriver.Chrome('chromedriver')
    driver.get(url)
    x1 = driver.find_element(By.CLASS_NAME, "lister-list")
    x2=driver.find_element(By.CLASS_NAME, "lister-item-content")
    for i in range(1,51):
        # xpath_genre = f"//div/div[3]/div/div[1]/div[3]/p[{i}]"
        xpath_title =f"//div/div[3]/div/div[{i}]/div[3]/h3"
        xpath_description=f"//div/div[3]/div/div[{i}]/div[3]/p[2]"
        xpath_genre=f"//div[{i}]/div[3]/p[1]"
        p = x2.find_element(By.XPATH, xpath_genre)
        q=  x2.find_element(By.XPATH, xpath_title)
        r=  x2.find_element(By.XPATH, xpath_description)
       
        genre =  p.text.split('|')[-1].strip()
        series_list.append({
                "title":q.text,
                "genres": genre,
                "description":r.text
            })
            
            
            


# In[3]:


len(series_list)


# In[4]:


series_list


# In[2]:


df = pd.DataFrame(data=series_list, columns=series_list[0].keys())
df.to_csv("series_list1.csv", index=False)


# In[5]:


df.head()


# In[15]:


pattern = r'^\d+\.\s+'


# In[16]:


df['title'] = df['title'].str.replace(pattern, '', regex=True)


# In[19]:


df.to_csv("series_list3.csv", index=False)


# In[20]:


df.head()


# In[22]:


df['genres'] = df['genres'].str.split(', ')


# In[23]:


df.head()


# In[24]:


df.to_csv("series_list4.csv", index=False)


# In[ ]:




