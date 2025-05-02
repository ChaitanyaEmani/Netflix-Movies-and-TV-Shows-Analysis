import pandas as pd

df = pd.read_csv("netflix_titles.csv")
df.head()
df.info()
df.isnull().sum()
df

# data cleaning
df.drop_duplicates(inplace=True)
df

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df, x='type')
plt.title("Content Type Distribution")

# Filter data for years 2000 to 2021
filtered_df = df[(df['release_year'] >= 2000) & (df['release_year'] <= 2021)]

# Group and plot
filtered_df.groupby(['release_year', 'type']).size().unstack().plot(kind='bar', figsize=(12, 6))
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.title("Movies vs TV Shows (2000–2021)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Top countries
df['country'].value_counts().head(10).plot(kind='barh')
plt.title("Top Countries with Netflix Content")


# Top genres
df['listed_in'].str.split(', ', expand=True).stack().value_counts().head(10).plot(kind='bar')
plt.title("Top Genres on Netflix")

#Top Directors

df['director'].value_counts().dropna().head(10).plot(kind='barh')
plt.title("Top 10 Directors")
plt.xlabel("No of movies or shows they directed")
plt.ylabel("Directors")
plt.tight_layout()

