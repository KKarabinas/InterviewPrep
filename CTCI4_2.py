#Minimal Height: given an sorted array in increasing order with unique integer elements, write an algo to create a
# binary search tree with minimal height

#                   8
#           4               12
#       2       6       10      14
#     1   3   5  7     9  11  13  15

class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

def preOrderTraversal(root):
    if root:
        print(root.value)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

def createMinBSTFromArray(array):
    if array == []:
        return None
    mid = int(len(array)/2)
    n = Node(array[mid])
    n.left = createMinBSTFromArray(array[0:mid])
    n.right = createMinBSTFromArray(array[mid+1:])
    return n



if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    root = createMinBSTFromArray(array)
    preOrderTraversal(root)
