import matplotlib.pyplot as plt
import numpy as np

questions = ['Overwhelming?', 'UI Readable?', 'Font Readable?', 'Congruent?', 'Looks Good?', 'Familiar?', 'Enjoyable?']
responses = np.array([
    [2, 1, 2, 2, 4],
    [4, 3, 4, 4, 3],
    [2, 3, 2, 1, 2],
    [4, 3, 3, 2, 3],
    [3, 2, 3, 3, 3],
    [5, 5, 4, 4, 5],
    [3, 4, 4, 4, 2]
])

means = np.mean(responses, axis=1)
std_devs = np.std(responses, axis=1)

bar_width = 0.15
index = np.arange(len(questions))

fig, ax = plt.subplots()
colors = ['#000000', '#003333', '#006666', '#009999', '#00CCCC']

for i in range(5):
    ax.bar(index + i * bar_width, responses[:, i], bar_width, label=f'Response {i + 1}', color=colors[i])

for i, (mean, std_dev) in enumerate(zip(means, std_devs)):
    ax.text(index[i] + bar_width * 2, max(responses[i]) + 0.2, f'Mean: {mean:.2f}\nStd Dev: {std_dev:.2f}', color='red', ha='center')

ax.set_xlabel('Questions')
ax.set_ylabel('Responses')
ax.set_title('Grouped Bar Chart of Responses')
ax.set_xticks(index + bar_width * 2)
ax.set_xticklabels(questions)


plt.show()
