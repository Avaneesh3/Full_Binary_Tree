Problem Statement-

Given a Binary Tree with a root node, check whether the binary tree is a full binary tree or not using Breadth First Search(BFS).
A full binary tree is a binary tree having 2**n nodes at every level n.

Examples-

Binary Tree:  1
Maximum Level: 0
Number of Nodes at level 0: 1 == 2**0


Binary Tree:  1
            2   3
Maximum Level: 1
Number of Nodes at level 1: 2 == 2**1

Binary Tree:  1
            2   3
         4   5 6  7
Maximum Level: 2
Number of Nodes at level 2: 4 == 2**2

Solution-
The total number of nodes in a full binary tree of maximum level 'n' is '2**(n+1) - 1'.
The approach is that we will traverse all the nodes of the binary tree with BFS starting from the root node using a Queue.
After appending the left child and the right child of the head node in the queue we will pop(remove) the head node from the Queue.
Simultaneously, we will maintain a counter of the total number of nodes removed and the maximum level.
At every level 'n', if the total number of nodes removed equals '2**(n+1) - 1', we will check whether the length of the Queue is equal to 2**(n+1).
This will tell us whether the Binary Tree contains the required number of nodes at every level.

Time Complexity: Big O(k) where 'k' is the total number of nodes.  
If the Binary Tree is in fact a full Binary Tree then we will have to traverse all the 'k' nodes.
