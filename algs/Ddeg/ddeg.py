import numpy as np



with open('rosalind_ddeg.txt','r') as file:
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

num_neb = []
for i in range(0,len(edge_mat)):
    temp = 0
    for j in range(0,len(edge_mat)):
        if edge_mat[i,j] == 1:
            temp += results[j]
    num_neb.append(temp)


f = open('results.txt','w')
for i in num_neb:
    f.write(str(i)+' ')

f.close()

