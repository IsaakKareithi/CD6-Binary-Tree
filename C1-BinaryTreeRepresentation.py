#Install the binary tree module if you haven't already
#pip install binary tree

from binarytree import Node

#create root node
root = Node(1) 

#create left and right node
root.left = Node(2)
root.right = Node(3)

#Add morenodes to  the left sub tree
root.left.left =  Node(4)
root.left.right =  Node(5)

#add mmore nodes to the right sub tree
root.right.left =  Node(6)
root.right.right = Node(7)

#Display the binary tree
print("Binary tree structure: ")
print(root)

#in-order traversal to display the tree nodes
def in_order_traversal(node):
    if Node:
        in_order_traversal(node.left)
        print(node.value)
        in_order_traversal(node.right)

#in-order traversal to display the three nodes
def pre_order_traversal(node):
    if node:
        print(node.value)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

# post-order traversal todisplay the 3 noes
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value)

#display the nodes using different traversals 
print("\n In-order Traversal: ")
in_order_traversal(root)
print("\n")

print("Pre-order Traversal: ")
pre_order_traversal(root)
print('\n')

print("Post-order Traversal: ")
post_order_traversal(root)
print()

