
with open('rosalind_ini4.txt', 'r') as file:
    data = file.read().split('\n')
    split_data = data[0].split(' ')
    a = int(split_data[0])
    b = int(split_data[1])+1
    total = 0
    for i in range(a,b):
        if i%2 == 1:
            total += i

    print(total)
    file.close()

