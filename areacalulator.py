def polygonreg(c,a,n):
    c = float(c)
    a = float(a)
    n = float(n)
    totmul = c*a*n
    totans = totmul/2
    return totans
def square(c):
    c = float(c)
    totans = c*c
    return totans
def triangle(b,h):
    b = float(b)
    h = float(h)
    totmul = b*h
    totans = totmul/2
    return totans
def rectangle(b,h):
    b = float(b)
    h = float(h)
    totans = b*h
    return totans
def trapeze(b,g,h):
    b = float(b)
    g = float(g)
    h = float(h)
    totadd = b + g
    totmul = totadd * h
    totans = totmul/2
    return totans
ask = input('what is your shape, please only enter either "polygon", "triangle", "rectangle", "square" or "trapeze" ')
try:
    if ask == 'square':
        s = input('what is the lenth of a side? ')
        x = square(s)
        print(x)
    elif ask == 'triangle':
        ba = input('what is the base? ')
        hi = input(' what is the hight?')
        x = triangle(ba,hi)
    elif ask == 'rctangle':
        ba = input('what is the base? ')
        hi = input(' what is the hight?')
        x = rectangle(ba,hi)
    elif ask == 'polygon':
        ap = input(' what is the apothem? ')
        num = input('what is the number of sides?')
        si = input('what is the lenth of a side? ')
        x = polygonreg(si,ap,num)
    elif ask == 'trapeze':
        pb = input('what is the lenth of the small base? ')
        gb = input('what is the lenth of the big base? ')
        hi = input('what is the hight? ')
        x = trapeze(pb,gb,hi)
        print(x)
except:
    print('not in database')
            

    