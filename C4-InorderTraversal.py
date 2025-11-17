from binarytree import build

class Node:

    #A class representing a node in a binary tree
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def print_inorder(root):
    #Recursivel performs an in-order traversal of the binary tree
    if root:
        #recursively traverse the left subtree
        print_inorder(root.left)

        #print the data of the node
        print(root.val, end='')

        #recursively traverse the right subtree
        print_inorder(root.right)

if __name__ == "__main__":
    #constructing the binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    #Using binary tree module to visualize the tree structure
    # Convert the tree into a binarytree node structure
    tree_list = [1,2,3,4,5]
    visual_tree = build(tree_list)

    print("\n Binary tree visualization: ")
    print(visual_tree)

    #printing in-order traversal
    print("In-order traversal of the binary tree is: ")
    print_inorder(root)
    print()