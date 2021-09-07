
f = open("even.txt","w")

with open('rosalind_ini5.txt', 'r') as file:
    data = file.read().split('\n')
    
    for i in range(0,len(data)):
        if i%2 == 1:
            f.write(data[i]+"\n")

    file.close()


f.close()
