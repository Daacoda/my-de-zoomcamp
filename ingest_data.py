#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd


# In[12]:


# Read a sample of the data
prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
url = f'{prefix}/yellow_tripdata_2021-01.csv.gz'
url


# In[13]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[14]:


from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg://root:root@localhost:5432/ny_taxi')


# In[15]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[16]:


df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[17]:


# This asks Postgres for data. 
# It will return an empty result because the table in SQL is empty!
pd.read_sql('SELECT * FROM yellow_taxi_data', con=engine)


# In[18]:


df_iter = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=50000
)


# In[19]:


get_ipython().system('uv add tqdm')
from tqdm.auto import tqdm


# In[20]:


for df_chunk in tqdm(df_iter):
  df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')


# In[ ]:


# This asks Postgres for data. 
# It will return an empty result because the table in SQL is empty!
pd.read_sql('SELECT * FROM yellow_taxi_data', con=engine)


# In[ ]:





# In[21]:





# In[23]:





# In[ ]:




