arr1, arr2  = input('Enter Input : ').split('/')
arr1 = list(map(int,arr1.split()))
arr2  = list(map(int,arr2.split()))
arr1.sort()
idx=0

for i in range(len(arr2)):
    #print('Target is {0}'.format(arr2[i]))
    b =False
    while(arr1[idx] <= arr2[i]):
        if(idx>=len(arr1)-1):
            print('No First Greater Value')
            b =True
            break
        else :
            idx+=1
    if(not b ):
        
        print(arr1[idx])
