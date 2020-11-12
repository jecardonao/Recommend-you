class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildtree(inorder, preorder, insert, end):
    if insert > end:
        return None
    aNode = Node(preorder[buildtree.preIndex])
    buildtree.preIndex += 1
    if insert == end:
        return aNode
    inindex = search(inorder, insert, end, aNode.data)
    aNode.left = buildtree(inorder, preorder, insert, inindex - 1)
    aNode.right = buildtree(inorder, preorder, inindex + 1, end)
    return aNode


def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i


def inorden(a):
    if a is None:
        return None
    else:
        inorden(a.left)
        print(a.data, end=' ')
        inorden(a.right)


def preorden(a):
    if a is None:
        return None
    else:
        print(a.data, end=' ')
        preorden(a.left)
        preorden(a.right)


preord = ['G', 'E', 'A', 'I', 'B', 'M', 'C', 'L', 'D', 'F', 'K', 'J', 'H']
inorden = ['I', 'A', 'B', 'E', 'G', 'L', 'D', 'C', 'F', 'M', 'K', 'H', 'J']

buildtree.preIndex = 0
arbol = buildtree(inorden, preord, 0, len(inorden) - 1)
inorden(arbol)
print(" ")
preorden(arbol)
print(" ")
