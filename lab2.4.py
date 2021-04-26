ls = []
lls = []
ans = []
temp = []
ls=input('Enter Your List : ').split()
for x in ls :
    t = int(x)
    lls.append(t)
lls.sort()
if(len(lls)>2):
    for i in range(0,len(lls)):
        for j in range(i+1,len(lls)):
            for k  in range(j+1,len(lls)):
                if(lls[i]+lls[j]==-lls[k]) :
                #print(lls[i],lls[j],lls[k])
                
                    temp.append(lls[i])
                    temp.append(lls[j])
                    temp.append(lls[k])
                
                    e =temp.copy()
                    ans.append(e)
                    temp.clear()
                
    print(ans)
else: print('Array Input Length Must More Than 2')    




