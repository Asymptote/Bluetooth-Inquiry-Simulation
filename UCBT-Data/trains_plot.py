import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('32-log.txt')


#change clk, hex to dec
data.clk = data.clk.map(lambda x: int(x, 16))

#delete last unnamed col
del(data['Unnamed: 9'])


def appendFreqs(halfTrain, l):
	l.append(halfTrain.f1)
	l.append(halfTrain.f2)
	l.append(halfTrain.f3)
	l.append(halfTrain.f4)
	l.append(halfTrain.f5)
	l.append(halfTrain.f6)
	l.append(halfTrain.f7)
	l.append(halfTrain.f8)

freqsA1 = []
freqsB1 = []
freqsA2 = []
freqsB2 = []

i=2

halfTrain = data.iloc[8*i]
appendFreqs(halfTrain, freqsA1)
halfTrain = data.iloc[8*i+1]
appendFreqs(halfTrain, freqsA1)

halfTrain = data.iloc[8*i+2]
appendFreqs(halfTrain, freqsB1)
halfTrain = data.iloc[8*i+3]
appendFreqs(halfTrain, freqsB1)

halfTrain = data.iloc[8*i+4]
appendFreqs(halfTrain, freqsA2)
halfTrain = data.iloc[8*i+5]
appendFreqs(halfTrain, freqsA2)

halfTrain = data.iloc[8*i+6]
appendFreqs(halfTrain, freqsB2)
halfTrain = data.iloc[8*i+7]
appendFreqs(halfTrain, freqsB2)

f, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, sharex=True, figsize=(10,10))

ax1.hist(freqsA1, bins=range(0, 79, 1), color='r')
ax2.hist(freqsB1, bins=range(0, 79, 1), color='k')
ax3.hist(freqsA2, bins=range(0, 79, 1), color='r')
ax4.hist(freqsB2, bins=range(0, 79, 1), color='k')
ax5.hist(freqsA1+freqsA2+freqsB1+freqsB2, bins=range(0, 79, 1), color='b')

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)
ax5.grid(True)

ax1.set_title('Train A')
ax2.set_title('Train B')
ax3.set_title('Train A')
ax4.set_title('Train B')
ax5.set_title('Overall')
ax5.set_ylim([0,4])

f.subplots_adjust(hspace=.5)

plt.xlabel("Frequencies in Train A&B")
plt.ylabel("Frequency")
plt.savefig("rand_2.png",dpi=144)
#plt.show()
	
'''
plt.hist(all_freqs, bins=range(0, 79, 1))
#plt.title("Frequency Histogram\n Master traversed trains 32 times 32x(ABAB)")
plt.title("Frequency Histogram\n One Random Traversal 1 x (ABAB)")
plt.xlabel("Frequencies in Train A&B")
plt.ylabel("Frequency")
#plt.ylim([0,70])
plt.ylim([0,4])
plt.savefig("rand_0.png",dpi=144)
'''