def numtoalpha(lista):
    for k in range(len(lista)-1):
        if lista[k]==10:
            lista[k]="A"
        elif lista[k]==11:
            lista[k]="B"
        elif lista[k]==12:
            lista[k]="C"
        elif lista[k]==13:
            lista[k]="D"
        elif lista[k]==14:
            lista[k]="E"
        elif lista[k]==15:
            lista[k]="F"
    return lista

def dectohex(n):
    lista=[]
    while n>=16:
        resto = n%16
        n = int(n/16)
        lista.append(resto)
    lista.append(n)
    lista = numtoalpha(lista)
    lista.reverse()
    return lista

def dectobin(n):
    lista = []
    while n>=2:
        resto = n%2
        n = int(n/2)
        lista.append(resto)
    lista.append(n)
    lista.reverse()
    return lista
