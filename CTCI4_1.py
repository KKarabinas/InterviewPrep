# given a directed graph, design an algorithm to find out whether there is a route between two nodes
import queue

class Node:
    def __init__(self,val):
        self.value = val
        self.children = []
        self.visited = False

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if Queue:
            tmp = self.items[0]
            self.items.__delitem__(0)
            return tmp
    def display(self):
        print([x.value for x in self.items])
    def isEmpty(self):
        return self.items == []

def findRouteBFS(root,node):
    queue = Queue()
    root.visited = True
    queue.enqueue(root)
    while not queue.isEmpty():
        r = queue.dequeue()
        if r == node:
            return True
        for x in r.children:
            if x.visited != True:
                x.visited = True
                queue.enqueue(x)
    return False

def findRouteDFS(root,node):
    if root == None:
        return False
    root.visited = True
    for x in root.children:
        if (x == node):
            print(True)
        if x.visited == False:
            findRouteDFS(x,node)

if __name__ == '__main__':
    root = Node(0)
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)

    root.children.append(a)
    root.children.append(b)
    a.children.append(c)
    a.children.append(d)
    b.children.append(e)
    b.children.append(f)
    f.children.append(g)

    #findRouteDFS(root,g)
    #findRouteDFS(e,g)

    #print(findRouteBFS(root,g))
    #print(findRouteBFS(e, g))

