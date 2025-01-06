# Gold Price Clustering using K-Means

## Project Description:
This project uses K-Means clustering to analyze historical gold prices and categorize them into different clusters based on the price trends, moving averages, and volatility.

## Dataset:
The dataset used in this project is the "Gold Prices" dataset from Kaggle, which contains monthly gold price data from 1950 to 2020.

## Steps Involved:
1. **Data Preprocessing**: 
   - Handled missing values by using backward fill for moving averages and filling missing volatility values with zeros.
2. **Feature Scaling**: 
   - Used `StandardScaler` to scale numerical features before applying K-Means clustering.
3. **Clustering**: 
   - Applied the K-Means algorithm to partition the data into 3 clusters.
4. **Visualization**: 
   - Visualized the clusters using scatter plots to observe patterns in gold prices.

## Key Concepts:
- **K-Means Clustering**
- **Feature Scaling**
- **Data Preprocessing**

## Result:
The dataset was successfully clustered into 3 groups, providing insights into periods of price stability, high volatility, and consistent growth.

## How to Run:
1. Clone this repository.
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
