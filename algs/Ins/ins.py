import numpy as np

def insert(arr):
    tot = 0
    for i in range(1,len(arr)):
        k = i
        while k > 0 and arr[k] < arr[k-1]:
            tot += 1
            temp = arr[k-1]
            arr[k-1] = arr[k]
            arr[k] = temp
            k = k-1

    return(tot)

with open('rosalind_ins.txt','r') as file:
    lines = file.read().split('\n')
    arr = [int(i) for i in lines[1].split(" ")]
    file.close()

results = []
results.append(insert(arr))
f = open('results.txt','w')
for i in results:
    f.write(str(i)+' ')

f.close()



