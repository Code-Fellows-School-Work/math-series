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

def multiply(n):
    return n*n

# optional params 0 and 1 align with the first two values of the fib sequence
# modified sum_series code from insights gained from class code review
def sum_series(n, optional_param1=0, optional_param2=1):

    if optional_param2 > 1:
        return multiply(n)

    if optional_param1 == 0 and optional_param2 == 1:
        return fibonacci(n)
    
    if optional_param1 == 2 and optional_param2 == 1:
        return lucas(n)
    
    
      
    