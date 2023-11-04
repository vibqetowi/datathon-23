
    adjusted_close = pd.read_csv(ROOT+'series/adjusted_close.csv',index_col=0)
    adjusted_close.index = pd.to_datetime(adjusted_close.index)
    # Uncomment the following line to test the notebook on a reduced number of 
    # products that span the entire makespan
    adjusted_close = adjusted_close.dropna(axis=1).iloc[:,:20]

    adjusted_close.head()