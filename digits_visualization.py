from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()
#data stored in 2d array with numbers representing varying darkness
print(digits.data)

#set visualization as 2 rows of 5 
fig, axes = plt.subplots(2, 5, figsize=(10, 5))
#loop through axes and flattened array
for i, ax in enumerate(axes.flatten()):
    ax.imshow(digits.images[i], cmap='gray')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Digit: {digits.target[i]}")
plt.show()
