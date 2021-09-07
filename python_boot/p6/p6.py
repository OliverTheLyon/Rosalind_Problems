
f = open("freq.txt","w")
words = {}

with open('rosalind_ini6.txt', 'r') as file:
    data = file.read().split('\n')
    data = data[0].split(' ')
    for w in data:
        words[w] = 0
    for w in data:
        words[w] = words[w] + 1

    file.close()

for key, freq in words.items():
    print(key+' '+str(freq))


f.close()
