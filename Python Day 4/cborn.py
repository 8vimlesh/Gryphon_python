import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

players = {
    "Players": ["Messi", "Mbappe", "Haaland", "Ronaldo", "Kane"],
    "goals": [5, 8, 5, 6, 7],
    "assists": [4, 4, 3, 6, 7]
}
df = pd.DataFrame(players)

sns.barplot(x="Players", y="goals", data=df)
plt.show()

sns.lineplot(x="Players", y="assists", data=df)
plt.show()
