# Objective:
Investigating the impact of interest rates on the housing market: use the Federal Reserve's interest rate data and home price data from sources like Zillow, Redfin, and the Fed's Case-Shiller home price index to study how changes in interest rates affect the housing market.

# Approach:
Cut it by ZIP code and see what the impact is in different parts of the country.
Create map visualization.
Try to forecast prices in different areas of the country.

# Questions:
1. How sensitive are home prices to changes in interest rates?
-->Plot interest rates against the HPI or normalized sale price over time to see if there is a correlation.
-->Plot by outlier zip codes

2. Is the relationship between interest rates and home prices different in different regions of the country?
   - Are there any time lags between changes in interest rates and changes in home prices?

3. How are house prices affected by recessions?
-->Plot the HPI or normalized sale price over time and mark the periods of recession to see if there is any correlation.

4. Create a model to predict future housing prices: use the federal interest rate data and dates of recessions to create a model to predict future housing prices.
BONUS: use machine learning time series analysis to develop a model that takes into account the effects of interest rates and economic cycles.

Other data to add: employment rates, inflation rates, GDP growth (from the feds?)

# Plan:
1. get:
    - price data by zip code over time
    - recession data
    - interest rate data (fed funds rate)
    analyze:
    - interest rates vs prices over time
    - interest rates vs price changes over time (need yearly price change data)

2. get: same as 1
analyze:
    - find outlier zip codes (higly and poorly impacted), discuss
    - plot data on a map

3. get:
    - recession data
analyze:
    - changes during recession vs not during recession
    - outliers by zip code (resilient zip codes vs sensitive ones)

4. get: data from above
analyze:
    - linear regression model for future house prices overall, by zip
    - predict house price by zip 5ys out under 1-3 fed rate scenarios
    - create time series ML model with scikit-learn?
    - add forecast values to map
