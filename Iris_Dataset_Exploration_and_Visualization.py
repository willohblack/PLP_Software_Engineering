import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# --- Task 1: Load and Explore the Dataset ---

try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    print("First 5 rows of the dataset:")
    print(df.head())
    
    print("\nData types and missing values info:")
    print(df.info())
    
    print("\nChecking for missing values:")
    print(df.isnull().sum())
    
    # Since Iris dataset has no missing values, this is just for demo:
    # If missing values existed, you could fill or drop them:
    # df.fillna(method='ffill', inplace=True)  # or df.dropna(inplace=True)

except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# --- Task 2: Basic Data Analysis ---

# Basic statistics for numerical columns
print("\nBasic statistics:")
print(df.describe())

# Group by species and compute mean sepal length
grouped_means = df.groupby('species')['sepal length (cm)'].mean()
print("\nMean sepal length per species:")
print(grouped_means)

# Observations
print("\nObservation: Setosa species has smaller sepal length on average compared to Versicolor and Virginica.")

# --- Task 3: Data Visualization ---

sns.set(style="whitegrid")

# 1) Line chart: Since Iris isn't time-series, plot cumulative mean sepal length by index per species as a proxy
plt.figure(figsize=(8,5))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    cum_mean = subset['sepal length (cm)'].expanding().mean()
    plt.plot(subset.index, cum_mean, label=species)
plt.title("Cumulative Mean Sepal Length by Sample Index")
plt.xlabel("Sample Index")
plt.ylabel("Cumulative Mean Sepal Length (cm)")
plt.legend()
plt.show()

# 2) Bar chart: Average petal length per species
plt.figure(figsize=(6,4))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3) Histogram: Distribution of sepal width
plt.figure(figsize=(6,4))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4) Scatter plot: Sepal length vs Petal length colored by species
plt.figure(figsize=(7,5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep')
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()
