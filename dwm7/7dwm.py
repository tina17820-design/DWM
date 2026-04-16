import pandas as pd
import matplotlib.pyplot as plt

# Read CSV from SAME folder
df = pd.read_csv("student-por.csv")

print("File loaded successfully!")
print(df.head())

# Use final marks column
data = df["G3"].tolist()

# Discretization
min_val = min(data)
max_val = max(data)

k = 5
bin_width = (max_val - min_val) / k

bins = []
start = min_val

for i in range(k):
    end = start + bin_width
    bins.append((round(start,2), round(end,2)))
    start = end

print("\nBins:", bins)

# Histogram
plt.hist(data, bins=k)
plt.title("Histogram of Final Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
