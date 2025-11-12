class BinaryTreeNode:
    def __init__(self, data):
        self.data = data 
        self.left_child = None # renamed for pep 8 compliance
        self.right_child = None # renamed for PEP 8 compliance

def insert(root, new_value):
    """Insert a new node with the given value into the BST"""
    if root is None:
        return BinaryTreeNode(new_value)
    if new_value < root.data:
        root.left_child = insert(root.left_child, new_value)
    elif new_value > root.data:
        root.right_child = insert(root.right_child, new_value)
    else:
        #duplicate value found;
        # You can decide how to handle it
        print(f"Value {new_value} already exists in the tree.")

    return root

def delete_tree(root):
    """Delete all nodes of the tree by removing references."""
    if root:
        #delete left subtree
        delete_tree(root.left_child)
        root.left_child = None #remove references to left child

        #delete right subtree
        delete_tree(root.right_child)
        root.right_child = None #remove references to the right child

        #Remove data references 
        print(f"Deleting Node: {root.data}")
        root.data = None #Optioinal: remove data references 

#Build the tree
root = insert(None, 15)
insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)

print("Deleting all the elements of the binary tree. ")
delete_tree(root)
root = None #Remove references to the root node