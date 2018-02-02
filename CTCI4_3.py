#List of depths: given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth

#       5
#   3       7
# 2   4   6   8

class TreeNode:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

def createListOfDepths(root):
    depthList = []
    queue = []
    if not root:
        return depthList
    depthList.append([Node(root)])
    if root.left != None:
        queue.append(root.left)
    if root.left != None:
        queue.append(root.right)
    counter = 2

    while len(queue)!= 0:
        for x in queue:
            if x.left!= None:
                queue.append(x.left)
            if x.right!=None:
                queue.append(x.right)
        tempList = []
        for x in range(0,counter):
            node = Node(queue[0])
            queue.__delitem__(0)
            tempList.append(node)

        for x in range(0,len(tempList)):
            if x != len(tempList)-1:
                tempList[x].next = tempList[x+1]
        depthList.append(tempList)
        counter*=2


    return depthList

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    depthList = createListOfDepths(root)
    for x in depthList:
        string = ''
        for y in x:
            string+=(str(y.value.value))
            string+=("->")
        print(string)

