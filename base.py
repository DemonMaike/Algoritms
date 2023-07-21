"""
My task is verification int in list
"""
x = 5

ok_test_list = [x for x in range(0,6)]
bad_tast_list = []
error_test_list = [x for x in range (0,5)]

def test(x:int, test_list:list) -> str:
    result = None
    for i in test_list:
        if i == x:
            result = x
    return result

print ('ok_test_list ',test(x, ok_test_list)) # O(n)
print ('bad_tast_list ',test(x, bad_tast_list)) # O(n)
print ('error_test_list ',test(x, error_test_list)) # O(n)

# and that func's hard is O(n) becouse
#  we go on all elements
# in our lists, and we do it once on each element.
# No matter how long our list.

"""
Task for replacement variable A and B.
"""
a = 1
b = 2

def replacement(a:any, b:any) -> None: # O(1)
    print(f'Before replacement: a = {a}, b = {b}')
    t = a # Step 1
    a = b # Step 2
    b = t # Step 3
    print(f'After replacement: a = {a}, b = {b}')

replacement(a, b)

# O(1) = 3

"""
Creating cycles
"""

# Algoritm's hard is O(n) = n
def cycle_hard_On(n:int) -> None:
    for i in range(n):
        print(i)

# Algorim's hard is O(3) = 3 and that's O(n) when n is len our cycle
cycle_hard_On(3)
