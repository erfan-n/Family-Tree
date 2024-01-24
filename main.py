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
def add_node(first_name,second_name):
    first_person=node(first_name) 
    second_person=dict_data[second_name]
    if second_name in dads:
        second_person.children.append(first_person)
    elif second_name not in dads and second_person not in no_childs:
        second_person.children.append(first_person)
        no_childs.add(first_person)
    elif second_person in no_childs:
        if len(second_person.parent.children) > 1:
            w = None
            for i in second_person.parent.children:
                if i.children==None and i.name != second_name:
                    w = i
                    break
            if w:
                no_childs.add(second_person.parent.children[second_person.parent.children.index(w)])
            else:
                dads.remove(second_person.parent.name)
        else:
            dads.remove(second_person.parent.name)
        no_childs.remove(second_person)
        no_childs.add(first_person)
        second_person.children = [first_person]
    first_person.parent = second_person
    first_person.level = first_person.parent.level+1
    dict_data[first_name] = first_person
    dads.add(second_name)
def check_parent(first_name,second_name): 
    first_person=dict_data[first_name] 
    second_person=dict_data[second_name] 
    while(first_person.level<second_person.level): 
        second_person=second_person.parent 
    if second_person.name==first_person.name: 
        return True 
    else: 
        return False 
def check_sibling(first_name,second_name): 
    if dict_data[first_name].parent.name==dict_data[second_name].parent.name: 
        return True 
    return False 
dict_data = {} 
Q = deque() 
dads=set() 
no_childs=set()
root = None 
root = CreateTree(root)