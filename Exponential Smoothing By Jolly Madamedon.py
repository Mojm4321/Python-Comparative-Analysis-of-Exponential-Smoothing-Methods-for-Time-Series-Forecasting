#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import timedelta
start_date = pd.to_datetime("2022-01-01")
end_date = start_date + timedelta(days=199)
date_range = pd.date_range(start_date, end_date, freq='D')
data = {
        'Date': date_range,
        'Value': np.linspace(50, 150, 200) + np.random.normal(scale=10, size=200),
        'Feature1': np.random.randint(1, 100, 200),
        'Feature2': np.random.uniform(0, 1, 200)
}
df = pd.DataFrame(data)


# In[2]:


df.head()


# In[3]:


from statsmodels.tsa.holtwinters import SimpleExpSmoothing


# In[4]:


df


# In[5]:


df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace = True)


# In[6]:


model = SimpleExpSmoothing(df["Value"])
fit_model = model.fit()


# In[7]:


fit_model.summary()


# In[8]:


import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.plot(df['Value'], label='Value')
plt.title('Time Series Plot of Value')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()


# In[9]:


value_summary = df['Value'].describe()
print(value_summary)


# In[10]:


window_size = 10
df['Moving Average'] = df['Value'].rolling(window=window_size).mean()

plt.figure(figsize=(12, 6))
plt.plot(df['Value'], label='Original Value', alpha=0.5)
plt.plot(df['Moving Average'], label=f'{window_size}-Day Moving Average', color='red')
plt.title('Time Series Plot with Moving Average')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()


# In[11]:


import matplotlib.pyplot as plt
plt.figure(figsize=(12, 7))
plt.plot(df.index, df['Value'], label='Original Data')
df['Fitted'] = fit_model.fittedvalues
plt.plot(df.index, df['Fitted'], label='Fitted Values', color='red')
plt.title('Original Data vs Fitted Values')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()


# In[12]:


forecast_period = 90
forecast = fit_model.forecast(steps=forecast_period)
future_dates = pd.date_range(df.index[-1] + timedelta(days=1), periods=forecast_period)
plt.figure(figsize=(12, 7))
plt.plot(df.index, df['Value'], label='Original Data')
plt.plot(df.index, df['Fitted'], label='Fitted Values', color='red')
plt.plot(future_dates, forecast, label='Forecast', color='green')

plt.title('Original Data, Fitted Values, and Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()


# In[14]:


from statsmodels.tsa.holtwinters import Holt
holt_model = Holt(df['Value']).fit()
holt_forecast = holt_model.forecast(steps=90)
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Value'], label='Original Data')
plt.plot(df.index, holt_model.fittedvalues, label='Holt Fitted Values', color='orange')
plt.plot(future_dates, holt_forecast, label='Holt Forecast', color='green')

plt.title('Holt’s Linear Trend Model - Original Data, Fitted Values, and Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()


# In[ ]:




