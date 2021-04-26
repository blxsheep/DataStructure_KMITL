class Stack :
    item = []
    def __innit__(self):
        self.item = []
    def isEmpty(self):
        return self.item == []
    def push (self,items):
        self.item.append(items)
    def pop(self):
        return self.item.pop()
    def peek(self):
        return self.item[-1]
    def size(self):
        return len(self.item)
opened =['(','[','}']
closed =[')',']','}']
l  = input('Enter Input : ')
opc = [0,0,0]
clc = [0,0,0]

for k in l :
    if(k in opened):
        opc[opened.index(k)]+=1
    elif(k in closed):
        clc[closed.index(k)]+=1
if(opc==clc):
    print('Parentheses : Matched ! ! !')
else:
    print('Parentheses : Unmatched ! ! !')
