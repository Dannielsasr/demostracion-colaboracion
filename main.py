print("Hola soy Felipe")
print("hola soy  daniel")
print("hola soy danny sanchez")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)