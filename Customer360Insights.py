#!/usr/bin/env python
# coding: utf-8

# In[1]:


#First we are importing our libraries and Dataset 


# In[177]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[102]:


df = pd.read_csv("C:\\Users\\Riya\\Downloads\\archive (2)\\Customer360Insights.csv")


# In[103]:


#head function is called when we want to see first n number of rows, 
#same as tail function is used when we want to see last n number of rows.


# In[104]:


df.head(5)


# In[105]:


df.tail(5)


# In[106]:


#This will tell us about basic information which needed like column name, null value count and type of column


# In[107]:


df.info()


# In[108]:


#nunique is used for checking number of unique values in particular column


# In[109]:


df['Country'].unique()


# In[110]:


#Unique is used for checking the unique values in particular column


# In[111]:


df['Category'].unique()


# In[112]:


df.describe()


# In[113]:


df['Product'].unique()


# In[114]:


#Groupby function


# In[115]:


df.groupby('Country')['MonthlyIncome'].mean()


# In[116]:


#isnull function is used for checking null values in columns


# In[117]:


df.isnull().sum()


# In[ ]:


#Value_counts will count the Unique values in that particular column


# In[118]:


df['Gender'].value_counts()


# In[119]:


df.groupby('Country')['OrderReturn'].value_counts()


# In[120]:


df['Country'].value_counts()


# In[121]:


df.groupby('Country')['CreditScore'].mean()


# In[ ]:


#Here we have used dron function which will drop not required column or we can say less required column
#This is one of the way to handle Nan values if that particular columns is not that much important to our data
#we can easily drop it by using below code.


# In[122]:


df.drop('ReturnReason',axis=1,inplace=True)


# In[123]:


df


# In[124]:


df['PaymentMethod'].value_counts()


# In[ ]:


#duplicated is used for checking the duplicate values in rows.


# In[125]:


df.duplicated()


# In[126]:


df.duplicated().sum()


# In[127]:


df['CreditScore'].max()


# In[128]:


df['CreditScore'].min()


# In[129]:


df.groupby('Category')['OrderConfirmation'].value_counts()


# In[130]:


df1 = df.groupby('Product')['OrderConfirmation'].value_counts()


# In[200]:


df1


# In[132]:


df.columns


# In[133]:


df['SessionStart'] = pd.to_datetime(df['SessionStart'])
df['SessionEnd'] = pd.to_datetime(df['SessionEnd'])
df['CartAdditionTime'] = pd.to_datetime(df['CartAdditionTime'])
df['OrderConfirmationTime'] = pd.to_datetime(df['OrderConfirmationTime'])


# In[134]:


df['SessionDuration'] = (df['SessionEnd'] - df['SessionStart']).dt.total_seconds()/60


# In[ ]:


#By calculating above session duration we can the engagement of user is between 3 minutes to 40 minutes 
#depending on their Sessionstart and Sessionend time duration.


# In[135]:


df['SessionDuration'].sort_values(ascending=False,axis=0)


# In[199]:


df['SessionDuration'].mean()


# In[ ]:


#So basically age segments gives us count of number that how many customers are from having that particular 
#age number.


# In[136]:


age_segments = df.groupby('Age').agg({'CustomerID': 'count'})


# In[137]:


age_segments


# In[138]:


df['Revenue'] = df['Price'] * df['Quantity']


# In[139]:


df['Revenue'].sort_values(ascending=False,axis=0)


# In[ ]:


#Here we have draw the Histogram between Customer age & their count that how many customers have this 
#same age.


# In[162]:


df['Age'].plot(kind='hist', bins=100, edgecolor='black')
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('CustomerID')
plt.show()


# In[ ]:


#Age distribution of the customer and from the analysis we can say female users are more as compare to males.


# In[149]:


df['Gender'].value_counts().plot(kind='bar', color=['pink','blue'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# In[ ]:


#Customer distribution by their country and we can see that highest number of customers are from canada
#and lowest customers are from UK.


# In[156]:


df['Country'].value_counts().plot(kind='bar')
plt.title('Customer Distribution by Country')
plt.xlabel('Country')
plt.ylabel('Count')
plt.show()


# In[ ]:


#from the calculation we can see that avarage time spent by customer is 21 minute and highest is 40 min
#and lowest is 3 min. 


# In[186]:


df['SessionDuration'].plot(kind='hist', bins=150, edgecolor='black')
plt.title('Session Duration Distribution')
plt.xlabel('Session Duration (minutes)')
plt.ylabel('Frequency')
plt.show()


# In[ ]:


#They have run the ad from different social media applications and we can see the number of orders they
#thet have received through this campaign. 


# In[ ]:


#we can see that instagram ads have highest number of orders following by Google-ads and facebook-ads.


# In[180]:


df['CampaignSchema '].value_counts().plot(kind='bar')
plt.title('Effectiveness of Campaigns')
plt.xlabel('Campaign')
plt.ylabel('Number of Orders')
plt.show()


# In[ ]:


#from below we can easily conclude that 34.3% payments done by Credit card following by Debit card which is
#31.1% and Cash on Delivery is having 24% and last paypal at 10.6%.


# In[198]:


df['PaymentMethod'].value_counts().plot(kind='pie', autopct='%1.1f%%',startangle=90)
plt.title('Payment Method Preferences')
plt.show()


# In[ ]:


#Below is Category wise sales quantity and we can see that home appliances are highest at 1523 
#and lowest is 1268 from the category electronics.


# In[183]:


px.bar(df.groupby('Category')['Quantity'].sum().head(),color_discrete_sequence=['lightpink'])


# In[ ]:


#This bar graph tells us about product wise revenue.


# In[185]:


df['Revenue'] = df['Price'] * df['Quantity']
px.bar(df.groupby('Product')['Revenue'].sum(),color_discrete_sequence=['lightgreen'])

