class Queue :
    item = []
    num =0
    def __init__(self):      
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
q1 = Queue()
q2 = Queue()

inp = input('Enter Input : ').split(',')
for k in inp:
    if(k!='D'):
        a,b = k.split()
        if(a=='EN'):    
            #print('onLY Q2')        
            q2.push(int(b))
            #print('q1',end='')
            #q1.prnt()
            #print('q2',end='')
            #q2.prnt()
        elif(a=='ES'):     
            #print('only Q1')      
            q1.push(int(b))
            #print('q1',end='')
            #q1.prnt(
            #print('q2',end='')
            #q2.prnt()

    else:
        
        if(not q1.isEmpty()):            
            print(q1.popfront())
        elif( q1.isEmpty() and not q2.isEmpty()):
            print(q2.popfront())
        elif(q1.isEmpty() and q2.isEmpty()):
            print('Empty')


