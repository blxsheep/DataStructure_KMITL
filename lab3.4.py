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

st = Stack()
l = input('Enter Input : ').split(',')
for line in l:
    word = line.split()

    if(word[0]=='B'):
        print(st.size())
    elif(word[0]=='A'):
        s= int(word[1])
        if(st.isEmpty()):
            st.push(s)
        elif(st.peek()> s):
            st.push(s)
        else:
            while(not st.isEmpty() and st.peek()<=s):
                st.pop()
            st.push(s)
        
