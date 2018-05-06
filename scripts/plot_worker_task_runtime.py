import numpy as np
import matplotlib.pyplot as plt
import sys

worker_utilization_file_name = "overall_worker_task_runtime.txt"

with open(worker_utilization_file_name, "r") as file_handle:
    data = map(float, file_handle.readlines())

mean = np.mean(data)
std_dev = np.std(data)

print "Mean="+str(mean)+" Std_dev="+str(std_dev)

indexes = np.arange(1, len(data)+1)
labels = ["Worker " + i for i in map(str, indexes)]
#plt.bar(indexes, data, 0.4, tick_label=labels)
plt.bar(indexes, data, 0.4)
plt.xticks([])
#plt.xticks(fontsize=18)
plt.title("Worker Task Allocation")
plt.ylabel("Task runtime (seconds)", fontsize=18)
plt.xlabel("Workers", fontsize=18)
plt.gca().yaxis.grid(True)
plt.savefig('plots/worker_task_runtime.png')
# plt.show()
