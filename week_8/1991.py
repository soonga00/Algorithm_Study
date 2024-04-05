class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def find_parent(self, value):
        if self.value == value:
            return self
        if self.left is not None:
            left_result = self.left.find_parent(value)
            if left_result is not None:
                return left_result
        if self.right is not None:
            right_result = self.right.find_parent(value)
            if right_result is not None:
                return right_result
        

def preorder(node):
    if node == None:
        return
    print(node.value, end="")
    preorder(node.left)
    preorder(node.right)
    
def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.value, end="")
    inorder(node.right)

def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end="")


n = int(input())
root = node('A')
for _ in range(n):
    parent, left, right = map(str, input().split())
    tmp = root.find_parent(parent)
    if left != '.':
        tmp.left = node(left)
    if right != '.':
        tmp.right = node(right)

preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
