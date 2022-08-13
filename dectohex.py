import bdectohex

def main():
    resultado = ""
    imp = 0

    while imp==0:
        try:
            imp = 1
            n = int(input("Digite um número inteiro: "))
        except:
            imp = 0
            
    aux = bdectohex.dectohex(n)

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
