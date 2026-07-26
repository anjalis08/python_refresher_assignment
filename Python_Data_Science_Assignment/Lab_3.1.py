import pandas as pd
import numpy as np

messy_data = {
    'StudentID': [1, 2, 3, 4, 2, np.nan, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Bob', np.nan, 'Eve'],
    'Score': [85, np.nan, 92, 78, np.nan, np.nan, 88]
}

df = pd.DataFrame(messy_data)
print("Original Data:")
print(df)

df=df.dropna(how='all')

mean_score = df['Score'].mean()

df['Score'] = df['Score'].fillna(mean_score)

df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)




