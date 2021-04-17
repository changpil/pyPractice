"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.
"""

# Time Complexity : O(N*M)
# def impactFactors(sequences, start, end):
#     map = {'A':1, 'C':2, "G":3, "T":4}
#     factors = []
#     for ch in sequences:
#         factors.append(map[ch])
#     minimalFactors = []
#     for i in range(len(start)):
#         minimalFactors.append(min(factors[start[i]: end[i] +1]))
#     return minimalFactors

def impactFactors(sequences, start, end):
    n = len(sequences)
    m = len(start)

    aux = [[0 for i in range(n + 1)] for i in [0, 1, 2]]

    for i, c in enumerate(sequences):
        aux[0][i + 1] = aux[0][i] + (c == 'A')
        aux[1][i + 1] = aux[1][i] + (c == 'C')
        aux[2][i + 1] = aux[2][i] + (c == 'G')

    print(aux)
    result = []

    for i in range(m):
        fromIndex, toIndex = start[i], end[i] + 1
        if aux[0][toIndex] - aux[0][fromIndex] > 0:
            r = 1
        elif aux[1][toIndex] - aux[1][fromIndex] > 0:
            r = 2
        elif aux[2][toIndex] - aux[2][fromIndex] > 0:
            r = 3
        else:
            r = 4

        result.append(r)

    return result


sequences = "CAGCCTA"
starts, ends = [2,5,0], [4,5,6]
print(impactFactors(sequences, starts, ends))
