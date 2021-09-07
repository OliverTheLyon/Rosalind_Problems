import numpy as np

def sum2(arr):
    look_up = {}

    for i in range(0,len(arr)):
        if str(int(arr[i] * (-1))) not in look_up:
            look_up[str(arr[i])] = i
        else:
            return([look_up[str(int(arr[i] * -1))]+1,i+1])
    return([-1])


with open('rosalind_2sum.txt','r') as file:
    lines = file.read().split('\n')
    arrs = []
    lines.pop(0)
    for line in lines[0:len(lines)-1]:
        temp = [int(i) for i in line.split(" ")]
        arrs.append(temp)
    file.close()


results = []
for arr in arrs:
    results.append(sum2(arr))
    print(results)
f = open('results.txt','w')
for i in results:
    for j in i:
        f.write(str(j)+' ')
    f.write('\n')

f.close()



