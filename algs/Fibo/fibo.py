def fib(x):
    if x < 2:
        return(x)
    val1 = 1
    val2 = 0
    temp = 0
    for i in range(2,x+1):
        temp = val1 + val2
        val2 = val1
        val1 = temp
    return(temp)

value = 22

print(fib(value))


