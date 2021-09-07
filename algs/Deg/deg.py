import numpy as np



with open('rosalind_deg.txt','r') as file:
    lines = file.read().split('\n')
    edges = []
    num = 0
    lines.pop(0)
    for line in lines[0:len(lines)-1]:
        temp = [int(i) for i in line.split(" ")]
        edges.append(temp)
        if temp[0] > num:
            num = temp[0]
        if temp[1] > num:
            num = temp[1]
    file.close()

edge_mat = np.zeros((num,num))
for e in edges:
    edge_mat[e[0]-1,e[1]-1] = 1
    edge_mat[e[1]-1,e[0]-1] = 1

results = []
for arr in edge_mat:
    results.append(int(sum(arr)))
print(num)
#print(results)
f = open('results.txt','w')
for i in results:
    f.write(str(i)+' ')

f.close()



