#import sys
#sys.path.append(".")
from Trie.trie import Trie
# Input keys (use only 'a' through 'z' and lower case)
keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
output = ["Not present in trie", "Present in trie"]

t = Trie()
print("Keys to insert: ")
print(keys)

# Construct Trie
for key in keys:
    t.insert(key)

# Search for different keys
if t.search("the") is True:
    print("the --- " + output[1])
else:
    print("the --- " + output[1])

if t.search("these") is True:
    print("these --- " + output[1])
else:
    print("these --- " + output[0])

if t.search("abc") is True:
    print("abc --- " + output[1])
else:
    print("abc --- " + output[1])

t.delete("abc")
print("Deleted key \"abc\"")

if t.search("abc") is True:
    print("abc --- " + output[1])
else:
    print("abc --- " + output[0])