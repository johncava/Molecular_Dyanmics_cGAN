##
# Plotter
##

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import glob
import numpy as np

files = glob.glob('./*.dat')
files = [(float(f.split('gen')[-1].split('.dat')[0]), f) for f in files]
files.sort(key = lambda x: x[0])

files = [f[1] for f in files]
#print(files)

'''
fig, subs = plt.subplots(1, 4,sharex=True, sharey=True, figsize = (8,4))
#print(subs)
for i, (file_, sub) in enumerate(zip(files,subs)):
    #print(sub)
    data = []
    with open(file_,'r') as f:
        for line in f:
            item = line.strip('\n').split(' ')[1]
            item = float(item)
            #print(item)
            data.append(item)
    sub.plot(list(range(len(data))), data)
    sub.set_ylim([3, 8])
    sub.set_ylabel('RMSD')
    sub.set_xlabel('Frame Number')

# set the spacing between subplots
plt.subplots_adjust(wspace=0.8)

plt.savefig('rmsd.png')
'''

plt.rcParams['font.size'] = '16'

for i, file_ in enumerate(files):
    #print(sub)
    data = []
    with open(file_,'r') as f:
        for line in f:
            item = line.strip('\n').split(' ')[1]
            item = float(item)
            #print(item)
            data.append(item)
    plt.figure()
    plt.plot(list(range(len(data))), data)
    plt.ylim([3, 8])
    plt.ylabel('RMSD')
    plt.xlabel('Frame Number')
    plt.savefig('rmsd'+str(i)+'.png')