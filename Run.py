import InquiryScan as slave
import Inquiry as master
import pandas as pd
import numpy as np
from collections import defaultdict

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




#Master testing
#print("Running Master")
#arr = master.run()