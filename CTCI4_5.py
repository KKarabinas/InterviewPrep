#Validate BST: implement a function to check if a binary tree is a binary search tree

class TreeNode:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

def checkBST(root):
    if root == None:
        return True
    if root.left != None:
        if root.value <= root.left.value:
            return False
    if root.right!= None:
        if root.value > root.right.value:
            return False

    if not checkBST(root.left):
        return False
    if not checkBST(root.right):
        return False
    return True


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(7)

    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)

    root1.right.left = TreeNode(10)
    root1.right.right = TreeNode(1)

    print(checkBST(root))
    print(checkBST(root1))