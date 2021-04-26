print('*** multiplication or sum ***')
lis = input('Enter num1 num2 : ').split()
li = []
for k in lis :
    t = int(k)
    li.append(t)
    
if(li[0]*li[1]<=1000) :print('The result is {0}'.format(li[0]*li[1]))
else:print('The result is {0}'.format(li[0]+li[1]))