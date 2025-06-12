#linnerud dataset
from sklearn.datasets import load_linnerud
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load data set
linnerud = load_linnerud()

#assign feature and target data
x = linnerud.data
y = linnerud.target
print(x)
print(y)

#features = chin-ups, sit-ups, jumps
df = pd.DataFrame(x, columns=linnerud.feature_names)
#targets = weight, waists, pulse
df_targets = pd.DataFrame(y, columns=linnerud.target_names)

sns.pairplot(df_targets)
plt.show()
