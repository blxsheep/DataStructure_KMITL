class Queue :
    def __init__(self):
        self.item = []
    def isEmpty(self):
        return self.item ==[]
    def push (self,data):
        self.item.append(data)
    def pop(self):
        temp = self.item[0]
        del self.item[0]
        return temp
class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)
class Stack :

    def __init__ (self):
        self.item = []
    def isEmpty (self):
        return self.item == []
    def push(self,data):
        self.item.append(data)
    def pop (self):
        temp = self.item[-1]
        del self.item[-1]
        return temp
ino = 'Infix : '

class BST:
    def __init__(self):
        self.root = None
        

    def insert (self,data):
        cur = self.root
        if(self.root ==None) :
            self.root= Node(data)
            return self.root
        else:
            while True :
                if(data <=cur.data):
                    # left hand side
                    if(cur.left == None):
                        cur.left = Node(data)
                        break
                    else :
                        cur = cur.left
                else:
                    # right handside 
                    if(cur.right ==None):
                        cur.right = Node(data)
                        break 
                    else :
                        cur = cur.right 
            return self.root  

    def findmin(self):
        cur =self.root 
        while cur.left != None :
            cur =cur.left
        return cur.data   
    def findmax(self):
        cur = self.root
        while cur.right != None:
            cur = cur.right
        return cur.data     

    def edit(self,key):
        #Breadth first Search 
        cur= self.root
        q =Queue()
        q.push(cur)
        while not q.isEmpty():
            cur = q.pop()
            if(cur.data > key ):
                cur.data *=3
            if(cur.left!= None):
                q.push(cur.left)
            if(cur.right!= None):
                q.push(cur.right)
    def preorder(self,root):
        if(root != None):
            print(root.data,end ='')
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        global ino
        if(root != None):
            
            if(root.left != None or root.right!=None):
                #IT not leaf
                ino+='('
            self.inorder(root.left)
            ino+=str(root.data)
            
            self.inorder(root.right)
            if(root.right!= None or root.left != None):
                #it not leaf
                ino+=')'

    def posorder(self,root):
        if(root != None):
            
            self.posorder(root.left)
            self.posorder(root.right)
            print(root.data,end =' ')


    def BFS(self,root):
        q = Queue()
        q.push(self.root)
        while not q.isEmpty():
            temp = q.pop()
            print(temp.data,end = ' ')
            if(temp.left != None):
                q.push(temp.left)
            if(temp.right !=None):
                q.push(temp.right)

        
        
            
        
        


            



        
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Postfix : ')
s = Stack ()
for ch in inp:
    if ch in '+-*/^':
        righty = s.pop()
        lefty = s.pop()
        newNode = Node(ch,lefty,righty)
        s.push(newNode)
    else :
        s.push(Node(ch))
T.root = s.pop()
print('Tree : ')
T.printTree(T.root)
print('--------------------------------------------------')
T.inorder(T.root)
print(ino)
print('Prefix : ',end='')
T.preorder(T.root)


