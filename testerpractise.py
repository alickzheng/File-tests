

def rfactorial(n):
    '''
    >>> rfactorial(2)
    2
    >>> rfactorial(5)
    120
    '''
    if n == 0:
        return 1
    return n * rfactorial(n - 1)










if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True) 