import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# sample data
data = {
    "A":[1,2,3,4,5],
    "B":[5,4,3,2,1],
    "C":[2,3,4,5,6]
}

df = pd.DataFrame(data)

# calculating the corelation matrix
corelation_matrix = df.corr()

# creating a heat map using seaborn
plt.figure(figsize=(5, 6))
sb.heatmap(corelation_matrix, annot = True, cmap = "coolwarm", linewidths=.5)
plt.title("Corelation matrix")
plt.show()