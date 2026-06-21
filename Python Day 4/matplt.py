import matplotlib.pyplot as plt

players = ['Player A', 'Player B', 'Player C', 'Player D']
goals = [10, 15, 7, 12]
plt.bar(players, goals)
plt.xlabel('Players')
plt.ylabel('Goals')
plt.title('Player Goals')
plt.show()
