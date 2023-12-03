import matplotlib.pyplot as plt
import numpy as np

data = [
    [2.79, 1.95, 2.98, 4.57, 3.77],
    [1.66, 2.57, 2.71, 2.73, 4.23],
    [2.19, 2.11, 2.24, 4.11, 3.91],
    [1.86, 1.73, 2.93, 8.52, 7.28],
    [2.06, 3.02, 2.52, 11.45, 8.21]
]

means = [np.mean(set_data) for set_data in data]
std_devs = [np.std(set_data) for set_data in data]

plt.boxplot(data, labels=['Ammo', 'Health', 'Gamestate', 'Enemies', 'Objective'])
plt.title('Survey Response Times')
plt.xlabel('Identification')
plt.ylabel('Response Times (Seconds)')

for i in range(len(means)):
    plt.text(i + 1, max(data[i]), f'Mean: {means[i]:.2f}\nStd Dev: {std_devs[i]:.2f}', ha='center', va='bottom', color='red')

plt.show()
