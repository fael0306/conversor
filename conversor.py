import bconversor

def main():
    resultado = ""
    imp = 0
    imp2 = 0

    while imp==0:
        try:
            imp = 1
            n = int(input("Digite um número inteiro: "))
        except:
            imp = 0

    while imp2==0:
        try:
            imp2 = 1
            op = int(input("Digite a base (apenas 2 ou 16): "))
            while op!=2 and op!=16:
                op = int(input("Digite a base (apenas 2 ou 16, por favor): "))
        except:
            imp2 = 0

    if op==2:
        aux = bconversor.dectobin(n)
    if op==16:
        aux = bconversor.dectohex(n)

    for k in range(0,len(aux)):
        resultado = resultado+str(aux[k])
        
    print("O hexadecimal desse número é:",resultado)

    rep = input("Gostaria de converter novamente (s ou n): ")
    while rep!="s" and rep!="n" and rep!="N" and rep!="S":
        print("Digite apenas s ou n.")
        rep = input("\nGostaria de converter novamente (s ou n): ")
    if rep=="s" or rep=="S":
        main()
main()
