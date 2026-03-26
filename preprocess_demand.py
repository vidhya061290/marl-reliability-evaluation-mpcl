# preprocess_demand.py
# Illustrative script showing how restricted demand data is processed.
# The real dataset cannot be shared publicly due to municipal privacy agreements.

import pandas as pd
import numpy as np

def aggregate_and_normalize(df):
    """Example of how demand data would be aggregated and normalized."""
    df['total_demand'] = df.sum(axis=1)
    df['normalized'] = (df['total_demand'] - df['total_demand'].mean()) / df['total_demand'].std()
    return df[['normalized']]

# Example usage (commented out):
# df = pd.read_csv('restricted_demand.csv')
# processed = aggregate_and_normalize(df)
# processed.to_csv('aggregated_demand.csv', index=False)
