import numpy as np
import matplotlib.pyplot as plt
import sys

worker_utilization_file_name = sys.argv[1]

with open(worker_utilization_file_name, "r") as file_handle:
    data = map(int, file_handle.readlines())

indexes = np.arange(1, 6)
labels = ["Worker " + i for i in map(str, indexes)]
plt.bar(indexes, data, 0.4, tick_label=labels)
plt.xticks(fontsize=18)
# plt.title("Distribution of tasks across worker machines")
plt.ylabel("Number of tasks", fontsize=18)
plt.gca().yaxis.grid(True)
plt.show()
