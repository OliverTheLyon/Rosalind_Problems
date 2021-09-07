import numpy as np

def merg(arr1,arr2):
    idx1 = 0
    idx2 = 0
    arr = []
    while idx1 < len(arr1) and idx2 < len(arr2):
        if arr1[idx1] <= arr2[idx2]:
            arr.append(arr1[idx1])
            idx1 += 1

        elif arr2[idx2] < arr1[idx1]:
            arr.append(arr2[idx2])
            idx2 += 1
    
    while idx1 < len(arr1):
        arr.append(arr1[idx1])
        idx1 += 1
    
    while idx2 < len(arr2):
        arr.append(arr2[idx2])
        idx2 += 1

    return(arr)

def merg_sort(arr):
    if len(arr) == 1:
        return(arr)
    mid = int(len(arr)/2)
    arr1 = merg_sort(arr[0:mid])
    arr2 = merg_sort(arr[mid::])
    return(merg(arr1,arr2))


with open('rosalind_ms.txt','r') as file:
    lines = file.read().split('\n')
    arr = [int(i) for i in lines[1].split(" ")]
    file.close()

results = merg_sort(arr)
f = open('results.txt','w')
for i in results:
    f.write(str(i)+' ')

f.close()



