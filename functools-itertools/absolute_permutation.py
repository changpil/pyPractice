import itertools

def absolute_permutation(N, k) :
    N=list(range(1,N+1))
    #l = list(itertools.permutations(N, len(N)))
    for t in itertools.permutations(N):
        isAbs= True
        for i ,v in enumerate(t):
            if abs(v-(i+1)) != k:
                isAbs = False
                break
        if isAbs:
            return " ".join(list(map(str, t)))
    return -1


print(absolute_permutation(3,0))