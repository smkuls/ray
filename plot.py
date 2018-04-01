import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = []
with open("numbers/data2.txt", "r") as task_runtime_file:
    data = map(float, task_runtime_file.readlines())

bin_edges = stats.mstats.mquantiles(data, np.linspace(0.0, 1.0, num=11))
# print bin_edges

fig, ax = plt.subplots(figsize=(8, 4))
# plot the cumulative histogram
n, bins, patches = ax.hist(data, bins=bin_edges, density=True, histtype='step',
                           cumulative=True, color="red")

# tidy up the figure
ax.grid(True)
ax.set_title('Cumulative frequency distribution of task runtimes')
ax.set_ylabel('Likelihood of occurrence')
yinterval = [np.round(i, 1) for i in np.linspace(0, 1, num=11)]
xinterval = [0.1, 0.2, 0.3, 0.4, 5, 10, 20]
ax.set_xscale('log')
ax.set_yticks(yinterval)
ax.set_yticklabels(yinterval)
ax.set_xticks(xinterval)
ax.set_xticklabels(map(int, 1000*np.array(xinterval)), rotation=15)
ax.set_xlabel('Task runtime (milliseconds)')

plt.show()
