import numpy as np
from joblib import Parallel, delayed
from Bio import ExPASy
from Bio import SwissProt

#read input
with open('rosalind_dbpr.txt','r') as file:
    lines = file.read().split('\n')    
    file.close()

#grab handel
handle = ExPASy.get_sprot_raw(lines[0])
record = SwissProt.read(handle)
a = dir(record)

rec = record.cross_references

results = []
for i in rec:
    if i[0] == 'GO':
        if i[2][0] == 'P':
            results.append(i[2][2::])


#write output
f = open('results.txt','w')
for i in results:
    f.write(str(i)+'\n')

f.close()



