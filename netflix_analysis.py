import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

# load dataset
df = pd.read_csv("netflix_titles.csv")

# Content type distribution
content_count = df['type'].value_counts()

plt.figure()
content_count.plot(kind='pie', autopct='%1.0f%%')
plt.title("Netflix Content Distribution")
plt.ylabel("")
plt.savefig("charts/content_distribution.png")

# Content growth over years
year_count = df['release_year'].value_counts().sort_index()

plt.figure()
year_count.plot(kind='line')
plt.title("Netflix Content Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.savefig("charts/content_growth.png")

print("Charts created successfully!")

# Top Genres
genre_count = df['listed_in'].str.split(',', expand=True).stack().value_counts().head(10)

plt.figure(figsize=(8,5))
genre_count.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/top_genres.png")


# Top Countries
country_count = df['country'].str.split(',', expand=True).stack().value_counts().head(10)

plt.figure(figsize=(8,5))
country_count.plot(kind='bar')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/top_countries.png")