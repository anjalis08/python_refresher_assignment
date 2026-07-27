import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = np.random.rand(100, 5)

df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

correlation = df.corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')

plt.title("Correlation Heatmap")
plt.show()