import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab

#np.random.seed(0)

#mu = 200
#sigma = 25
n_bins = 50
#x = np.random.normal(mu, sigma, size=10)

runtime_file = open("task_runtime_output.txt", 'r')
data = runtime_file.readlines()

x = []
for line in data:
    x.append(float(line.strip('\n'))*1000)
mu = np.mean(x)
sigma = np.std(x)
#print mu, sigma

fig, ax = plt.subplots(figsize=(8, 4))

# plot the cumulative histogram
n, bins, patches = ax.hist(x, n_bins, normed=1, histtype='step', cumulative=True)

# Add a line showing the expected distribution.
y = mlab.normpdf(bins, mu, sigma).cumsum()
y /= y[-1]

ax.plot(bins, y, 'k--', linewidth=1.5,)

# Overlay a reversed cumulative histogram.
#ax.hist(x, bins=bins, normed=1, histtype='step', cumulative=-1, label='Reversed emp.')

# tidy up the figure
ax.grid(True)
ax.legend(loc='right')
ax.set_title('Task Runtime CDF')
ax.set_xlabel('Task runtime (milliseconds)')
ax.set_ylabel('')

plt.show()

