def solution(A):
    s = set(A)
    for i in range(1,100000+1):
       if i not in A:
           return i
print(solution([1, 3, 6, 4, 1, 2]))