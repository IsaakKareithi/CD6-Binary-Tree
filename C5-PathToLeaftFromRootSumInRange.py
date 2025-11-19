class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def has_path_sum(node, target_sum):
    #Determines if the binary tree has a root-to-leaf path
    #with the given sum 

    #base case: if the currnet node is None, no path exists
    if node is None:
        return False
    
    #subtract the node's data from the target sum
    remaining_sum = target_sum - node.data

    #if the node is a leaf, check id the remaining sum is zero 
    if remaining_sum == 0 and node.left is None and node.right is None:
        return True
    
    #Recurse on the left and right subtrees
    return has_path_sum(node.left, remaining_sum) or has_path_sum(node.right, remaining_sum)

def find_paths_in_range(node, low, high, current_path = None, current_sum=0, valid_paths = None):
    #Finds all the root-to-leaf paths where the sum of the node value is within [low, high]


    #constr
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)







