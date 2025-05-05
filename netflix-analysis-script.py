import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/Users/shiveshrajsahu/Desktop/PythonCodes/Projects to complete /netflix.csv')
print("\nStep 1 of the Business Case")
# Preview
print("\nFirst 5 rows:")
print(df.head())

# Basic structure
print("\nDataset Info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

# STEP 1: Define the Problem Statement + Analyze Basic Metrics (10 Points)
# What to do:
# 1. Write a summary of what you’re solving and what the dataset contains.
# 2. Write a summary of what you’re solving and what the dataset contains.
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")
print("\nColumn Names:")
print(df.columns.tolist())

# Code for Step 2
# Unique values per column
print("\nStep 2 of the Business Case")
print("\nUnique value count per column:")
print(df.nunique()) #Helps identify categorical features and
                    # columns that might be candidates for encoding or filtering.

# Convert to categorical
categorical_cols = ['type', 'director', 'cast', 'country', 'rating', 'listed_in']
for col in categorical_cols:
    df[col] = df[col].astype('category') #Saves memory by converting string-based
                                         # features with repeating values into a category data type.

# Check updated dtypes
print("\nUpdated data types after conversion:")
print(df.dtypes) #Confirms if the type conversion actually happened.

# Statistical Summary
print("\nStatistical Summary for All Columns:")
print(df.describe(include='all')) #Count of non-null values,
                                  # Most common category (top),
                                  # Number of unique values,
                                  # Mean, std, min, max for numeric columns

# Optional: memory usage
print("\nMemory Usage (Optimized):")
print(df.memory_usage(deep=True)) # Confirms how much memory each column is consuming.
                                  # Useful if dataset scales in production.

# Step 3: Data Cleaning & Preprocessing
# We want to see which columns have NaN (missing values):
print("\nStep 3: Data Cleaning & Preprocessing")
print("\nMissing values (pre-cleaning):")
print(df.isnull().sum())
#These are the columns we need to handle now.
print("\nThese are the columns we need to handle now.")

#We don’t want to lose good rows due to missing values in non-critical columns like
# director, cast, and country.
#Fill missing values in non-critical categorical fields with 'Unknown'
df['director'] = df['director'].cat.add_categories('Unknown').fillna('Unknown')
df['cast']     = df['cast'].cat.add_categories('Unknown').fillna('Unknown')
df['country']  = df['country'].cat.add_categories('Unknown').fillna('Unknown')

#Drop rows with missing values in essential fields (rating, duration, etc.)
df.dropna(inplace=True)

#Confirm no missing values remain
print("\n Missing values (post-cleaning):")
print(df.isnull().sum())

# Convert date_added to datetime
print("\nConvert date_added to datetime")
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

#Recheck types after all transformations
print("\n Final Data Types:")
print(df.dtypes)

#Remove duplicates if any
print("\nRemove duplicates if any")
df.drop_duplicates(inplace=True)

#Step 4: Visual Analysis – Univariate + Bivariate
print("\nStep 4: Visual Analysis – Univariate + Bivariate")

#To explore patterns in both continuous and categorical variables using visualization tools.
# This helps you understand the distribution of the data and potential relationships.

# Continuous Variable – release_year
print("\n Continuous Variable – release_year")
plt.figure(figsize=(10,5))
sns.histplot(df['release_year'], bins=30, kde=True)
plt.title("Distribution of Release Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.show()

# Categorical Variable – type
print("\n Categorical Variable – Content Type (TV Shows vs Movies)")
sns.countplot(data=df, x='type')
plt.title("TV Shows vs Movies")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Genre Analysis – Top 10 Genres
print("\n Categorical Variable – Top 10 Genres")
top_genres = df['listed_in'].str.split(', ').explode().value_counts().head(10)
top_genres.plot(kind='barh', title='Top 10 Genres')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()

#Boxplot: Content Age by Type

# Calculate content age
df['content_age'] = 2025 - df['release_year']

# Plot boxplot: Age of content by type (Movie vs TV Show)
plt.figure(figsize=(10, 5))
sns.boxplot(x='type', y='content_age', data=df)
plt.title('Content Age Distribution by Type')
plt.xlabel('Type')
plt.ylabel('Content Age (in years)')
plt.show()

#Correlation Heatmap
# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df[['release_year', 'content_age']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()



#Step 5: Feature Engineering
print("\n Step 5: Feature Engineering")

#1. Content Age
print("\n Content Age")
from datetime import datetime

df['content_age'] = datetime.now().year - df['release_year']

#2. Number of Genres
print("\n Number of Genres")
df['num_genres'] = df['listed_in'].apply(lambda x: len(str(x).split(', ')))

#3. Has Multiple Countries
print("\n Has Multiple Countries")
df['multi_country'] = df['country'].apply(lambda x: ',' in str(x))

#After Adding Features:
#check results using:
print("\nAfter Adding Features:")
print("\ncheck results using:")
print(df[['release_year', 'content_age', 'num_genres', 'multi_country']].head())
















