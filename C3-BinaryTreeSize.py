class Node:
    """A class representing a neode in a binary tree
        
        Atributes:
            data : the value stored in he node.
            left_cild: A reference to the left child node
            right_child: A reference to the right child node    """
    

    def __init__(self, data):
        self.left_child = None
        self.data = data
        self.right_child = None

def find_size_recursive(root):
    """Calculates the total umber of nodes in the binary tree recursively
    
    Args:
         root (Node): the root node of the ninary tree
         
    Returns: 
        int: the size of binary tree"""
    
    if root is None:
        return 0
    return find_size_recursive(root.left_child) + find_size_recursive(root.right_child) + 1

def  find_size_iterative(root):
    """Calculates the total number of nodes in the binary tree iteratively
    
    Arg:
    argument -- root (node): the root node of the binary tree
    Return: int The size of the binary tree
    """
    if root is None:
        return 0
    
    count = 0
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        count += 1

        #push left and right children onto the stack if they exist
        if node.left_child is not None:
            stack.append(node.left_child)
        if node.right_child is not None:
            stack.append(node.right_child)

    return count

# Constructiong the binarry tree
root = Node(1)
root.left_child = Node(2)
root.right_child = Node(3)
root.left_child.left_child = Node(4)
root.left_child.right_child = Node(5)
root.right_child.left_child = Node(6)
root.right_child.right_child = Node(7)
root.right_child.right_child.left_child = Node(8)
root.right_child.right_child.right_child = Node(9)

#calculating and printing the size of the binary tree usinng recursive method
size_recursive = find_size_recursive(root)
print(f"The size of the binary tree (recursive) is: {size_recursive}")
#calculating and printing the size of the binary tree usinng iterative method
size_iterative = find_size_iterative(root)
print(f"The size of the binary tree (iterative) is: {size_iterative}")