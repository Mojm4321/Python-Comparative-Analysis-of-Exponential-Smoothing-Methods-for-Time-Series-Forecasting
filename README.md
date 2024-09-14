# Comparative Analysis Of Exponential Smoothing Methods For Time Series Forecasting

# Introduction
The primary purpose of this report is to analyse and compare different exponential smoothing methods for time series forecasting, using a dataset with a clear linear trend and random fluctuations. By applying these techniques to a simulated dataset, the report aims to evaluate their effectiveness in capturing the trend and managing noise. The analysis will highlight the strengths and limitations of each method, particularly in scenarios where seasonality is absent, and will provide guidance on selecting the most suitable forecasting approach for similar data patterns. 

# Dataset Overview

## Construction of the Dataset
To facilitate this analysis, a simulated dataset was generated, covering a period from January 1, 2022 to July 19, 2022, totaling 200 days. The dataset features a daily frequency idnex created using pandas. The primary variable of interest, the 'Value' column, was design to illustrate a general upward trend using np.linspace. To add realism and mimic the fluctuation seen in real-world data, random noise was incorporated into this trend using np.random.normal (as shown in Figure 1). This approach allows for a controlled setting to test and compare the performance of different smoothing methods. 

![Figure 1]()

In addition to the 'Value' column, the dataset includes two two extra features, Feature 1 and Feature 2. Feature 1 consists of random integers, while Feature 2 contains random uniform values, provide a more comprehensive picture of the dataset structure (see Figure 2). These feature were used in the forecasting models in this report. The dataset preview shown in Figure 2 also displays the first five rows using the df.head() code. 

![Figure 2]()

The purpose of constructing this dataset was to create a simple yet realistic scenario for applying and comparing different exponential smoothing methods. By controlling the trend and noise components, this setup enables a clear and straightforward evaluation of each method's performance.