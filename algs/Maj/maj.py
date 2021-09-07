import numpy as np

def maj(arr):
    length = len(arr)
    array = np.array(arr)
    unique, counts = np.unique(array, return_counts=True)
    for i in range(0,len(counts)):
        if (length/2) < counts[i]:
            return(unique[i])

    return(-1)


with open('rosalind_maj.txt','r') as file:
    lines = file.read().split('\n')
    arr = []
    for line in lines[1:len(lines)-1]:
        arr.append([int(i) for i in line.split(" ")])
    file.close()


results = []
for i in arr:
    results.append(maj(i))
f = open('results.txt','w')
for i in results:
    f.write(str(i)+' ')

f.close()



