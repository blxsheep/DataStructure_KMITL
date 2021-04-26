def gcd (a,b):
    if(b%a==0):
        return a
    else :
        return gcd(b%a,a)


a,b = map(int,input('Enter Input : ').split())
if(a==0 and b==0):
    print('Error! must be not all zero.')

else:
    if a >= b >= 0 or a >= 0 >= b:
        print('The gcd of {0} and {1} is :'.format(a,b),end=' ')
    elif b >= a >= 0 or b >= 0 >= a:
        print('The gcd of {0} and {1} is :'.format(b,a),end=' ')
    elif a < 0 and b < 0:
        if abs(a) > abs(b):
             print('The gcd of {0} and {1} is :'.format(a,b),end=' ')
        else:
            print('The gcd of {0} and {1} is :'.format(b,a),end=' ')
    if(abs(a)>abs(b)):
        a,b=b,a
    if(a==0):
        a,b =b,a
    print(abs(gcd(a,b)))