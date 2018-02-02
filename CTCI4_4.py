#Checked Balanced: implement a function to check if a binary tree is balanced. for the purpose of this question,
#  a balanced tree is defined to be a tree such that the heights of two subtrees of a node never differ by more than one.

class TreeNode:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

def checkHeight(root):
    if root == None:
        return -1
    leftHeight = checkHeight(root.left)
    if leftHeight == "Error-Not Balanced":
        return leftHeight
    rightHeight = checkHeight(root.right)
    if rightHeight == "Error-Not Balanced":
        return rightHeight

    heightDiff = leftHeight - rightHeight
    if abs(heightDiff) > 1:
        return "Error-Not Balanced"
    else:
        return max(leftHeight,rightHeight)+1

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

    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(8)

    root1.right.right.left = TreeNode(9)
    root1.right.right.right = TreeNode(10)
    root1.right.right.left.left = TreeNode(11)
    root1.right.right.left.right = TreeNode(12)


    print(checkHeight(root))
    print(checkHeight(root1))