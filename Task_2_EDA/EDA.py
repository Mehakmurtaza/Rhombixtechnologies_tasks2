import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------
# STEP 1: Load the cleaned dataset
# ---------------------------------------------
df = pd.read_csv('Cleaned_Superstore.csv')

# ---------------------------------------------
# STEP 2: Basic statistical analysis
# ---------------------------------------------
# Calculating basic statistics for Sales
print("Mean Sales:", df['sales'].mean())
print("Median Sales:", df['sales'].median())
print("Maximum Sales:", df['sales'].max())
print("Minimum Sales:", df['sales'].min())


# ---------------------------------------------
# STEP 3: Outlier detection using boxplots
# ---------------------------------------------

# Boxen plot to visualize outliers in Sales
plt.figure()
sns.boxenplot(x=df['sales'])
plt.title("Outliers in Sales")
plt.xlabel("Sales")
plt.show()

# Box plot to visualize outliers in Profit
plt.figure()
sns.boxplot(x=df['profit'])
plt.title("Outliers in Profit")
plt.xlabel("Profit")
plt.show()

# ---------------------------------------------
# STEP 4: Correlation analysis
# ---------------------------------------------
# Calculating correlation between numerical variables
correlation = df[['sales', 'profit', 'quantity', 'discount']].corr()
print(correlation)

# Visualizing correlation using heatmap
plt.figure()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


# ---------------------------------------------
# STEP 5: Categorical analysis
# ---------------------------------------------
# Bar chart showing Sales by Category
plt.figure()
sns.barplot(x='category', y='sales', data=df)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()


# ---------------------------------------------
# STEP 6: Trend analysis over time
# ---------------------------------------------
# Grouping sales by year

df['order_date'] = pd.to_datetime(df['order_date'])
sales_by_year = df.groupby(df['order_date'].dt.year)['sales'].sum()

# Line chart showing sales trend over time
plt.figure()
sales_by_year.plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.show()


# ---------------------------------------------
# STEP 7: Distribution analysis
# ---------------------------------------------
# Histogram showing Sales distribution
plt.figure()
plt.hist(df['sales'], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

