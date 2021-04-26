print('******** Parking Lot ********')
line = input('Enter max of car,car in soi,operation : ').split()
cap = int(line[0])
log = []
if(line[1]!='0'):
    k = line[1].split(',')
    for h in k:
        log.append(int(h))
   
cmd = line[2]
cnum = int(line[3])
if(cmd == 'arrive') :
    if( cnum in log ):
        print('car {0} already in soi'.format(cnum))
    elif(  len(log)< cap):
        log.append(cnum)
        txt = 'car {0} arrive! : Add Car {0}'.format(cnum)
        print(txt)
    else:
        print('car {0} cannot arrive : Soi Full'.format(cnum))
elif(cmd =='depart'):
    if(log==[]):
        print('car {0} cannot depart : Soi Empty'.format(cnum))
    elif(cnum in log):
        log.remove(cnum)
        print('car {0} depart ! : Car {0} was remove'.format(cnum))
    elif(not cnum in log):
        print('car {0} cannot depart : Dont Have Car {0}'.format(cnum))

      
print(log)


