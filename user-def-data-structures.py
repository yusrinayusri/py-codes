# user-defined data structures in python

# Linked list - linear data structure, data linked to pointers.
# node(data, pointer[next])
link_list = ['img1', 'img2', 'song1', 'song2']
print(link_list)

link_list.append('img3')
link_list.insert(1, 'song3')
print(link_list)

link_list.remove('song2')
print(link_list)

# Stack - linear data structure, LIFO, push(), pop()
stack = ['yusrina', 'francisco', 'bobby', 'nam do san']
print(stack)

stack.append('nam joo hyuk')
print(stack)

# print top item
n = len(stack)
print(stack[n-1])

stack.pop()
print(stack)

# Queue - linear data structure, FIFO
que = [1, 5, 6, 78, 345]
print(que)

que.append(67)
que.append(89)
print(que)

# print head/front
print(que[0])

# print rear/tail
n = len(que)
print(que[n-1])

que.remove(que[0])
print(que)

# Tree - hierarchical data structure (root, leaves)
class node:
    def __init__(self, ele):
        self.ele = ele
        self.left = None
        self.right = None

def preorder(self):
    if self:
        print(self.ele)
        preorder(self.left)
        preorder(self.right)

n = node('Hello')
n.left = node('there')
n.right = node('what is this bro')
preorder(n)

# Graphs - non linear data structure. contains nodes & edges
class adjnode:
    def __init__(self, val):
        self.val = val
        self.next = None


class graph:
    def __init__(self, vertices):
        self.v = vertices
        self.ele = [None] * self.v

    def edge(self, src, dest):
        node = adjnode(dest)
        node.next = self.ele[src]
        self.ele[src] = node

        node = adjnode(src)
        node.next = self.ele[dest]
        self.ele[dest] = node

    def __repr__(self):
        for i in range(self.v):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.ele[i]
            while temp:
                print(" -> {}".format(temp.val), end="")
                temp = temp.next


g = graph(4)
g.edge(0, 2)
g.edge(1, 3)
g.edge(3, 2)
g.edge(0, 3)
g.__repr__()

# Hashmaps - indexed data structures. Dictionaries.
def printdict(d):
    for key in d:
        print(key, "->", d[key])


hm = {0: 'first', 1: 'second', 2: 'third'}
printdict(hm)

hm[3] = 'fourth'
printdict(hm)

hm.popitem()
printdict(hm)
