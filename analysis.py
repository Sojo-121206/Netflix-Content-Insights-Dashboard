import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\Admin\OneDrive\Projects\Netflix_project\netflix_titles.csv")
# df = pd.read_csv("netflix_titles.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing values
df['director'].fillna("Unknown", inplace=True)
df['cast'].fillna("Unknown", inplace=True)
df['country'].fillna("Unknown", inplace=True)
df['rating'].fillna("Not Rated", inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Create new column
df['year_added'] = df['date_added'].dt.year

# Clean genre
df['listed_in'] = df['listed_in'].str.strip()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDataset Shape:", df.shape)

# Save cleaned file
df.to_csv("cleaned_netflix.csv", index=False)

print("\nData cleaning completed! ✅")
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# EDA START
# ---------------------------

print("\n🔹 Movies vs TV Shows:\n")
print(df['type'].value_counts())

# Bar chart
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.show()


# ---------------------------
# Content added over years
# ---------------------------

print("\n🔹 Content added over years:\n")
print(df['year_added'].value_counts())

df['year_added'].value_counts().sort_index().plot()
plt.title("Content Growth Over Years")
plt.show()


# ---------------------------
# Genre Analysis
# ---------------------------

# Split genres
df['listed_in'] = df['listed_in'].str.split(',')

# Explode
df_exploded = df.explode('listed_in')

# Count genres
genre_count = df_exploded['listed_in'].value_counts()

print("\n🔹 Top Genres:\n")
print(genre_count.head(10))

# Plot
genre_count.head(10).plot(kind='bar')
plt.title("Top 10 Genres")
plt.show()