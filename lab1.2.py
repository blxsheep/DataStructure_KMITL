
import math
import locale
locale.setlocale(locale.LC_ALL,'')
print('*** Converting hh.mm.ss to seconds ***')
list = input('Enter hh mm ss : ').split()

l=[]
            
for i in list:
    t= int(i)
    l.append(t)
l.reverse()
#print(list)
if(l[1]>=60 or l[1]< 0 ) : print('mm({0}) is invalid!'.format(l[1]))
elif(l[2]<0) : print('hh({0}) is invalid!'.format(l[2]))
elif(l[0]>=60 or l[0]<0): print('ss({0}) is invalid!'.format(l[0]))
else :          
            
            sum = 0 
            list.reverse()

  
            for x in  range(0,3):
                sec = math.pow(60,x)*l[x]
                sum+=sec
                l[x] = '{:02d}'.format(l[x])

            sum = int(sum)
            sum = '{:n}'.format(sum)

            print('{0}:{1}:{2} = {3} seconds'.format(l[2],l[1],l[0],sum))