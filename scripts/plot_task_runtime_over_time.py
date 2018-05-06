import numpy as np
import matplotlib.pyplot as plt
import sys

worker_utilization_file_name = "task_runtime_output.txt"

with open(worker_utilization_file_name, "r") as file_handle:
    y = map(float, file_handle.readlines())

N = 500
def running_mean(x, N):
    cumsum = np.cumsum(np.insert(y, 0, 0)) 
    return ((cumsum[N:] - cumsum[:-N])*1000 / N)

ynew = running_mean(y, N)

plt.plot(np.arange(1, len(ynew)+1), ynew) 
plt.xticks([])
plt.title("Task Runtime Durations Over Time")
plt.ylabel("Task runtime (milliseconds)", fontsize=18)
plt.xlabel("Time", fontsize=18)
plt.show()
