import numpy as np
from joblib import Parallel, delayed

def sum3(arr):
    look_up = {}

    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if str(int(arr[i]+arr[j])) not in look_up:
                if i != j:
                    look_up[str(int(arr[i]+arr[j]))] = (i,j)
    
    for m in range(0,len(arr)):
        if str(int(arr[m]*-1)) in look_up:
            x,y = look_up[str(int(arr[m]*-1))]
            if x != m and y != m:
                temp = [m+1,y+1,x+1]
                temp.sort()
                return(temp)


    return([-1])


with open('rosalind_3sum.txt','r') as file:
    lines = file.read().split('\n')
    arrs = []
    lines.pop(0)
    for line in lines[0:len(lines)-1]:
        temp = [int(i) for i in line.split(" ")]
        arrs.append(temp)
    file.close()


results = Parallel(n_jobs=4)(delayed(sum3)(i) for i in arrs)
f = open('results.txt','w')
for i in results:
    for j in i:
        f.write(str(j)+' ')
    f.write('\n')

f.close()



