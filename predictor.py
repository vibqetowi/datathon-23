import numpy as np 
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures

def polynomial_regression(past_prices):
    """
        Fits a 3d degree polynomial for each asset and returns the predicted value
    """
    past_prices.index = pd.to_datetime(past_prices.index)

    models={}

    # Fitting a 3d degree polynomial for each asset
    for c in past_prices.columns:
        x=past_prices[[c]]
        xp = PolynomialFeatures(degree=3).fit_transform(np.arange(len(x)).reshape((len(x),1)))
        model = sm.OLS(x.values, xp).fit()
        models[c] = model

    # Returning the next value of each polynomial
    return pd.DataFrame({k:v.predict(PolynomialFeatures(degree=3).fit_transform(np.array([len(x)]).reshape((1,1)))) for k,v in models.items()})/past_prices.iloc[-1]

if __name__ == "__main__":
    ROOT='./kaggle/input/dt23-test/'
    adjusted_close = pd.read_csv(ROOT+'series/adjusted_close.csv',index_col=0)
    adjusted_close.index = pd.to_datetime(adjusted_close.index)
    # Uncomment the following line to test the notebook on a reduced number of 
    # products that span the entire makespan
    adjusted_close = adjusted_close.dropna(axis=1).iloc[:,:20]

    print(adjusted_close.head())

    predicted_df = polynomial_regression(adjusted_close)

    print(predicted_df.head())