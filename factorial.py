
fac = int(input('choose the factorial:'))
fac2 = fac - 1

def factorial(x,y):
    
    z = x * y

    if x == 1 or x == 0:
        x = 1
        y = 1
        print(x)
    elif y == 1:
        print(x)
        return
    else:
        print(x)
        y -= 1
        factorial(z,y)
    
factorial(fac,fac2)