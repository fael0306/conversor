import bconversor

def get_valid_base():
    while True:
        try:
            base = int(input("Digite a base (apenas 2, 10 ou 16): "))
            if base in (2, 10, 16):
                return base
            print("Base inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def get_valid_number(base):
    while True:
        try:
            number = input(f"Digite um número na base {base}: ")
            if all(digit.isdigit() and int(digit, base) < base for digit in number):
                return number
            print("Número inválido para a base escolhida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar o número correto na base escolhida.")

def get_valid_destination_base(current_base):
    while True:
        try:
            dest_base = int(input(f"Digite a base para a qual deseja converter (apenas 2, 10 ou 16): "))
            if dest_base != current_base and dest_base in (2, 10, 16):
                return dest_base
            print("Base inválida ou igual à base de origem. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def main():
    while True:
        current_base = get_valid_base()
        number = get_valid_number(current_base)
        destination_base = get_valid_destination_base(current_base)
        
        try:
            if current_base == destination_base:
                resultado = number
            elif current_base == 2 and destination_base == 10:
                resultado = bconversor.bintodec(number)
            elif current_base == 2 and destination_base == 16:
                resultado = bconversor.bintohex(number)
            elif current_base == 10 and destination_base == 2:
                resultado = bconversor.dectobin(number)
            elif current_base == 10 and destination_base == 16:
                resultado = bconversor.dectohex(number)
            elif current_base == 16 and destination_base == 2:
                resultado = bconversor.hextobin(number)
            elif current_base == 16 and destination_base == 10:
                resultado = bconversor.hextodec(number)
            
            print("O resultado é:", resultado)
        except ValueError:
            print("Número provavelmente na base errada. Tente novamente.")
        
        rep = input("Gostaria de converter novamente (s ou n): ").lower()
        while rep not in ('s', 'n'):
            print("Digite apenas 's' ou 'n'.")
            rep = input("\nGostaria de converter novamente (s ou n): ").lower()
        
        if rep == "n":
            break
        
if __name__ == "__main__":
    main()
