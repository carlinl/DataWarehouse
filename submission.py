## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    if x == 0:
        return 0
    if x == 1:
        return 1
    a = 1
    b = x
    while(a <= b):
        mid = (a + b)//2
        if(mid <= x / mid):
            a = mid + 1
            ans = mid
        else:
            b = mid - 1
    return ans


################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    x = x_0
    count = 0
    x_new = x_0 - f(x_0)/fprime(x_0)
    while abs(x - x_new) >= EPSILON and count < MAX_ITER:
        x = x_new
        x_new = x_new - f(x_new)/fprime(x_new)
        count += 1
    return x_new

################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_tree(tokens): # do not change the heading of the function
    if  len(tokens) == 1:
        return Tree(tokens)

    stack = []
    for e in tokens:
        if e != ']':                        
            stack.append(e)
        else:
            children = []
            while stack[-1] != '[':
                children.append(stack.pop())
            stack.pop()
            parent = stack.pop()
            if not isinstance(parent, Tree):
                parent = Tree(parent)
            while children:
                if not isinstance(children[-1], Tree):
                    parent.add_child(Tree(children[-1]))
                else:
                    parent.add_child(children[-1])
                children.pop()
            stack.append(parent)
    return stack[0]

def max_depth(root): # do not change the heading of the function
    d = [1]
    if not root:
        return 0
    if root.children:
        for e in root.children:
            d.append(max_depth(e)+1)
        return max(d) 
    else:
        return 1
                
