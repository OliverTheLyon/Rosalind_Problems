def bin_search(arr, x):
    #base case
    if len(arr) < 3:
        for i in range(0,len(arr)):
            if arr[i] == x:
                return(int(i+1))
        return(-1)

    #split
    else:
        len1 = int(len(arr)/2)
        len2 = int(len(arr)-len1)
        v1 = bin_search(arr[0:len1],x)
        v2 = bin_search(arr[len1:],x)
        if 0 < v1:
            return(v1)
        elif 0 < v2:
            return(v2 + len1)
        else:
            return(-1)

f = open('results.txt','w')


with open('rosalind_bins.txt','r') as file:
    lines = file.read().split('\n')
    arr1 = [int(i) for i in lines[2].split(" ")]
    arr2 = [int(i) for i in lines[3].split(" ")]
    
    file.close()



results = []
for i in arr2:
    results.append(bin_search(arr1,i))
f = open('results.txt','w')
for i in results:
    f.write(str(i)+' ')

f.close()



