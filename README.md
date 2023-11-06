## Project Overview
The purpose of this project was to create a trading algorithm that could operate within a specified historical period (2000-2015) with the goal of optimizing ROI. The strategy was constrained to include 80-120 stocks from a pre-selected pool of 304 S&P 500 stocks, rebalance daily, and avoid the use of future information.

An innovative approach was taken by leveraging the correlation between industry performance and the S&P 500 index's daily movements. The algorithm was designed to prefer industries with a higher correlation on green days and a lower correlation on red days.

## Industry Correlation Analysis
The industry_correlations script was developed to calculate the daily percentage return for each industry and the S&P 500, separate the returns into green and red days based on the S&P 500's performance, and calculate the correlation coefficients for each scenario.

Here is a breakdown of the script's functionality:

Data Import: Industry data is imported and timestamped for accurate analysis.
Return Calculation: Daily returns are computed for both the industry and S&P 500.
Day Classification: Days are classified as green or red based on S&P 500 performance.
Correlation Calculation: Correlation coefficients for green and red days are calculated and stored.
Industry Selection: Industries are selected based on the linear regression model fitting green-day correlation against red-day correlation, prioritizing those with the highest green-day correlation and furthest below the linear fit.
What Was Envisioned But Not Implemented
LSTM Model
The plan was to incorporate a Long Short-Term Memory (LSTM) model to take into account the industry discriminations when making predictions. This would have potentially added a more refined and predictive aspect to the trading algorithm.

## Cumulative Performance
A cumulative percent performance was calculated for individual S&P stocks versus the S&P 500 index, with the intent to inform stock selection through a moving average crossover strategy.

## What Went Wrong
# RNN Integration Issues
The project encountered challenges with the integration of Recurrent Neural Networks (RNNs), particularly due to a knowledge gap that made the implementation unfeasible within the constraints and timeframe of the challenge.

# Technical Hurdles
There were difficulties in optimizing for alpha, accounting for trading fees, and adhering to the fundamental constraints set out by the challenge. This resulted in the project not reaching its full potential technically.

# Learning Outcomes
Despite the setbacks, this project served as an important educational journey, providing insight into portfolio management and machine learning.