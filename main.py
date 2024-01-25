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
def not_close(first_name,second_name): 
    if check_parent(first_name,second_name) or check_parent(second_name,first_name) or check_sibling(first_name,second_name): 
        return False 
    return True 
def furthest_child(person): 
    if person.children: 
        return 1+max(list(map(furthest_child,person.children))) 
    return 0 
def lowest_common_ancestor(first_name,second_name):  
    first_person=dict_data[first_name]  
    second_person=dict_data[second_name]  
    while(first_person.level<second_person.level):  
        second_person=second_person.parent  
    while(first_person.level>second_person.level):  
        first_person=first_person.parent  
    while(first_person.name != second_person.name):  
        first_person=first_person.parent  
        second_person=second_person.parent  
    return first_person 
def furthest_relation():  
    max=0  
    first_person= None  
    second_person= None 
    no_childs.add(root) 
    for a in no_childs:  
        for b in no_childs:  
            if a.level+b.level-2*lowest_common_ancestor(a.name,b.name).level>max:  
                max=a.level+b.level-2*lowest_common_ancestor(a.name,b.name).level  
                first_person=a.name  
                second_person=b.name 
    no_childs.remove(root) 
    print(first_person,second_person)
def delete_node(person):
    if person.children == None or person.children == []:
        if person.name in dads:
            dads.remove(person.name)
        if person in no_childs:
            no_childs.remove(person)
        dict_data.pop(person.name)
        person.parent.children.remove(person)
        del person
        return
    temp = person.children.copy()
    temp.append(person)
    list(map(delete_node,temp))
def size_node(person):
    if person.children: 
        return 1+sum(list(map(size_node,person.children))) 
    return 1

def hash(message):

    K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h5 = 0x9b05688c
    h4 = 0x510e527f
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    if message == '':
        return ''

    message = bytearray(message, 'ascii')

    length = len(message) * 8
    message.append(0x80)
    while (len(message) * 8 + 64) % 512 != 0:
        message.append(0x00)

    message += length.to_bytes(8, 'big')

    blocks = []
    for i in range(0, len(message), 64):
        blocks.append(message[i:i+64])

    for message_block in blocks:
        message_schedule = []
        for t in range(0, 64):
            if t <= 15:
                message_schedule.append(bytes(message_block[t*4:(t*4)+4]))
            else:
                term1 = _sigma1(int.from_bytes(message_schedule[t-2], 'big'))
                term2 = int.from_bytes(message_schedule[t-7], 'big')
                term3 = _sigma0(int.from_bytes(message_schedule[t-15], 'big'))
                term4 = int.from_bytes(message_schedule[t-16], 'big')

                schedule = ((term1 + term2 + term3 + term4) % 2**32).to_bytes(4, 'big')
                message_schedule.append(schedule)

        assert len(message_schedule) == 64

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7

        for t in range(64):
            t1 = ((h + _capsigma1(e) + _ch(e, f, g) + K[t] +
                   int.from_bytes(message_schedule[t], 'big')) % 2**32)

            t2 = (_capsigma0(a) + _maj(a, b, c)) % 2**32

            h = g
            g = f
            f = e
            e = (d + t1) % 2**32
            d = c
            c = b
            b = a
            a = (t1 + t2) % 2**32

        h0 = (h0 + a) % 2**32
        h1 = (h1 + b) % 2**32
        h2 = (h2 + c) % 2**32
        h3 = (h3 + d) % 2**32
        h4 = (h4 + e) % 2**32
        h5 = (h5 + f) % 2**32
        h6 = (h6 + g) % 2**32
        h7 = (h7 + h) % 2**32

    return (((h0).to_bytes(4, 'big') + (h1).to_bytes(4, 'big') +
            (h2).to_bytes(4, 'big') + (h3).to_bytes(4, 'big') +
            (h4).to_bytes(4, 'big') + (h5).to_bytes(4, 'big') +
            (h6).to_bytes(4, 'big') + (h7).to_bytes(4, 'big')).hex())

def _sigma0(num: int):
    num = (_rotate_right(num, 7) ^
           _rotate_right(num, 18) ^
           (num >> 3))
    return num

def _sigma1(num: int):
    num = (_rotate_right(num, 17) ^
           _rotate_right(num, 19) ^
           (num >> 10))
    return num

def _capsigma0(num: int):
    num = (_rotate_right(num, 2) ^
           _rotate_right(num, 13) ^
           _rotate_right(num, 22))
    return num

def _capsigma1(num: int):
    num = (_rotate_right(num, 6) ^
           _rotate_right(num, 11) ^
           _rotate_right(num, 25))
    return num

def _ch(x: int, y: int, z: int):
    return (x & y) ^ (~x & z)

def _maj(x: int, y: int, z: int):
    return (x & y) ^ (x & z) ^ (y & z)

def _rotate_right(num: int, shift: int, size: int = 32):
    return (num >> shift) | (num << size - shift)

dict_data = {} 
Q = deque() 
dads=set() 
no_childs=set()
root = None 
root = CreateTree(root)