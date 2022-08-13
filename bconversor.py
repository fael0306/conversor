def numtoalpha(lista):
    lista = str(lista)
    lista = lista.replace("10","A")
    lista = lista.replace("11","B")
    lista = lista.replace("12","C")
    lista = lista.replace("13","D")
    lista = lista.replace("14","E")
    lista = lista.replace("15","F")
    return lista

def alphatonum(lista):
    lista = str(lista)
    lista = lista.replace("A","10")
    lista = lista.replace("a","10")
    lista = lista.replace("B","11")
    lista = lista.replace("b","11")
    lista = lista.replace("C","12")
    lista = lista.replace("c","12")
    lista = lista.replace("D","13")
    lista = lista.replace("d","13")
    lista = lista.replace("E","14")
    lista = lista.replace("e","14")
    lista = lista.replace("F","15")
    lista = lista.replace("f","15")
    return lista

def dectohex(n):
    lista=[]
    n = int(n)
    while n>=16:
        resto = n%16
        n = int(n/16)
        lista.append(resto)
    lista.append(n)
    lista.reverse()
    for k in range(0,len(lista)):
        lista[k] = str(lista[k])
    lista = numtoalpha(lista)
    return lista

def dectobin(n):
    lista = []
    n = int(n)
    while n>=2:
        resto = n%2
        n = int(n/2)
        lista.append(resto)
    lista.append(n)
    lista.reverse()
    return lista

def bintodec(a):
    soma = 0
    a = list(str(a))
    for k in range(0,len(a)):
        a[k]=int(a[k])
    a.reverse()
    for k in range(0,len(a)):
        soma = soma+(a[k]*(2**k))
    return soma

def hextodec(a):
    soma = 0
    a = list(str(a))
    a = alphatonum(a)
    for k in range(0,len(a)):
        a[k]=int(a[k])
    a.reverse()
    for k in range(0,len(a)):
        soma = soma+(a[k]*(16**k))
    return soma

def bintohex(a):
    r = bintodec(a)
    r = dectohex(r)
    return r

def hextobin(a):
    r = hextodec(a)
    r = dectobin(a)
    return r
