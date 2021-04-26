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
ans2 = []
ans1 =[]
#print(ord('a'))
#print(chr(97))
a,b = input('Enter String and Code : ').split(',')
def cv (char,key):
    num = ord(char)
    num+=key
    if(num>90 and num< 97) : 
        num-=26
    elif( num>122):
        num-=26
    return chr(num)

for i in a :
    if(i!=' '):
        q1.push(i)
        ans2.append(i)
for j in b :
    if(j!=' '):
        q2.push(j)
while(not q1.isEmpty()):
    
    k = int(q2.popfront())
    q2.push(k)
    ann = cv(q1.popfront(),k)
    ans1.append(ann)

print('Encode message is :  ',end='')
print(ans1)
print('Decode message is :  ',end='')
print(ans2)
