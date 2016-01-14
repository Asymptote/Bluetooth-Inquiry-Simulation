import InquiryScan as slave
import Inquiry as master
import pandas as pd
import numpy as np
from collections import defaultdict


def print_f_count(freq, train):
	freq = freq.tolist()
	print("\n-------"+train+"--------")
	print("Total Frequqncies: "+str(pd.unique(freq)))	
	for i in pd.unique(freq):
		print(str(i)+": "+str(freq.count(i)))

'''
#Slave testing
freqSeq = []

print("Running Slave")
arr = slave.run()

#check all 32 hoppings
c = 4096
for i in range(1,33):
    freqSeq.append(arr[i*c-1])

print("Total Freqs: "+ str(len(pd.unique(freqSeq))))

d = defaultdict(int)
for f in freqSeq:
    d[str(f)] += 1

for element in d.keys():
    if d[element] > 1:
        print("<"+element +">: "+ str(d[element]))
    if d[element] < 1:
        print("<"+element +">: "+ str(d[element]))

print("Slave testing finished")


indices = pd.unique(freqSeq)
indices.sort()
indices = indices.tolist()

even = list(range(0,79,2))
odd = list(range(1,79,2))
addresses = np.asarray((even+odd))

print(addresses[indices])
'''

#Master testing
print("Running Master")
arr = master.run()

freqSeq = arr

indices = pd.unique(freqSeq)
indices.sort()
indices = indices.tolist()

even = list(range(0,79,2))
odd = list(range(1,79,2))
addresses = np.asarray((even+odd))


############################################

ta_1 = arr[0:8192]
tb_1 = arr[8192:2*8192]
ta_2 = arr[2*8192:3*8192]
tb_2 = arr[3*8192:4*8192]

ta_1_f = addresses[ta_1]
tb_1_f = addresses[tb_1]
ta_2_f = addresses[ta_2]
tb_2_f = addresses[tb_2]

print("Train A-1 Unique Freqs: " + str(pd.unique(ta_1_f)))
print("Train B-1 Unique Freqs: " + str(pd.unique(tb_1_f)))
print("Train A-2 Unique Freqs: " + str(pd.unique(ta_2_f)))
print("Train B-2 Unique Freqs: " + str(pd.unique(tb_2_f)))

print_f_count(ta_1_f, 'Train A-1')
print_f_count(tb_1_f, 'Train B-1')
print_f_count(ta_2_f, 'Train A-2')
print_f_count(tb_2_f, 'Train B-2')

f_vals = addresses[indices]
print("Values: " + str(f_vals))
print("Total freqs: " + str(len(f_vals)))

