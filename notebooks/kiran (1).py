# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8

# In[1]:


1 + 1
1 + 1

# In[2]:


print('Hello World!')


# In[3]:


def say_hello(recipient):
    return 'Hello, {}!'.format(recipient)

say_hello('Tim')


# In[ ]:




# COMMAND ----------

# MAGIC %sh curl -n https://cust-success.cloud.databricks.com/#setting/clusters/api/1.2/clusters/list

# COMMAND ----------

# MAGIC %sh curl -n https://cust-success.cloud.databricks.com/#setting/clusters/api/1.2/clusters/list | running

# COMMAND ----------


print('abc')
df = spark.sql("select 1, 2, 35, 1, 2, 3, 4,1, 2, 35, 1, 2, 3, 4,1, 2, 35, 1, 2, 3, 4,1, 2, 35, 1, 2, 3, 4,1, 2, 35, 1, 2, 3, 4,5 as this_is_a_very_long_name_this_is_a_very_long_name5_this_is_a_very_long_name_this_is_a_very_long_name56")
display(df)
