def fibonacci(n):
    """ 

    The Fibonacci sequence is, by definition, the integer sequence in which every number after the first two is the sum of the two preceding numbers. To simplify:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

    In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 

    Fn = Fn-1 + Fn-2 
    with seed values 

    F0 = 0 and F1 = 1.

    """

    if n == 0 | n ==1:
        return
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

def lucas(n):
    """
    Lucas numbers are also defined as the sum of its two immediately previous terms.

    The Lucas numbers are in the following integer sequence:
    2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 …………..
    """
    if n == 0:
        return 2
    elif n==1:
        return    
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, default1=0, default2=1):

    """

    """
    if n == 0:
        return default1
    elif n == 0:
        return default1
    else:
        return sum_series

    pass