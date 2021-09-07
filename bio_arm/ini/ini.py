import numpy as np
from joblib import Parallel, delayed
from Bio.Seq import Seq

#read input
with open('rosalind_ini.txt','r') as file:
    lines = file.read().split('\n')    
    file.close()

#count base pairs
my_seq = Seq(lines[0])
adenine = my_seq.count('A')
thymine = my_seq.count('T')
guanine = my_seq.count('G')
cytosine = my_seq.count('C')

results = [adenine, cytosine, guanine, thymine]
#write output
f = open('results.txt','w')
for i in results:
    f.write(str(i)+' ')

f.close()



