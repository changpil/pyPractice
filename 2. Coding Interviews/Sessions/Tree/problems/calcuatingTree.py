"""
Give an Node
{
    Node getLeft();
Node getRight();
String toString();
}
Give a root nodeNode root
       *
      / \
    +     -
   /  \  / \
   Pattern1:knapsack  2 3 4
Return(Pattern1:knapsack + 2) * (3 - 4)

If(Pattern1:knapsack + 2) + (3 + 4)
doesnot need to be bracketed Only leaf nodes are numbers

followup Give you * + 12 - 34 to return this tree
"""