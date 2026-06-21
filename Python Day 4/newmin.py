import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Movie Dataset
movies = {
    "Movie": ["Avatar", "Inception", "Jawan", "3 Idiots", "Interstellar"],
    "Rating": [8.2, 8.8, 7.5, 8.4, 8.7],
    "Views_Million": [12, 15, 10, 18, 14]
}

# 1. Create DataFrame
df = pd.DataFrame(movies)

# 2. Display DataFrame
print("----- NETFLIX MOVIES DASHBOARD -----")
print("\nMovie Data:")
print(df)

# 3. Convert Rating column into NumPy array
ratings = np.array(df["Rating"])
print("\nRatings Array:")
print(ratings)

# 4. Statistics
print("\n----- Statistics -----")
print("Average Rating:", ratings.mean())
print("Highest Rating:", ratings.max())
print("Lowest Rating:", ratings.min())
print("Total Views:", df["Views_Million"].sum(), "Million")

# 5. Highest Rated Movie
highest_rated = df[df["Rating"] == df["Rating"].max()]
print("\nHighest Rated Movie:")
print(highest_rated)

# 6. Most Viewed Movie
most_viewed = df[df["Views_Million"] == df["Views_Million"].max()]
print("\nMost Viewed Movie:")
print(most_viewed)

# 7. Movies with Rating > 8
print("\nMovies with Rating > 8:")
print(df[df["Rating"] > 8])

# 8. Sort by Rating Descending
print("\nMovies Sorted by Rating:")
print(df.sort_values(by="Rating", ascending=False))

# 9. Create Popularity Column
df["Popularity"] = df["Rating"] * df["Views_Million"]

# 10. Display Updated DataFrame
print("\nUpdated DataFrame:")
print(df)

# 11. Movie with Highest Popularity
most_popular = df[df["Popularity"] == df["Popularity"].max()]
print("\nMovie with Highest Popularity:")
print(most_popular)

# 12. Bar Chart - Ratings
plt.figure(figsize=(8,5))
plt.bar(df["Movie"], df["Rating"])
plt.title("Netflix Movie Ratings")
plt.xlabel("Movies")
plt.ylabel("Ratings")
plt.show()

# 13. Bar Chart - Views
plt.figure(figsize=(8,5))
plt.bar(df["Movie"], df["Views_Million"])
plt.title("Netflix Movie Views")
plt.xlabel("Movies")
plt.ylabel("Views (Million)")
plt.show()

# 14. Add New Movie
new_movie = {
    "Movie": "KGF Chapter 2",
    "Rating": 8.6,
    "Views_Million": 16
}

df.loc[len(df)] = [
    new_movie["Movie"],
    new_movie["Rating"],
    new_movie["Views_Million"],
    new_movie["Rating"] * new_movie["Views_Million"]
]

# 15. Recalculate Statistics
print("\n----- After Adding New Movie -----")
print(df)

print("\nNew Average Rating:", df["Rating"].mean())
print("New Highest Rating:", df["Rating"].max())
print("New Lowest Rating:", df["Rating"].min())
print("New Total Views:", df["Views_Million"].sum(), "Million")

# Bonus: Pie Chart
plt.figure(figsize=(7,7))
plt.pie(
    df["Views_Million"],
    labels=df["Movie"],
    autopct="%1.1f%%"
)
plt.title("Share of Total Movie Views")
plt.show()