import numpy as np
from joblib import Parallel, delayed

def par(arr):
    less = []
    mid = [arr[0]]
    more = []
    for i in arr[1::]:
        if arr[0] < i:
            more.append(i)
        elif i < arr[0]:
            less.append(i)
        else:
            mid.append(i)

    return(less+mid+more)


with open('rosalind_par3.txt','r') as file:
    lines = file.read().split('\n')
    arrs = []
    lines.pop(0)
    for line in lines[0:len(lines)-1]:
        temp = [int(i) for i in line.split(" ")]
        arrs.append(temp)
    file.close()


results = Parallel(n_jobs=4)(delayed(par)(i) for i in arrs)
f = open('results.txt','w')
for i in results:
    for j in i:
        f.write(str(j)+' ')
    f.write('\n')

f.close()



