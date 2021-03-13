# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
#
# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
#
# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
#
# Example 1:
# Input:
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

import collections
def build_graph(accounts):
    graph = collections.defaultdict(set)
    email_to_name = {}

    for account in accounts:
        name = account[0]
        for email in account[1:]:
            graph[account[1]].add(email)
            graph[email].add(account[1])
            email_to_name[email] = name
    return graph, email_to_name


def accountsMerge(accounts):
    graph,email_to_name = build_graph(accounts)
    #print(email_to_name)
    #print(graph)
    visited = set()
    merged = []
    for email in graph:
        components = []
        if email not in visited:
            dfs(graph, email, visited, components)
            merged.append([email_to_name[email]] + components)

    return merged

def dfs(graph, n, visited, component):
    visited.add(n)
    component.append(n)
    for child in graph[n]:
        if child not in visited:
            dfs(graph, child, visited, component)

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(accountsMerge(accounts))

