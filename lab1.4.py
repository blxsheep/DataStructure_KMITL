import timeit
start = timeit.timeit()


print('*** Fun with Drawing ***')
#num = int(input('Enter input : '))
num = 100
# wide  = 4x-3  
#wing x +x (boarder include)
#mid 2x-3
for i in range(0,num):
    for j in range(0,4*num-3):
        if(i+j==num-1 or j==4*num-3-num+i or j==2*num-i+num-3 or j==i+num-1) :print('*',end="")
        elif((j>num-1-i and j<i+num-1)or(j<3*num-3+i and j>2*num-i+num-3)): print('+',end='')
        else :print('.',end="")
    print('')   
for x in range(0,2*num-2):
    for y in range(0,4*num-3):
        if(x+1==y or y == 4*num-3-x-2):print('*',end='')
        elif(y>x+1 and y<4*num-5-x): print('+',end='')
        else: print('.',end='')
    print('')
end = timeit.timeit()
print(end-start)





    
