import InquiryScan as slave
import Inquiry as master
import pandas as pd
from collections import defaultdict

#Slave testing
freqSeq = []

print("Running Slave")
arr = slave.run()

#check all 32 hoppings
c = 4096
for i in range(1,513):
    freqSeq.append(arr[i*c-1])

print("Total Freqs: "+ str(len(pd.unique(freqSeq))))

d = defaultdict(int)
for f in freqSeq:
    d[str(f)] += 1

for element in d.keys():
    if d[element] > 16:
        print("<"+element +">: "+ str(d[element]))

print("Slave testing finished")


#Master testing