'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work. 
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''

# Student details
def details():
    student_number = '28747445' #write your student number as a string
    student_email = 'hzhe0006' + '@student.monash.edu' #write your student email
    name = 'Huihong Zheng' #write your name as it appears on Moodle
    return str(student_number), student_email, name


def gcd(a, b):
    """ Determines greatest common divisor of two integers.
    
    Input : two integers a and b such that not a==b==0
    Output: greatest common divisor of a and b
    
    For example:
    >>> gcd(0, 4)
    4
    >>> gcd(10, 0)
    10
    >>> gcd(18, 27)
    9
    >>> gcd(21, 13)
    1
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == 0 and b == 0:
        return 0
    else :
        while a % b != 0:
            c = a % b
            a = b
            b = c
            gcd(a, b)
        return b



def reverse(lst):
    """ Computes reverse of input sequence.
    
    Input : any list (lst)
    Output: reverse of lst
    
    For example:
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse([10, 11, 12, 13, 14])
    [14, 13, 12, 11, 10]
    >>> reverse([1])
    [1]
    >>> reverse([])
    []
    """
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse(lst[:-1])


def is_pal(string):
    """Checks whether string is palindrome.
    
    Input : any string
    Output: True if string==string[::-1]
    
    For example:
    >>> is_pal('aa')
    True
    >>> is_pal('aabb')
    False
    >>> is_pal('aba')
    True
    """
    pass


from collections import deque
from graphs import neighbours, print_grid_traversal
import graphs

def bfs_traversal(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> bfs_traversal(g, 0, {12})
    [0, 1, 2, 12]
    >>> print_grid_traversal(g, 10, bfs_traversal(g, 0, {12}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    >>> print_grid_traversal(g, 10, bfs_traversal(g, 0, {22}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---004---003---005---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---006---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    pass


def dfs_traversal(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, dfs_traversal(g, 0, {12}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    >>> print_grid_traversal(g, 10, dfs_traversal(g, 0, {9, 40, 49}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---004---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   005---006---008---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   007   009---010---011---012---013---014   
    """
    pass


def bfs_path(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, bfs_path(g, 0, {22}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---004---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    pass


def dfs_path(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, dfs_path(g, 0, [9, 39]))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---004---005---006---007---008---009   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   010   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   011---012   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    pass


if __name__=='__main__':
    """
    <your paragraph with examples here>
    """

    import doctest
    doctest.testmod(verbose=True)
