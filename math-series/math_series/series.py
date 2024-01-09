def fibonacci(n):
    # base case
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    # recursive case
    # used ChatGPT to mathematically express fibonacci sequence
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    # base case
    if n == 0:
        return 2
    
    if n == 1:
        return 1
    
    return lucas(n-2) + lucas(n-1)