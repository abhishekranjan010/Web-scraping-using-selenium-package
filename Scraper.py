#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[2]:


from selenium.webdriver.support.select import Select


# In[3]:


from selenium.webdriver.common.by import By


# In[4]:


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import action_builder
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.html5 import application_cache
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.utils import basestring


# In[5]:


from webdriver_manager.chrome import ChromeDriverManager


# In[6]:


import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/LENOVO/Downloads/Compressed/chromedriver_win32/chromedriver.exe')

driver.get('https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365')
driver.implicitly_wait(20)

see_all_reviews= driver.find_element_by_xpath('//*[@id="customer-reviews-header"]/div[2]/div/div[3]/a[2]').click()

element= Select(driver.find_element_by_tag_name("select")).select_by_index(2).click()
dropdown= element.select_by_index()

reviews= driver.find_elements_by_class_name('review').text()


driver.close()


# In[7]:


from selenium import webdriver

driver = webdriver.Chrome('C:/Users/LENOVO/Downloads/Compressed/chromedriver_win32/chromedriver.exe')

driver.get('https://www.walmart.com/reviews/product/14898365?sort=submission-desc')
driver.implicitly_wait(5)

reviews= driver.find_elements_by_class_name('review')
for review in reviews:
    print(review.text)

#pagination= driver.find_elements_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[2]/div/div/button')


# In[11]:


import pandas as pd


# In[16]:


driver = webdriver.Chrome('C:/Users/LENOVO/Downloads/Compressed/chromedriver_win32/chromedriver.exe')

driver.get('https://www.walmart.com/reviews/product/14898365?sort=submission-desc')
driver.implicitly_wait(5)

review_date= driver.find_elements(By.CLASS_NAME, "review-date")
reviewer_name= driver.find_elements(By.CLASS_NAME, "review-user")
review_title_and_ratings= driver.find_elements(By.CLASS_NAME, "review-heading")
review_description= driver.find_elements(By.CLASS_NAME, "review-description")



for review in review_date:
    print(review.text)

print("*"*50)

for name in reviewer_name:
    print(name.text)

print("*"*50)

for title in review_title_and_ratings:
    print(title.text)

print("*"*50)

for body in review_description:
    print(body.text)



# In[8]:


driver = webdriver.Chrome('C:/Users/LENOVO/Downloads/Compressed/chromedriver_win32/chromedriver.exe')

driver.get('https://www.walmart.com/reviews/product/14898365?sort=submission-desc')
driver.implicitly_wait(5)

review_date= driver.find_elements(By.CLASS_NAME, "review-date")
reviewer_name= driver.find_elements(By.CLASS_NAME, "review-user")
review_title_and_ratings= driver.find_elements(By.CLASS_NAME, "review-heading")
review_description= driver.find_elements(By.CLASS_NAME, "review-description")


date=[]
name=[]
title_and_ratings=[]
description=[]

for review in review_date:
    print(review.text)
    date.append(review.text)

print("*"*50)

for name in reviewer_name:
    print(name.text)
    name.append(name.text)

print("*"*50)

for title in review_title_and_ratings:
    print(title.text)
    title_and_ratings.append(title.text)

print("*"*50)

for body in review_description:
    print(body.text)



#finallist= zip()

#for data in list(finallist):
#    print(data)


# In[19]:


driver = webdriver.Chrome('C:/Users/LENOVO/Downloads/Compressed/chromedriver_win32/chromedriver.exe')

driver.get('https://www.walmart.com/reviews/product/14898365?sort=submission-desc')
driver.implicitly_wait(5)

reviews= driver.find_elements(By.ID, "product-review-scroll-hook")
reviews_list= []

for review in reviews:
    review_date= driver.find_elements(By.CLASS_NAME, "review-date")
    reviewer_name= driver.find_elements(By.CLASS_NAME, "review-user")
    review_title_and_ratings= driver.find_elements(By.CLASS_NAME, "review-heading")
    review_description= driver.find_elements(By.CLASS_NAME, "review-description")
    item= {
        'date':review_date,
        'name':reviewer_name,
        'title_and_ratings':review_title_and_ratings,
        'description':review_description
    }
    
    reviews_list.append(item)


df= pd.DataFrame(reviews_list)
print(df)

df.to_csv('output', index=False)


# In[ ]:





# In[ ]:




