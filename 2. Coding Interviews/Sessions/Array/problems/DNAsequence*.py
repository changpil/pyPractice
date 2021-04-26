"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence.
Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively.
You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

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

"""

# Timeout
# def DNAsequence(S, P, Q):
#     cfmap ={'A':1, 'C':2, 'G':3, 'T':4}
#     f = []
#     for c in S:
#         f.append(cfmap[c])
#     map = [[0]*len(S) for _ in range(len(S))]
#     for i in range(len(f)):
#         minf = f[i]
#         for j in range(i, len(f)):
#             minf = min (minf, f[j])
#             map[i][j] = minf
#     result = []
#     for i in range(len(P)):
#         result.append(map[P[i]][Q[i]])
#     return result

def DNAsequence(S, P, Q):
    cfmap ={'A':1, 'C':2, 'G':3, 'T':4}
    prefixSum1, prefix1 = [0], 0
    prefixSum2, prefix2 = [0], 0
    prefixSum3, prefix3 = [0], 0
    prefixSum4, prefix4 = [0], 0

    for c in S:
        if c == 'A':
            prefix1 += 1
        elif c == 'C':
            prefix2 += 1
        elif c == 'G':
            prefix3 += 1
        elif c == 'T':
            prefix4 += 1

        prefixSum1.append(prefix1)
        prefixSum2.append(prefix2)
        prefixSum3.append(prefix3)
        prefixSum4.append(prefix4)

    result = []
    for i in range(len(P)):
        if P[i] == Q[i]:
            result.append(cfmap[S[P[i]]])
        else:
            if prefixSum1[Q[i] + 1] > prefixSum1[P[i]]:
                result.append(1)
            elif prefixSum2[Q[i] + 1] > prefixSum2[P[i]]:
                result.append(2)
            elif prefixSum3[Q[i] + 1] > prefixSum3[P[i]]:
                result.append(3)
            elif prefixSum4[Q[i] + 1] > prefixSum4[P[i]]:
                result.append(4)
    return result

print(DNAsequence('CAGCCTA', [2, 5, 0], [4,5,6]))