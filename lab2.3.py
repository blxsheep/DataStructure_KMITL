def new_range(lst):
    ln = len(lst)
    ans = []
    if(ln==1):
        end = lst[0]
        i = 0.0 
        while(i<end):
            ans.append(round(i,3))
            i+=1.0
    elif(ln==2):
        start = lst[0]
        end = lst[1]
        i =float(start)
        while(i<end):
            ans.append(round(i,3))
            i+=1
    elif(ln==3):
        start = lst[0]
        end = lst[1]
        step = lst[2]
        i =float(start)
        while(i<end):
            ans.append(round(i,3))
            i+=step
    return tuple(ans)

l = []
print('*** New Range ***')
l  = list(map(float,input('Enter Input : ').split()))
print(new_range(l))