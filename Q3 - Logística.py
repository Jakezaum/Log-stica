# Início da função dimensoesObjeto
def dimensoesObjeto():
    print("------------ Dimensões do objeto ------------")
    global acumulador
    while True:
        try: #Identificação como variável
            RU4393710 = int(input("Digite a altura do objeto (em cm): ")) # Primeiras perguntas
            comprimento = int(input("Digite o comprimento do objeto (em cm): "))
            largura = int(input("Digite a largura do objeto (em cm): "))
            volume = RU4393710 * comprimento * largura
            if volume < 1000:
                print("O volume do objeto (em cm³) é: {}\n".format(volume))
                return 10
            elif 1000 <= volume < 10000:
                print("O volume do objeto (em cm³) é: {}\n".format(volume))
                return 20
            elif 10000 <= volume < 30000:
                print("O volume do objeto (em cm³) é: {}\n".format(volume))
                return 30
            elif 30000 <= volume < 100000:
                print("O volume do objeto (em cm³) é: {}\n".format(volume))
                return 50
            else:
                print("O volume do objeto (em cm³) é: {}".format(volume))
                print("   Não aceitamos objetos com dimensões tão grandes.\n   Entre com as dimensões desejadas novamente.")
                continue # Volta às primeiras perguntas
        except ValueError:
            print("   Você digitou alguma dimensão do objeto com valor não numérico.\n   Por favor, tente novamente...")
# Fim da função dimensoesObjeto

# Início da função pesoObjeto
def pesoObjeto():
    print("-------------- Peso do objeto --------------")
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em Kg): ")) # Pergunta 2
            if peso <= 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso <= 30:
                return 3
            else:
                print("   Não aceitamos objetos com mais de 30Kg.\n   Entre com o peso desejado novamente.\n")
                continue
        except ValueError:
            print("   Você digitou o peso do objeto com valor não numérico.\n   Por favor, tente novamente...\n")
            continue # Volta à pergunta 2
# Fim da função pesoObjeto

# Início da função rotaObjeto
def rotaObjeto():
    print("\n------------- Rota do objeto -------------")
    print("Escolha a rota desejada utilizando as\nseguintes siglas:\n")
    print("+-----------------------------------------+")
    print("|  BR - De Brasília para Rio de Janeiro.  |")
    print("|  BS - De Brasília para São Paulo.       |")
    print("|  RB - De Rio de Janeiro para Brasília.  |")
    print("|  RS - De Rio de Janeiro para São Paulo. |")
    print("|  SR - De São Paulo para Rio de Janeiro. |")
    print("|  SB - De São Paulo para Brasília.       |")
    print("+-----------------------------------------+")
    while True:
        try:
            rota = input('>> ')
            if rota == "RS":
                return 1
            elif rota == "SR":
                return 1
            elif rota == "BS":
                return 1.2
            elif rota == "SB":
                return 1.2
            elif rota == "BR":
                return 1.5
            elif rota == "RB":
                return 1.5
        except:
            print("A rota escolhida não consta em nosso sistema. Tente novamente.")
            continue
# Fim da função rotaObjeto

#Programa Principal
print("Seja bem-vindo(a) à Transportadora Maluche!")
dms = dimensoesObjeto()
ps = pesoObjeto()
rt = rotaObjeto()
valor = dms * rt * ps
print("Total a pagar(R$): {} (dimensões: {} x peso: {} x rota: {} )" .format(valor, dms, ps, rt))
