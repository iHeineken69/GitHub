# Fibonacci numbers from the users input number
def fib(n):
    results = []
    a, b = 0, 1
    while a < int(n):
        results.append(a)
        a, b = b, a+b          
    return results

# Prints all the even numbers from the users input number
def even_number(n):
    results = []
    a = 0
    while a < int(n):
        results.append(a)
        a = a + 2
    return results

# Prints all the odd numbers from the users input number
def odd_number(n):
    results = []
    a = 1
    while a < int(n):
        results.append(a)
        a = a + 2
    return results
        
data = int(input("Enter a number for the fib calc: "))
data1 = int(input("Enter a number for the even_n calc: "))
data2 = int(input("Enter a number for the odd_n calc: "))

print("This is a fibonacci series")
print(fib(data))
print("This is a even number series")
print(even_number(data1))
print("This is a odd number series")
print(odd_number(data2))

a = fib(data)
b = even_number(data1)


