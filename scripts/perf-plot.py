#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss

fig, ax = plt.subplots()

# ax.set_xscale("log", basex=3)
# ax.set_yscale("log", basey=10)

def normalize(data, x):
    data2 = [t/x for t in data]
    return data2


data_30_4 = [4.42426 , 4.67012 , 4.4859 , 4.4272 , 4.56382,  4.67012]# [4, 5, 3, 4, 4]
# data_30_4 = normalize(data_30_4, 4.0 * (5.0/60))

data_10_4 = [4.11 , 4.076 , 4.034 , 3.89 , 3.862]# [1, 2, 2, 2, 1]
# data_10_4 = normalize(data_10_4, 4.0 * (5.0/60))

data_3_4 = [3.602 , 3.671 , 3.464 , 3.437 , 3.4627]
# data_3_4 = normalize(data_10_4, 4.0 * (20.0/60))

data_30_2 = [4.49381 , 4.637 , 4.69931 , 4.62337 , 4.617]# [3, 2, 3, 2, 2] #In 2 minutes
# data_30_2 = normalize(data_30_2, 2.0 * (2.0/60))

data_10_2 = [4.02693, 4.03921 , 4.06168 , 4.12634 , 4.0932] # [8, 7, 5, 9, 8, 9]
# data_10_2 = normalize(data_10_2, 2.0 * (5.0/60))

data_3_2 = [ 3.75932 , 3.6513 , 3.424 , 3.554 , 3.536]
# data_3_2 = normalize(data_3_2, 2.0 * (5.0/60))

data_4 = [data_3_4, data_10_4, data_30_4]
data_2 = [data_3_2, data_10_2, data_30_2]

#print data_30_2, data_10_2, data_3_2


def mean_arr(data):
    mean = [np.mean(np.array(x)) for x in data]
    return mean

def stddev_arr(data):
    stddev = [np.std(np.array(x)) for x in data]
    return stddev


#N = len(mean)

width = 0.28       # the width of the bars: can also be len(x) sequence

color1 = '#e06c0d' #(1.0,0.5,0.62)
color2 = '#af0505' #'#028413' #(0.2588,0.4433,1.0)
color3 = '#999999' #'#d62728'



pcolor = '#0e326d'

print mean_arr(data_2)

'''
plt.plot(np.arange([0,1,2]), mean_arr(data_2), ':', color=pcolor,  lw=3.0,  
        marker='x', mew = 3.0, markersize = 10,
        markerfacecolor='none', markeredgecolor=pcolor,
        dash_capstyle='round', label='2 VMs')#, yerr = stddev_arr(data_2))
'''

#plt.errorbar([3,10,30], mean_arr(data_2), [1,1,1])
# plt.plot([3,10,30], np.array([3.24, 26, 324]), ':', color=pcolor,  lw=1.0, marker='x', mew = 1.0, markersize = 7, markerfacecolor='none', markeredgecolor=pcolor, dash_capstyle='round', label="2 VMs predicted") #, yerr = stddev_arr(data_2))


def get_CI(ci, data):
    mean = mean_arr(data)
    stddev = stddev_arr(data)
    data_df = [len(d)-1 for d in data]
    yerr=ss.t.ppf(ci, data_df)*stddev
    return yerr

#plt.errorbar([3,10,30], mean_arr(data_2), get_CI(0.95, data_2), color=pcolor,  lw=2.0,  
#        dash_capstyle='round', label='2 VMs')


plt.errorbar([3,5,10], mean_arr(data_2), stddev_arr(data_2), color=pcolor,  lw=2.0,  
        dash_capstyle='round', label='Ray')


pcolor = '#028413'
plt.errorbar([3,5,10], mean_arr(data_4), stddev_arr(data_4), color=pcolor, ls="--",  lw=2.0,  
        dash_capstyle='round', label='Fulcrum')

#plt.errorbar([3,10,30], mean_arr(data_4), get_CI(0.95, data_4), color=pcolor,  lw=2.0,  
#        dash_capstyle='round', label='4 VMs')

print "CI: ", get_CI(0.95, data_2), get_CI(0.95, data_4)

# plt.plot([10,30], np.array([3.5, 171.3]), ':', color=pcolor,  lw=1.0, marker='o', mew = 1.0, markersize = 7, markerfacecolor='none', markeredgecolor=pcolor, dash_capstyle='round', label="4 VMs predicted") #, yerr = stddev_arr(data_2))

'''
plt.plot([3,10,30], mean_arr(data_4), ':', color=pcolor,  lw=3.0,  
        marker='|', mew = 3.0, markersize = 10,
        markerfacecolor='none', markeredgecolor=pcolor,
        dash_capstyle='round', label='4 VMs')#, yerr = stddev_arr(data_2))
'''

def string(x):
    if x >= (1000 * 1000 * 1000):
        return str(x/(1000*1000*1000)) + 'B'    
    #elif x >= (1000 * 1000):
    #    return str(x/(1000*1000)) + 'M'
    elif x >= 1000:
        return str(x/1000) + 'K'
    else:
        return str(x)



plt.ylabel('Average iteration time in seconds', fontsize=14)
plt.xlabel('Number of workers', fontsize=14)
#plt.title('HSS: weak scaling')
#data = [class_, launch, countdown, shuttle, gif, get, dot]
# plt.xticks((3,5,10), (3,5,10))
# plt.yticks([1,5,10], (1,5,10))
#plt.xticks(ind, ("class\n" + string(class_[0]), "launch\n" + string(launch[0]), "countdown\n" + string(countdown[0]), "shuttle\n" + string(shuttle[0]), "gif\n" + string(gif[0]), "get\n" + string(get[0]), "dot\n" + string(dot[0])))
#plt.yticks(np.arange(0, 81, 10))
plt.ylim(ymin=3.2, ymax=4.8)
plt.xlim(xmin=2, xmax=11)
#leg = plt.legend((p3[0], p2[0], p1[0]), ('data exchange', 'histogramming','local sort'))
leg = plt.legend(bbox_to_anchor=(0.06, 0.9), borderaxespad=0, loc=2, numpoints=3, handlelength=5,prop={'size':12})
#leg.get_frame().set_linewidth(0.0)
#ax.set_axisbelow(True)
#plt.xticks(rotation=45, fontsize=8)
ax.yaxis.grid()
plt.show()

'''
import numpy as np
import pylab as P
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import LogLocator

fig, ax = plt.subplots()

#
# The hist() function now has a lot more options
#
#mu, sigma = 200, 25
#x = sigma*P.randn(4,3)


#print x[0], x[1], x[2], x[3], len(x)
counts, bins, patches = plt.hist(x, 4, histtype='bar', stacked=True)
plt.grid(linestyle=':', linewidth=1, color='grey')
#P.ylim(0, 1.05)
#ax.xaxis.set_ticks()
ax.xaxis.set_ticks(bins+10)
ticklabelcolor = 'black'
xticks = ["2048", "8192", "32K", "128K"]
ax.set_xticklabels(xticks, color=ticklabelcolor)

plt.show()


ticklabelcolor = 'black'
logp = np.arange(1,19,1)
p = np.array([2**i for i in logp])
#ax.xaxis.set_ticks(p[1::2])
#xticks =np.array([2**x for x in logp[1::2]])
#xticks = np.array([string(x) for x in xticks])
'''

