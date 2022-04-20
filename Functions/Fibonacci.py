def fibonacci(a):
    if(a <= 1):
        return a
    else:
        return(fibonacci(a-1) + fibonacci(a-2))
n = int(input("Enter number of terms:"))
print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i))
