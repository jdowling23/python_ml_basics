import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris      #import built in iris dataset

iris = load_iris()

#create dataframe using iris dataset and features as column names
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df)
#identify target to classify
df['species'] = iris.target
#plot dataframe with colors determined by species
sns.pairplot(df, hue='species')
plt.show()
