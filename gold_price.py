# -*- coding: utf-8 -*-
"""Gold_Price.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13Dh-GfUFONkAv58QpOXQSq7CzRLuwKA1
"""

!pip install pandas matplotlib seaborn plotly scikit-learn

import pandas as pd

# Load dataset
data = pd.read_csv('monthly_csv.csv')

# Preview the first few rows
print(data.head())

# Check the column names and data types
print(data.info())

# View basic statistics of the dataset
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Convert 'Date' to datetime and sort
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values('Date')

# Check for missing months
full_date_range = pd.date_range(start=data['Date'].min(), end=data['Date'].max(), freq='MS')
missing_dates = full_date_range.difference(data['Date'])

print("Missing Dates:", missing_dates)

# Drop duplicates if any
data = data.drop_duplicates()

# Fill missing prices (if necessary) using interpolation
data['Price'] = data['Price'].interpolate(method='linear')

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Price'], label='Gold Price')
plt.title('Gold Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Calculate daily percentage change
data['Daily Change (%)'] = data['Price'].pct_change() * 100

# Plot volatility over time
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Daily Change (%)'], label='Volatility', color='orange')
plt.title('Gold Price Volatility Over Time')
plt.xlabel('Date')
plt.ylabel('Daily Change (%)')
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('monthly_csv.csv')

# Convert 'Date' to datetime and sort
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values('Date')

# Handle missing values
data['Price'] = data['Price'].interpolate(method='linear')

# Preview the cleaned data
print(data.head())

# Plot raw data
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Price'], label='Gold Price')
plt.title('Gold Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Calculate moving averages
data['MA_3'] = data['Price'].rolling(window=3).mean()
data['MA_12'] = data['Price'].rolling(window=12).mean()

# Calculate monthly percentage change
data['Volatility'] = data['Price'].pct_change().abs() * 100

print(data[['Date', 'Price', 'MA_3', 'MA_12', 'Volatility']].tail())

from sklearn.preprocessing import MinMaxScaler

# Select features
features = ['MA_3', 'MA_12', 'Volatility']
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data[features])

print(data_scaled[:5])  # Preview scaled data

# Check for NaN values
print(data.isnull().sum())

# Check rows with NaN values
print(data[data.isnull().any(axis=1)])

# Fill NaNs for rolling averages (optional)
data['MA_3'] = data['MA_3'].fillna(method='bfill')  # Backward fill
data['MA_12'] = data['MA_12'].fillna(method='bfill')  # Backward fill

# Fill NaN for Volatility
data['Volatility'] = data['Volatility'].fillna(0)

# Confirm no more NaNs
print(data.isnull().sum())

print(pd.DataFrame(data_scaled).isnull().sum())

from sklearn.preprocessing import StandardScaler

# Select relevant columns for scaling
columns_to_scale = ['Price', 'MA_3', 'MA_12', 'Volatility']
data_scaled = data[columns_to_scale]

# Initialize the scaler
scaler = StandardScaler()

# Scale the data
data_scaled = scaler.fit_transform(data_scaled)

# Check for NaN values in scaled data
print(pd.DataFrame(data_scaled).isnull().sum())

from sklearn.cluster import KMeans

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(data_scaled)

# Preview cluster assignments
print(data[['Date', 'Price', 'Cluster']].tail())

import matplotlib.pyplot as plt

# Plot the clusters
plt.figure(figsize=(10, 6))
plt.scatter(data['Price'], data['MA_3'], c=data['Cluster'], cmap='viridis')
plt.title('K-Means Clustering of Gold Prices')
plt.xlabel('Price')
plt.ylabel('MA_3 (3-month Moving Average)')
plt.colorbar(label='Cluster')
plt.show()

print(f"Inertia: {kmeans.inertia_}")

from sklearn.metrics import silhouette_score

score = silhouette_score(data_scaled, data['Cluster'])
print(f"Silhouette Score: {score}")

cluster_profile = data.groupby('Cluster')[['Price', 'MA_3', 'MA_12', 'Volatility']].mean()
print(cluster_profile)

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

inertia_values = []
cluster_range = range(1, 11)

for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertia_values.append(kmeans.inertia_)

plt.plot(cluster_range, inertia_values, marker='o')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()