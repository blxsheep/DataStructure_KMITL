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
    def reverse (self):
        self.item.reverse()
    def isin(self,ob):
        return ob in self.item
blueq =Queue()
redq = Queue()
bcnt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rcnt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rbomb =0
bbomb =0
rans = ''
bans = ''
mistake =0
save = True

boom = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for j in range(0,500):
    bcnt.append(0)
    rcnt.append(0)
    boom.append(0)

srword ,bbword = input('Enter Input (Normal, Mirror) : ').split()

bword =[]
for k in bbword:
    bword.append(k)
bword.reverse()
lne = len(bword)
i = 0
while(i<lne) :
    if(i ==0):
        bcnt[i]=1
    else:
        if(bword[i]==bword[i-1]):
            bcnt[i] =bcnt[i-1]+1
            if(bcnt[i]==3):
                blueq.push(bword[i])
                bcnt[i]= 0
                del bcnt[i]
                del bcnt[i-1]
                del bcnt[i-2]
                del bword[i]
                del bword[i-1]
                del bword[i-2]
                i-=3
        else:
            bcnt[i] = 1
    i+=1
    lne = len(bword)

bbomb = blueq.size()
#blueq.prnt()
mt =[]
rword =[]
for i in srword:
    rword.append(i)
bword.reverse()
for k in bword :
    if(not blueq.isin(k)):
        bans+=k
#print(len(rword))
ln =len(rword)
i=0
while(i<ln) :    
    if(i ==0):
        rcnt[i]=1
        rans+=rword[i]
    else:
        #print('i=',end='')
        #print(i)
        
        if(rword[i]==rword[i-1]):
            rcnt[i] =rcnt[i-1]+1
            
            if(rcnt[i]==3):
                
                 
                
                if(not blueq.isEmpty())  :  
                    if(blueq.peek()==rword[i]):
                        mistake+=1 
                        save =True   
                            
                    
                    else:
                        save =True
                        #print('savee')
                    rans+=str(blueq.popfront())
                else:
                    #print('emq')
                    #print(' i = {0}'.format(i))
                    save =False
                    
                    
                rans+=rword[i]
                
                #print(rans)
                if(not save):
                    #print(rword[i])
                    redq.push(rword[i])
                    rcnt[i]=0  
                    del rcnt[i]
                    del rcnt[i-1]
                    del rcnt[i-2]
                    del rword[i]
                    del rword[i-1]
                    del rword[i-2]
                    i-=3
                
                
            elif(rcnt[i]==1 or rcnt[i]==2):
                rans+=rword[i]
            
        else:
            rcnt[i] = 1
            rans+=rword[i]
    ln = len(rword)
    i+=1
    #print('ln = {0}'.format(ln))
           
rr = []
for k in rans :
    rr.append(k)       
rr.reverse()
lasr = []
cnt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i =0
lnn = len(rr)
while(i<lnn):
    lasr.append(rr[i])
    if(i ==0):
        cnt[i]=1
    else:
        #print('i = {0} , lnn ={1}'.format(i,lnn))
        if(rr[i]==rr[i-1]):
            cnt[i] =cnt[i-1]+1
            if(cnt[i]==3):
                del lasr[-1]
                del lasr[-1]
                del lasr[-1]
                del rr[i]
                del rr[i-1]
                del rr[i-2]
                cnt[i]= 0
                del cnt[i]
                del cnt[i-1]
                del cnt[i-2]
                i-=3
        else:
            cnt[i] = 1
    i+=1
    lnn = len(rr)
rans = ''
for m in lasr :
    rans+=m
if(bbomb>redq.size()):
    rbomb =0
else:
    rbomb = redq.size()-bbomb
print('NORMAL :')
print(len(rans))
if(len(rans)==0):
    print('Empty')
else:
    print(rans)
print('{0} Explosive(s) ! ! ! (NORMAL)'.format(redq.size()))
if(mistake):
    print('Failed Interrupted {0} Bomb(s)'.format(mistake))
print('------------MIRROR------------')
print(': RORRIM')
print(len(bans))
if(len(bans)==0):
    print('ytpmE')
else :
    print(bans)
print('(RORRIM) ! ! ! (s)evisolpxE {0}'.format(bbomb))



