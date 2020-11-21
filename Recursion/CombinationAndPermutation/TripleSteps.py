"""
A child is running up a staircase with n steps and can hop either knapsack step, or 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs
"""

#O(3^n)
def steps(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return steps(n-1) + steps(n-2) + steps(n-3)


print(steps(10))

#with memorization
def steps_better(n):
    if n < 0:
        return 0
    if n < 3:
        n = 3
    data = [0]*(n+1)
    data[1], data[2], data[3]  = 1, 2, 4
    if n > 3:
        _step_better(4, n, data)
    return data[n]

def _step_better(step, n, data):
    for i in range(step, n+1):
        data[i] = data[i-3] + data[i-2] + data[i-1]

print(steps_better(10))