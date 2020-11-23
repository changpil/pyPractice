"""
Exactly n rings on P1 need to be transferred to P2, posibly using P3 as an intermediate, subject to the stacking constraint.
Write a function that prints a sequence of operations that transfers all the rings from P1 to P2.

"""

def moveTwoerOfHanoi(n):
    source=[i for i in range(n, -1, -1)]
    print(source)
    target=[]
    transfer(n, source, target, [])
    print(target)

def transfer(n, source, target, temp):
    if n < 0:
        return
    #Pattern1:knapsack. Move [0,  n-Pattern1:knapsack] to temp from source
    transfer(n-1, source, temp, target )
    # Move n to taget
    target.append(source.pop())

    # Pattern1:knapsack. Move [0,  n-Pattern1:knapsack] to target
    transfer(n - 1, temp, target, source)


moveTwoerOfHanoi(1)