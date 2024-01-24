from collections import deque
class node: 
    def __init__(self, name = None): 
        self.name = name 
        self.parent = None 
        self.children = None 
        self.level = None
def CreateTree(root): 
    if root == None: 
        root = node(input('Enter the name of the head of the family : ')) 
        root.level = 1 
        root.parent = node(None) 
        root.parent.name='' 
        dict_data[root.name] = root 
        Q.append(root) 
    while(True): 
        children = input(f"Enter the names of {Q[0].name}'s children : ").split(' ') 
        if children[0] == '': 
            if Q[0].parent.name not in dads: 
                no_childs.append(Q[0]) 
                dads.add(Q[0].parent.name) 
            Q.popleft() 
            if len(Q) == 0: 
                break 
            continue 
        children = list(map(node,children)) 
        for i in children: 
             Q.append(i) 
        Q[0].children = children 
        for i in children: 
            i.parent = Q[0] 
            i.level = i.parent.level + 1 
            dict_data[i.name] = i 
        Q.popleft() 
    return root
dict_data = {} 
Q = deque() 
dads=set() 
no_childs=set()
root = None 
root = CreateTree(root)