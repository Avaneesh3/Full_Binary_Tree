class Binary_tree_node:              #Binary Tree node class
    def __init__(self,value = None,left_child = None,right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def Full_BinaryTree_BFS(root_node):       #Checking whether Binary Tree is full using BFS
    if root_node is None:
        return False

    l = []                           #list functioning as a Queue using l.pop(0)
    l.append(root_node)
    nodes_removed,level = 0,0        #total number of nodes removed and current level of binary tree during traversal 

    while(len(l) > 0):
        node = l.pop(0)
        nodes_removed+=1
        if node.left_child is not None:
            l.append(node.left_child)
        if node.right_child is not None:
            l.append(node.right_child)
        if nodes_removed == (2**(level+1) - 1) :
            level += 1
            if len(l) > 0 and len(l) != 2**level :
                return False              #The given binary tree is not full
    return True      #The given binary tree is full


#-----------------------------------------Example----------------------------------
three = Binary_tree_node(3)
two = Binary_tree_node(2)
root_node = Binary_tree_node(1,two,three)
print(Full_BinaryTree_BFS(root_node))


#----------------------------------Counter Example----------------------------------
five =  Binary_tree_node(5)
four =  Binary_tree_node(4)
three = Binary_tree_node(3)
two = Binary_tree_node(2,four,five)
root_node = Binary_tree_node(1,two,three)
print(Full_BinaryTree_BFS(root_node))
