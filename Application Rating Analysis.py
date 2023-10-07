#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


applications = pd.read_csv('applications.csv')
industries = pd.read_csv('industries.csv')


# In[3]:


applications.columns = applications.columns.str.lower()
applications.columns = applications.columns.str.replace(' ', '_')
industries.columns = industries.columns.str.lower()
industries.columns = industries.columns.str.replace(' ', '_')


# In[4]:


applications.drop_duplicates(subset='applicant_id', keep='first', inplace=True)
applications['external_rating'].fillna(0, inplace=True)
applications['education_level'].fillna('Середня', inplace=True)


# In[5]:


applications_ind = pd.merge(applications, industries, on='industry', how='left')


# In[6]:


applications_ind['applied_at'] = pd.to_datetime(applications_ind['applied_at'])
applications_ind['day'] = applications_ind['applied_at'].dt.strftime('%A')
applications_ind = applications_ind.sort_values('applied_at')


# In[7]:


applications_ind['statement_rating'] = (((applications_ind['age'] >= 35) & (applications_ind['age'] <= 55)) * 20 +
                                       ((applications_ind['day'] != 'Saturday') & (applications_ind['day'] != 'Sunday')) * 20 +
                                       (applications_ind['marital_status'] == 'Married') * 20 +
                                       (applications_ind['location'] == 'Київ чи область') * 10 +
                                       (applications_ind['score']) +
                                       (applications_ind['external_rating'] >= 7) * 20 - 
                                       (applications_ind['external_rating'] <= 2) * 20)


# In[8]:


applications_ind['statement_rating'][(applications_ind['amount'].isnull()) | (applications_ind['external_rating'] == 0)] = 0
applications_ind['statement_rating'] = applications_ind['statement_rating'].clip(0, 100)
applications_ind.head()


# In[9]:


applications_top = applications_ind[applications_ind['statement_rating'] > 0]


# In[10]:


applications_top['week'] = applications_top['applied_at'].dt.strftime('%U')
applications_top['year'] = applications_top['applied_at'].dt.strftime('%Y')
weekly_average_rating = applications_top.groupby(['year', 'week'])['statement_rating'].mean().reset_index()


# In[11]:


plt.figure(figsize=(12, 6))
plt.plot(weekly_average_rating['week'], weekly_average_rating['statement_rating'])
plt.title('Average rating of accepted applications per week')
plt.xlabel('Week')
plt.ylabel('Average statement rating')
plt.ylim(0, 55)
plt.show()


# In[ ]:




