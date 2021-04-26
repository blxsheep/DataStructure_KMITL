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
    def isin(self,ob):
        return ob in self.item
    def insert(self,idx,obs):
        idx =int(idx)
        self.item.insert(idx,obs)
    def islast(self,indx):
        if(indx>=self.size()):
             print('ErrorINdxLAst')
        return  int(indx)==self.size()-1 

class pair ():
    def __init__(self,g,v):
        self.g= g
        self.v= v

vval = []
vg= []
#q = Queue()
q =[]

m,n= input('Enter Input : ').split('/')

def inls(lis,obs):
    llis =[]
    for l in lis:
        op = l.v
        llis.append(op)
    return obs.v in llis

def gruop_in_list(lis,obs):
    llis =[]
    for l in lis:
        op = l.g
        llis.append(op)
    return obs.g in llis




line  = m.split(',')

for i in line :    
    a,b = i.split()   
    vval.append(b)
    vg.append(a)

linee  = n.split(',')

for i in linee :
    if(i =='D'):
        if(not q==[]):
            t = q[0]
            del q[0]
            print(t.v)
        else:
            print('Empty')
    else:
        cmd,val = i.split()
        if(cmd=='E'):
            index0 = vval.index(val)
            temp = pair(vg[index0],val)
            if(q==[] or not gruop_in_list(q,temp)):
                q.append(temp)
            else:
                ix =len(q)-1
                while(ix >=0 and q[ix].g!=temp.g ):
                    ix-=1
                #if(not inls(q,temp)):
                    
                q.insert(ix+1,temp)
                ix=len(q)-1

                





    


        






    
         
