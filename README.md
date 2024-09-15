# Comparative Analysis Of Exponential Smoothing Methods For Time Series Forecasting By Jolly Madamedon

# Introduction
The primary purpose of this report is to analyse and compare different exponential smoothing methods for time series forecasting, using a dataset with a clear linear trend and random fluctuations. By applying these techniques to a simulated dataset, the report aims to evaluate their effectiveness in capturing the trend and managing noise. The analysis will highlight the strengths and limitations of each method, particularly in scenarios where seasonality is absent, and will provide guidance on selecting the most suitable forecasting approach for similar data patterns. 

# Dataset Overview

## Construction of the Dataset
To facilitate this analysis, a simulated dataset was generated, covering a period from January 1, 2022 to July 19, 2022, totaling 200 days. The dataset features a daily frequency idnex created using pandas. The primary variable of interest, the 'Value' column, was design to illustrate a general upward trend using np.linspace. To add realism and mimic the fluctuation seen in real-world data, random noise was incorporated into this trend using np.random.normal (as shown in Figure 1). This approach allows for a controlled setting to test and compare the performance of different smoothing methods. 

![Figure 1](https://github.com/Mojm4321/Python-Comparative-Analysis-of-Exponential-Smoothing-Methods-for-Time-Series-Forecasting/blob/main/1%20python.png)

Figure 1


In addition to the 'Value' column, the dataset includes two two extra features, Feature 1 and Feature 2. Feature 1 consists of random integers, while Feature 2 contains random uniform values, provide a more comprehensive picture of the dataset structure (see Figure 2). These feature were used in the forecasting models in this report. The dataset preview shown in Figure 2 also displays the first five rows using the df.head() code. 

![Figure 2](https://github.com/Mojm4321/Python-Comparative-Analysis-of-Exponential-Smoothing-Methods-for-Time-Series-Forecasting/blob/main/2%20python.png)

Figure 2


# Exploratory Data Analysis 
Before applying smoothing methods, it's crucial to understand the dataset's characteristics. This section provides a visual and statistical exploration of the data to reveal key patterns and trends.

## Visualing the Time Series
A time series plot of the 'Value' column was created to examine the overall trend and fluctuations (see Figure 3). The plot illustrated a clear linear upward trend through the period, accompannied by random flucationations due tot he introduced noise. This consistent upward trajectory indicates the presence of a trend component, making the data suitable for trend-capture methods like Holt's Linear Trend Model.

![Figure 3](https://github.com/Mojm4321/Python-Comparative-Analysis-of-Exponential-Smoothing-Methods-for-Time-Series-Forecasting/blob/main/6%20python.png)

Figure 3

## Summary Statistics
The summary statistics of the 'Value' column offer more insights into the data distribution (shown in Figure 4). With a mean of approximately 99.47 and a standard deviation of around 30.19, indicating some variability. The range of values, from a minimum of about 34.90 to a maximum of 158.03, further highlights the presence of fluctuations. These statistics confirm the dataset's inherent variability, indicating that the smoothing methods will need to manage this noise while accurately modeling the trend.

![Figure 4](https://github.com/Mojm4321/Python-Comparative-Analysis-of-Exponential-Smoothing-Methods-for-Time-Series-Forecasting/blob/main/7%20python.png)

Figure 4

## Moving Average
To smooth out short-term fluctuations and better visualise the underlying trend, a 10-day moving average (MA) was plotted alongside the original data (Figure 5). The MA (red line) provides a clearer view of the linear trend by reducing the impact of random moise. The visualisaiton supports the intial observation of an upward trend and indicates a lack of regular seasonality. Therefore, methods designed to capture trend rather than seasonal patterns will be more appropriate for this dataset.

![Figure 5](https://github.com/Mojm4321/Python-Comparative-Analysis-of-Exponential-Smoothing-Methods-for-Time-Series-Forecasting/blob/main/8%20python.png)

Figure 5

# Exponential Smoothing Methods

# Simple Exponential Smoothing 
The dataset was subsequently loaded into a DataFrame name df, consisting of 200 rows with columns including Date, Value, Feature1, and Feature 2. The primary focus was on  Date and Value columns, with Date serving as the the time index and Value was the target variable for modeling. Examining the structure of the DataFrame, as shown in Figure 6, confirmed the presence of key columns and ensured tha the data was corrected formatted for the analysis. 

![Figure 6](https://github.com/Mojm4321/Python-Comparative-Analysis-of-Exponential-Smoothing-Methods-for-Time-Series-Forecasting/blob/main/3%20python.png)


Figure 6

The Date column was then converted into a datetime format and set as the inxed of the DataFrame. This step is important for ensuring that the time series data is ordered correctly. Following this data preparation, the Simple Exponential Smoothing (SES) model was applied to the Value column. This was done by passing the Value series to the SimpleExpSmoothing function from the statsmodels library and subsequently calling the fit() method to train the model, as shown in Diagram 7.

![Figure 7](https://github.com/Mojm4321/Python-Comparative-Analysis-of-Exponential-Smoothing-Methods-for-Time-Series-Forecasting/blob/main/4%20python.png)


Figure 7

## Results from the Model
The summary of the fitted SES model, as presented in Diagram 8, provide key metrics for evaluating its performance. The smoothing level (alpha) was estimated at 0.22, indicating that the model handles a balance between recent observations and the overall historical pattern, avoiding overreaction to short term fluctuations in the data. This moderate responsiveness allows the model to smooth the series effectively.

The Sum of Squared Errors (SSE) was 21804.385, reflecting the total squared difference between the observed values and the fitted values. This metric suggest how well the model captures the data, with a lower SSE highlighting a closer fit.

Furthermore, the model selection criteria, Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) were reported as 942.31 and 948.90, respectively. This metric serves to evaluate the model quality by considering both the goodness of fit and model complexity, with a lower values implying a more efficient model.


![Figure 8](https://github.com/Mojm4321/Python-Comparative-Analysis-of-Exponential-Smoothing-Methods-for-Time-Series-Forecasting/blob/main/5%20python.png)


Figure 8

## Fitted Values
The fitted values were plotted against the original data to visually assess the model's performance. In this plot, the original data appears as a blue line, while the fitted values are represented by a red line. The model provides a smoothed line that follows the general level of the time series, capturing the overall pattern without reacting to minor variations, as shown in Figure 9.

![Figure 9](https://github.com/Mojm4321/Python-Comparative-Analysis-of-Exponential-Smoothing-Methods-for-Time-Series-Forecasting/blob/main/9%20Python.png)

Figure 9

## Forecast with Simple Exponential Smoothing
The model was used to forecast the next 90 days. These forecasted values were plotted alongside the original data and fitted values for comparison. As expected with SES, the forecast,  depicted as a green line extends as a flat line from the last fitted value. This indicates that SES assumes no trend in the data, projecting the future values at a constant level based on the most recent data points. While this characterstic makes SES a useful baseline model, it also illustrates that it may not be suitable for data with trends or seasonality, as illustrated in Figure 10.

![Figure 10](https://github.com/Mojm4321/Python-Comparative-Analysis-of-Exponential-Smoothing-Methods-for-Time-Series-Forecasting/blob/main/10%20python.png)


Figure 10