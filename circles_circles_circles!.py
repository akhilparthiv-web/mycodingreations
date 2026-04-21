from math import *
def dfror(r):
    x = 2 * float(r)
    return(x)
def rford(d):
    x = d/ 2
    return(x)
def cfrod(d):
    x = d * pi
    return(x)
def cfror(r):
    x = r*2*pi
    return(x)
def afrod(d):
    x = (d/2)**2*pi
    return(x)
def afror(r):
    x = r**2*pi
    return(x)
def rfroc(c):
    x = c/(2*pi)
    return(x)
def dfroc(c):
    x = c/pi
    return(x)
def rfroa(a):
    x = sqrt((a/pi))
    return(x)
def dfroa(a):
    x = sqrt((a/pi))
    y = 2*x
    return(y)
while True:
    ask = input('what do you want? ').lower()
    if ask == 'diameter':
        what = input('what do you have the value of(ie. circumfrence etc.)? ')
        if what == 'circumfrence':
            u = input('what it its value? ')
            try:
                x = dfroc(float(u))
            except:
                x = 'error, enter a number cuh',"\U0001F940","\U0001F940","\U0001F940"
            print(x)
        elif what == 'area':
            u = input('what it its value? ')
            try:
                x=dfroa(float(u))
            except:
                x = 'error, enter a number cuh',"\U0001F940","\U0001F940","\U0001F940"
            print(x)
        elif what == 'radius':
            u = input('what it its value? ')
            try:
                x=dfror(float(u))
            except:
                x = 'error, enter a number cuh',"\U0001F940","\U0001F940","\U0001F940"
            print(x)
    elif ask == 'radius':
        what = input('what do you have the value of(ie. circumfrence etc.)? ').lower()
        if what == 'circumfrence':
            u = input('what it its value? ')
            try:
                x = rfroc(float(u))
            except:
                x = 'error, enter a number cuh',"\U0001F940","\U0001F940","\U0001F940"
            print(x)
        elif what == 'area':
            u = input('what it its value? ')
            try:
                x = rfroa(float(u))
            except:
                x = 'error, enter a number cuh',"\U0001F940","\U0001F940","\U0001F940"
            print(x)
        elif what == 'diameter':
            u = input('what it its value? ')
            try:
                x=rfrod(float(u))
            except:
                x = 'error, enter a number cuh',"\U0001F940","\U0001F940","\U0001F940"
            print(x)
    elif ask == 'circumfrence':
        what = input('what do you have the value of(ie. circumfrence etc.)? ').lower()
        if what == 'radius':
            u = input('what it its value? ')
            try:
                x = cfror(float(u))
            except:
                x = 'error, enter a number cuh',"\U0001F940","\U0001F940","\U0001F940"
            print(x)
        elif what == 'diameter':
            u = input('what it its value? ')
            try:
                x=cfrod(float(u))
            except:
                x = 'error, enter a number cuh',"\U0001F940","\U0001F940","\U0001F940"
            print(x)
    elif ask == 'area':
        what = input('what do you have the value of(ie. circumfrence etc.)? ').lower()
        if what == 'radius':
            u = input('what it its value? ')
            try:
                x = afror(float(u))
            except:
                x = 'error, enter a number cuh',"\U0001F940","\U0001F940","\U0001F940"
            print(x)
        elif what == 'diameter':
            u = input('what it its value? ')
            try:
                x=afrod(float(u))
            except:
                x = 'error, enter a number cuh',"\U0001F940","\U0001F940","\U0001F940"
            print(x)
    else:
        print("byee","\U0001F940")
        break
    
