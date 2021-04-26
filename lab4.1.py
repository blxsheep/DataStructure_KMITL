class Queue :
    item = []
    def __innit__(self):
        self.item = []
    def isEmpty(self):
       return self.item== []
    def push(self,ob):
        self.item.append(ob)
    def popfront(self):
        k = self.item[0]
        del self.item[0]
        return k 
    def peek(self):
        return self.item[0]
    def prnt(self):
        print('\nIN Queue:')
        print(self.item)
    def size(self):
        return len(self.item)
q = Queue()

inp =input('Enter Input : ').split(',')
for k in inp:
    lis = k.split()
    
    if(lis[0]=='E') :
        q.push(int(lis[1]))
        print(q.size())
    elif(lis[0]=='D'):
        if(q.isEmpty()):
            print('-1')
        else:
             print(q.popfront(),end=' ')
             print('0')
            
if(q.isEmpty()):
    print('Empty')
else: 
    while(not q.isEmpty()):
        print(q.popfront(),end=' ')
        