import bconversor

def main():
    resultado = ""
    imp = 0
    imp2 = 0
    b2 = 0

    while imp2==0:
        try:
            imp2 = 1
            b = int(input("Digite a base (apenas 2, 10 ou 16): "))
            while b!=2 and b!=10 and b!=16:
                b = int(input("Digite a base (apenas 2, 10 ou 16, por favor): "))
        except:
            imp2 = 0

    while imp==0:
        try:
            imp = 1
            n = input("Digite um número na base escolhida: ")
            if b==2:
                while b2!=10 and b2!=16:
                    b2 = int(input("Digite a base para o qual deseja convertê-lo (apenas 10 ou 16, por favor): "))
            if b==10:
                while b2!=2 and b2!=16:
                    b2 = int(input("Digite a base para o qual deseja convertê-lo (apenas 2 ou 16, por favor): "))
            if b==16:
                while b2!=2 and b2!=10:
                    b2 = int(input("Digite a base para o qual deseja convertê-lo (apenas 2 ou 10, por favor): "))
        except:
            imp = 0
            print("\nDigite um número na base correta")

    try:
        if b==2 and b2==2:
            resultado = n
        if b==2 and b2==10:
            resultado = bconversor.bintodec(n)
        if b==2 and b2==16:
            resultado = bconversor.bintohex(n)
        if b==10 and b2==2:
            resultado = bconversor.dectobin(n)
        if b==10 and b2==10:
            resultado = n
        if b==10 and b2==16:
            resultado = bconversor.dectohex(n)
        if b==16 and b2==2:
            resultado = bconversor.hextobin(n)
        if b==16 and b2==10:
            resultado = bconversor.hextodec(n)
        if b==16 and b2==16:
            resultado = n
    except:
            print("Número provavelmente na base errada. Tente novamente.")
            main()
        
    print("O resultado é:",resultado)

    rep = input("Gostaria de converter novamente (s ou n): ")
    while rep!="s" and rep!="n" and rep!="N" and rep!="S":
        print("Digite apenas s ou n.")
        rep = input("\nGostaria de converter novamente (s ou n): ")
    if rep=="s" or rep=="S":
        main()
main()
