def numtoalpha(lista):
    n=0
    for k in lista:
        if k=="10":
            lista[n]="A"
        if k=="11":
            lista[n]="B"
        if k=="12":
            lista[n]="C"
        if k=="13":
            lista[n]="D"
        if k=="14":
            lista[n]="E"
        if k=="15":
            lista[n]="F"   
        n=n+1
    return lista

def dectohex(n):
    lista=[]
    n = int(n)
    conc = ''
    while n>=16:
        resto = n%16
        n = int(n/16)
        lista.append(resto)
    lista.append(n)
    lista.reverse()
    for k in range(0,len(lista)):
        lista[k] = str(lista[k])
    lista = numtoalpha(lista)
    for k in lista:
        conc = conc+k
    return conc

def dectobin(n):
    lista = []
    n = int(n)
    conc = ''
    while n>=2:
        resto = n%2
        n = int(n/2)
        lista.append(resto)
    lista.append(n)
    lista.reverse()
    for k in lista:
        k = str(k)
        conc=conc+k
    conc = int(conc)
    return conc

def bintodec(a):
    soma = 0
    a = list(str(a))
    t = 0
    for k in range(0,len(a)):
        a[k]=int(a[k])
    a.reverse()
    for k in range(0,len(a)):
        soma = soma+(a[k]*(2**k))
    return soma

def hextodec(a):
    soma = 0
    a = list(str(a))
    a.reverse()
    for k in range(0,len(a)):
        if a[k]=="A" or a[k]=="a":
            soma = soma+(10*(16**k))
        elif a[k]=="B" or a[k]=="b":
            soma = soma+(11*(16**k))
        elif a[k]=="C" or a[k]=="c":
            soma = soma+(12*(16**k))
        elif a[k]=="D" or a[k]=="d":
            soma = soma+(13*(16**k))
        elif a[k]=="E" or a[k]=="e":
            soma = soma+(14*(16**k))
        elif a[k]=="F" or a[k]=="f":
            soma = soma+(15*(16**k))
        else:
            soma = soma+(int(a[k])*(16**k))
    return soma

def bintohex(a):
    r = bintodec(a)
    r = dectohex(r)
    return r

def hextobin(a):
    r = hextodec(a)
    r = dectobin(a)
    return r
