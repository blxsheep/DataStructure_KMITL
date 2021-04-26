finish = False
def hash (st):
    code = 0
    for ch in st :
        code+= ord(ch)
    return code
def manage(hashcode,data,lis):
    size = len(lis)
    global finish
    index  =hashcode%size 
    
    if(not finish):
        
        if(not isfull(lis)):
            if(lis[index]==-1):
                lis[index] = data
            else:
                i=0
                while(lis[index]!=-1):

                    i+=1
                    collisoin  = i 
                    if(collisoin > maxCol) :
                        print ('Max of collisionChain')
                        return 
                        
                    print('collision number {0} at {1}'.format(collisoin,index))
                    
                    index = (hashcode + i*i)%size
                lis[index] =data
        else :
            print("This table is full !!!!!!")
            finish = True
        
       
def isfull(lis):
    full = True 
    for i in lis :
        if(i==-1) :
            full =False
            break
    return full
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)
def createTable (size):
    lis= []
    for i in range(size):
        lis.append(-1)
    return lis
print(' ***** Fun with hashing *****')
left,right = input('Enter Input : ').split('/')
tablesize =  int(left[0])

maxCol  =  int(left[2])
lisofpair  = []
table = createTable(tablesize)
right = right.split(',')
first =True 
for e in right :
    if(not finish and not first) :print('---------------------------')
    k,v = e.split()
    lisofpair.append(Data(k,v))
    first =False
    #print(Data(k,v))
   
    manage(hash(k),Data(k,v),table)
    inn = 0 
    for j in table :
        inn+=1
        if(not finish)  :
            print("#{0}".format(inn),end="	")
            print(j) if(j !=-1 ) else print("None")


