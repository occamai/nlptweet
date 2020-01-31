#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import tweepy as tw
import pandas as pd
import csv


# In[2]:


consumer_key= 'swDlscPnoEH0jWqyzXNw76NJq'
consumer_secret= 'SXZC7rFMIv3EETNcwHxK0L0RLplPVaHGHP9Rm2HTd73iyaNE2U'
access_token= '1220403631695904768-knKEXn7WqnEt5FkvqSUm0sgC3MEhXW'
access_token_secret= 'fyduCeYiiWft9gWVa5G9rRPDQLCUYX3YugmOAKMbGzptq'


# In[3]:


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# In[6]:


# Open/Create a file to append data
csvFile = open('kobe.csv', 'a', newline = "")
#Use csv Writer
csvWriter = csv.writer(csvFile)


# In[7]:


# Define the search term and the date_since date as variables
search_words = "#kobe"
date_since = "2020-1-16"


# In[8]:


new_search = search_words + " -filter:retweets"
new_search
'#kobe -filter:retweets'


# In[9]:


tweets = tw.Cursor(api.search,
                       q=new_search,
                       lang="en",
                       since=date_since).items(5)

[tweet.text for tweet in tweets]


# In[10]:


for tweet in tw.Cursor(api.search, 
                           q=new_search,
                           lang="en",
                           since=date_since).items(5):
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
csvFile.close()


# In[ ]:




