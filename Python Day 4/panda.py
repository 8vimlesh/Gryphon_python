#Pandas is a powerful Python library used for data analysis, data manipulation, and data cleaning.
#It provides easy-to-use data structures and functions for handling structured data.


import pandas as pd

fifa = {

    "players": ["ronaldo", "messi", "mbappe " , "haaland"],
    "goals": [700, 800, 300, 200]
}

df = pd.DataFrame(fifa)
print ("Total Goals : " , df["goals"].sum())
print ( "Avg Goals :" , df["goals"].mean()) 
print ("highest Goal :" , df["goals"].max())
print ("\nTop Scorer")
print (df[df["goals"] == df["goals"].max()])
