import os
import glob

if not os.path.exists('plots'):
    os.makedirs('plots')

files = glob.glob('plot_*.py')

for file in files:
	os.system('python '+file)