import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

players = {
    "Players": ["Messi", "Mbappe", "Haaland", "Ronaldo", "Kane"],
    "goals": [5, 8, 5, 6, 7],
    "assists": [4, 4, 3, 6, 7]
}

df = pd.DataFrame(players)

print("----- FIFA Dashboard -----")

print("\nPlayer Data:")
print(df)

print("\nTotal Goals:", df["goals"].sum())
print("Average Goals:", df["goals"].mean())
print("Highest Goals:", df["goals"].max())
print("Lowest Goals:", df["goals"].min())

top_scorer = df[df["goals"] == df["goals"].max()]

print("\nTop Scorer:")
print(top_scorer)

plt.bar(df["Players"], df["goals"])
plt.title("FIFA Player Goals")
plt.xlabel("Players")
plt.ylabel("Goals")
plt.show()