import sys
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

task_durations_file = sys.argv[1]
data = []
with open(task_durations_file, "r") as task_runtime_file:
    data = map(float, task_runtime_file.readlines())

bin_edges = stats.mstats.mquantiles(data, np.linspace(0.0, 1.0, num=1001))
# print bin_edges

fig, ax = plt.subplots(figsize=(8, 4))
# plot the cumulative histogram
n, bins, patches = ax.hist(data, bins=bin_edges, density=True, histtype='step',
                           cumulative=True, color="red", linewidth=2.0)

# tidy up the figure
ax.grid(True)
# ax.set_title('Cumulative Frequency Distribution of Task Runtimes')
# ax.set_ylabel('Likelihood of occurrence', fontsize=18)
yinterval = [np.round(i, 1) for i in np.linspace(0, 1, num=11)]
xinterval = [0.05, 0.1, 0.2, 0.3, 0.4, 0.6]
ax.set_xscale('log')
ax.set_xlim(min(data), 1)
ax.set_yticks(yinterval)
ax.set_yticklabels(yinterval, fontsize=18)
ax.set_xticks(xinterval)
ax.set_xticklabels(map(int, 1000*np.array(xinterval)), rotation=45, fontsize=18)
ax.set_xlabel('Task runtime (milliseconds)', fontsize=18)

plt.show()
