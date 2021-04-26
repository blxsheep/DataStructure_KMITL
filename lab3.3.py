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
    def prnt(self):
        print('\nStack')
        print(self.item)
dict = {'+':1,'-':1,'*':2,'/':2,'(':0,'^':3}


st =Stack()
d = input('Enter Infix : ')
print('Postfix : ',end='')
for k in d :
    #st.prnt()
    if(k.isalpha()):
        print(k,end='')
    else :
        #print(4)
        if(st.isEmpty()) :
            #print(5)
            st.push(k)
        elif(k =='('):
            st.push(k)
            
        elif(k == ')'):
            while(not st.isEmpty() and st.peek()!= '('):
               # print(1)
                print(st.pop(),end='')
            if(not st.isEmpty() and st.peek()=='('):
                st.pop()
            
        else:
            
            #print(3)
            
            while(not st.isEmpty() and dict[k]<=dict[st.peek()]):
                #print(2)
                print(st.pop(),end='')
            st.push(k)
while(not st.isEmpty()):
    print(st.pop(),end='')


       