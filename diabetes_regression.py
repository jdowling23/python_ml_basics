from sklearn.datasets import load_diabetes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

diabetes = load_diabetes()

#create data frame from diabetes data set
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
print(df)

df['progression'] = diabetes.target
sns.pairplot(df)
plt.show()
