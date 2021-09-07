
with open('rosalind_ini3.txt', 'r') as file:
    data = file.read().split('\n')
    string = data[0]
    num_string = data[1].split(' ')
    a = int(num_string[0])
    b = int(num_string[1])+1
    c = int(num_string[2])
    d = int(num_string[3])+1
    
    string_out = str(string[a:b]) + " " + str(string[c:d])
    print(string_out)
    
    file.close()

