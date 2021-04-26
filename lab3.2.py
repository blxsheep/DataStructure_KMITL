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
class Plate():
    def __innit__(self,w,f):
        self.w= w
        self.f = f
    def sett(self,w,f):
        self.w= w
        self.f = f
st =Stack()
k = input('Enter Input : ').split(',')

for line in k:
    word = line.split()       
    p = Plate()
    a = int(word[0])
    b = int (word[1])
    p.sett(a,b)
    if(st.isEmpty()):
        st.push(p)
        continue
    else:        
        while(st.peek().w <p.w ):            
            print(st.pop().f)
            if(st.isEmpty()):
                break
        st.push(p)
    
        
    


