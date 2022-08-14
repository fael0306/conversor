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

def alphatonum(lista):
    n=0
    for k in lista:
        if k=="A" or k=="a":
            lista[n]=10
        if k=="B" or k=="b":
            lista[n]=11
        if k=="C" or k=="c":
            lista[n]=12
        if k=="D" or k=="d":
            lista[n]=13
        if k=="E" or k=="e":
            lista[n]=14
        if k=="F" or k=="f":
            lista[n]=15
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
# NÃO FUNCIONA DE HEXA PARA DECIMAL
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
