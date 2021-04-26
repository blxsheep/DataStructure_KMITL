#num = int(input('Enter Input : '))
import timeit
start = timeit.timeit()
num = 100
wide = 2*num+4
high = num+2
for i in range(1,high+1):
    for j in range(1,wide+1):
        if(j+i<num+3):print('.',end='')
        elif(i>1 and i <num+2 and j >wide/2+1 and j<wide) :print('#',end='')
        elif(j>wide/2) :print('+',end='')
        else: print('#',end='')
    print('')        
for i in range(high,0,-1):
    for j in range(wide,0,-1):
        if(j+i<num+3):print('.',end='')
        elif(i>1 and i <num+2 and j >wide/2+1 and j<wide) :print('+',end='')
        elif(j>wide/2) :print('#',end='')
        else: print('+',end='')
    print('')   
end = timeit.timeit()
print(end-start)         
