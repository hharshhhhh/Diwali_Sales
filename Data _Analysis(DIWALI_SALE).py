#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb


# In[8]:


df=pd.read_csv(r'C:\Users\harsh\OneDrive\Desktop\Downloads\DIWALI_SALE.csv', encoding='unicode_escape')


# In[9]:


df.shape


# In[10]:


df.head(10)


# In[11]:


df.info()


# In[14]:


#To drop empty columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[15]:


df.head(5)


# In[17]:


pd.isnull(df).sum()
#To check null values in column


# In[18]:


df.dropna(inplace=True)


# In[19]:


df.columns


# In[20]:


df.describe()


# In[21]:


sx = sb.countplot(x = 'Gender',data = df)

for bars in sx.containers:
    sx.bar_label(bars)


# In[23]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sb.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# # Females are doing more shopping than males

# In[24]:


sx = sb.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in sx.containers:
    sx.bar_label(bars)


# In[25]:


sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sb.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# # Sales in different states

# In[27]:


sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(11)

sb.set(rc={'figure.figsize':(15,5)})
sb.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[28]:


sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sb.set(rc={'figure.figsize':(15,5)})
sb.barplot(data = sales_state, x = 'State',y= 'Amount')


# In[29]:


sx = sb.countplot(data = df, x = 'Marital_Status')

sb.set(rc={'figure.figsize':(7,5)})
for bars in sx.containers:
    sx.bar_label(bars)


# In[30]:


sb.set(rc={'figure.figsize':(20,5)})
sx = sb.countplot(data = df, x = 'Occupation')

for bars in sx.containers:
    sx.bar_label(bars)


# In[31]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sb.set(rc={'figure.figsize':(20,5)})
sb.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# In[32]:


sb.set(rc={'figure.figsize':(20,5)})
sx = sb.countplot(data = df, x = 'Product_Category')

for bars in sx.containers:
    sx.bar_label(bars)


# In[33]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(11)

sb.set(rc={'figure.figsize':(20,5)})
sb.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# In[34]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sb.set(rc={'figure.figsize':(20,5)})
sb.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[35]:


fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




