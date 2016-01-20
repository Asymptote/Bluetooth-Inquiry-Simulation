import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('32-log.txt')


#change clk, hex to dec
data.clk = data.clk.map(lambda x: int(x, 16))

#delete last unnamed col
del(data['Unnamed: 9'])


all_freqs = []
for i in range(0,32):
	for j in range(0,8):
		halfTrain = data.iloc[8*i+j]

		all_freqs.append(halfTrain.f1)
		all_freqs.append(halfTrain.f2)
		all_freqs.append(halfTrain.f3)
		all_freqs.append(halfTrain.f4)
		all_freqs.append(halfTrain.f5)
		all_freqs.append(halfTrain.f6)
		all_freqs.append(halfTrain.f7)
		all_freqs.append(halfTrain.f8)

plt.hist(all_freqs, bins=range(0, 79, 1))
plt.title("Frequency Histogram\n Master traversed trains 32 times 32x(ABAB)")
#plt.title("Frequency Histogram\n One Random Traversal 1 x (ABAB)")
plt.xlabel("Frequencies in Train A&B")
plt.ylabel("Frequency")
plt.ylim([0,70])
#plt.ylim([0,4])
plt.savefig("32_trav.png",dpi=144)
