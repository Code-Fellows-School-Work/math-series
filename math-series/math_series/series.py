def fibonacci(n):
    # base case
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    # recursive case
    # used ChatGPT to mathematically express fibonacci sequence
    return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    # base case
    if n == 0:
        return 2
    
    if n == 1:
        return 1
    
    return lucas(n-2) + lucas(n-1)

# optional params 0 and 1 align with the first two values of the fib sequence
def sum_series(n, optional_param1=0, optional_param2=1):

    if n == 0:
        return None
    
    if n == 1:
        return None
    
    if optional_param1 == 0 and optional_param2 == 1:
        return fibonacci(n-3) + fibonacci(n-2)
    
    if optional_param1 == 2 and optional_param2 == 1:
        return lucas(n-3) + lucas(n-2)
    
    if optional_param2 > 1:
        return n+25, n-25