class mail :
    def __init__ (self):
        self.fn = ''
        self.ln = ''
        self.email = ''
        self.fullname = ''
    def create1 (self,first,last):
        self.fn = first
        self.ln = last
        self.email = (first+'.'+last+'@kmitl.ac.th')
        self.email = self.email.lower()
        self.fn = self.fn.capitalize()
        self.ln = self.ln.capitalize()
        self.fullname = self.fn+' '+self.ln
m1 = mail()
temp =[]


print('*** Create Email < BY KMITL > ***')
ls = input('Enter Input : ').split(',')
for line in ls:
    temp=(line.split())
    #print(temp,end='')
    #print('')
    if(temp[0]=='A'):
        m1.create1(temp[1],temp[2])
    elif(temp[0]=='F'):
        m1.create1(temp[1],m1.ln)
    elif(temp[0]=='L'):
        m1.create1(m1.fn,temp[1])
    elif(temp[0]=='E'):
        s = "'E' -> Email : "
        if(m1.fn==''and m1.ln==''):
            print(s+'Please Enter Your Firstname & Lastname')  
        elif(m1.fn==''):
            print(s+'Please Enter Your Firstname')
        elif(m1.ln==''):
            print(s+'Please Enter Your Lastname')
        else :
            print(s+m1.email)
    elif(temp[0]=='SA'):
        s="'SA' -> Fullname : "
        if(m1.fn==''and m1.ln==''):
            print(s+'Please Enter Your Firstname & Lastname')  
        elif(m1.fn=='') :
            print(s+'Please Enter Your Firstname')
        elif(m1.ln==''):
            print(s+'Please Enter Your Lastname')
        else :            
            print(s+m1.fullname)
    elif(temp[0]=='SF'):
        if(m1.fn=='') : print("'SF' -> Please Enter Your Firstname")
        else :print("'SF' -> Firstname : "+m1.fn)
    elif(temp[0]=='SL'):
        if(m1.ln=='') : print("'SL' -> Lastname : Please Enter Your Lastname")
        else : print("'SL' -> Lastname : "+m1.ln)
    elif(temp[0]=='X'): break
    else:
         print("'"+line+"'" +' is Invalid Input !!!')
         break
        
        
    

   

