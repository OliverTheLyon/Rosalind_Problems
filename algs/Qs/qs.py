import numpy as np

def qs(arr,lo,hi):
    if lo < hi:
        pi = part(arr,lo, hi)
        qs(arr,lo,pi-1)
        qs(arr,pi+1,hi)
    return(arr)

def part(arr, lo, hi):
    pvt = arr[hi]
    i = (lo-1)
    for j in range(lo,hi):
        if arr[j] < pvt:
            i+=1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

    temp = arr[hi]
    arr[hi] = arr[i+1]
    arr[i+1] = temp
    return(i+1)

with open('rosalind_qs.txt','r') as file:
    lines = file.read().split('\n')
    arr1 = [int(i) for i in lines[1].split(" ")]
    file.close()



results = qs(arr1,0,len(arr1)-1)
f = open('results.txt','w')
for i in results:
    f.write(str(i)+' ')

f.close()



