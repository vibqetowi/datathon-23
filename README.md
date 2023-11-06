## Assumptions

start value of Portfolio is 1M

## Weights

Alpha score matters a lot

As constraints are added, alpha score diminishes
Constraints are necessary for diversification
While alpha score might decrease, Active Risk will decrease. Goal: 3-4%

Alpha Score | Stock Weight Index | Constraints XYZ > Portfolio Weight

Possible Constraints :

- Industry
- Country
- Carbon Footprint

Axioms: Resources\Optimization_Axioms.PNG

## LSTM

We tried to use long short-term memory networks (LSTM), which is a variety of recurrent neural networks (RNNs) that is able to learn long-term dependencies and do predictions. In this case, we have stock data such as open, close, high, low, along with commonly used indicators such as RSI, MACD, Moving averages. With these data and dependencies, we are able to feed it to our machine learning model, in order to get the closed price of the next day with data and indicators of previous day. We are able to produce a prediction graph, but the problem is that there is an increasing margin of error as the time increased. Therefore resulting in a pretty good looking graph, but in reality it wasn't accurate enough because of a significant amount of errors.
