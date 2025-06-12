from sklearn.datasets import load_wine
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#classify wine into 3 cultivars grown in specific regions of italy based on its chemical properties

wine = load_wine()
x = wine.data
y = wine.target

df = pd.DataFrame(x, columns=wine.feature_names)
df['cultivar'] = y

sns.pairplot(df, hue='cultivar')
plt.show()
