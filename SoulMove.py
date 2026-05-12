import os


EMISSAO_BICICLETA = 0
EMISSAO_CARRO = 0.2
EMISSAO_METRO = 0.005
EMISSAO_MOTO = 0.08
EMISSAO_ONIBUS = 0.04 #1.30kg que o onobus emite dividio pela média de passageiros (30 pessoas)
EMISSAO_TREM = 0.005
CREDITOS_POR_PONTO = 0.009


pontos_acumulados = 0
creditos_acumulados = 0


#missoes[i][0] é no nome da missao i. 
#missoes[i][1] é os pontos da missao i.
missoes = [
    ["emita tantos carbonos", 30],
    ["Ande de 6/7 bicicletas", 10],
    ["Faça 6 viagens de tranporte publico em 7 dias", 67]
]




total_carbono_emitido = 0

def veiculo_existe(veiculo : str):
    match veiculo.lower().strip():
        case "carro": return True
        case "bicicleta": return True
        case "metro": return True
        case "moto": return True
        case "onibus": return True
        case "trem": return True
        case _: return False
        

def obter_emissao(veiculo : str):
    match veiculo.lower().strip():
        case "carro": return EMISSAO_CARRO
        case "bicicleta": return EMISSAO_BICICLETA
        case "metro": return EMISSAO_METRO
        case "moto": return EMISSAO_MOTO
        case "onibus": return EMISSAO_ONIBUS
        case "trem": return EMISSAO_TREM



def comparar_emissao(veiculo1 : str, veiculo2 : str):
    emissao1 = obter_emissao(veiculo1)
    emissao2 = obter_emissao(veiculo2)
    if emissao1 == 0 or emissao2 == 0:
        return False
    return emissao1/emissao2

def menor_emissao(veiculo1 : str, veiculo2 : str):
    emissao1 = obter_emissao(veiculo1)
    emissao2 = obter_emissao(veiculo2)
    if emissao1 < emissao2:
        return veiculo1
    return veiculo2

def calcular_viagem(veiculo : str, km : float):
    emissao = obter_emissao(veiculo)
    return emissao * km


def caso_ver_pontos():
    print(f"Pontos: {pontos_acumulados}\nCreditos: {creditos_acumulados}")
    input()

def caso_comparar_emissao():
    veiculo1 = input("Veiculo 1 (sem acentos): ")
    
    while(not veiculo_existe(veiculo1)):
        print("Veiculo  não encontrado! Tente novamente sem acentos")
        veiculo1 = input("Veiculo: ")

    veiculo2 = input("Veiculo 2 (sem acentos): ")
    while(not veiculo_existe(veiculo2)):
        print("Veiculo  não encontrado! Tente novamente sem acentos")
        veiculo2 = input("Veiculo: ")


    if obter_emissao(veiculo1) == 0 or obter_emissao(veiculo2) == 0:

        print("Bicicleta não emite carbono")

        if veiculo1.lower().strip() == "bicicleta":
            print(f"Emissao {veiculo2}: {obter_emissao(veiculo2)}")
        else:
            print(f"Emissao {veiculo1}: {obter_emissao(veiculo1)}")
        input()
        return

    diff = abs(1 - comparar_emissao(veiculo1, veiculo2))

    print(f"{veiculo1} emite {((diff * 100.00)):.2f}%", end=" ")
    print("a menos") if menor_emissao(veiculo1, veiculo2) == veiculo1 else print("a mais")
    input()
    os.system("cls")


def caso_calcular_viagem():
    veiculo = input("insira um veículo (sem acentos): ")
    while not veiculo_existe(veiculo):
        veiculo = input("Veiculo invalido!!\nInsira um veículo (sem acentos): ")
    km = float(input("Quantos quilometros deseja calcular: "))
    emissao = obter_emissao(veiculo) * km

    print(f"{veiculo} emitirá {emissao:.1f}KG de carbono em {km}KM")
    input()


def caso_verificar_emissao():
    veiculo = input("insira um veículo (sem acentos): ")
    while not veiculo_existe(veiculo):
        veiculo = input("Veiculo invalido!!\nInsira um veículo (sem acentos): ")
    emissao = obter_emissao(veiculo)
    print(f"A emissão de {veiculo} é de {emissao}KG por KM")
    input()

    


def caso_ver_missao():
    print("Missoes: ")

    for i in range(len(missoes)):
        print()
        print(f"Titulo: {missoes[i][0]}\nPontuacao: {missoes[i][1]}")
    input()


def caso_completar_missao():
    print("Qual missao gostaria de realizou?")
    for i in range(len(missoes)):
        print(f"{i+1} - {missoes[i][0]}. Pontos: {missoes[0][1]}")
    escolha = input("Input: ")
    if escolha >= 1 and escolha <= len(missoes)-1:
        pass




def caso_converter_pontos():
    pontos = input(f"Voce tem {pontos_acumulados} pontos. Quantos pontos gostaria de converter: ")
    while(not pontos.isnumeric and pontos > pontos_acumulados):
        print(f"insira um valor inteiro menor que {pontos_acumulados}: ")
        pontos = input("quantos pontos gostaria de converter: ")


os.system("cls")
nome = input("Nome: ")
os.system("cls")

escolha = -1
while not escolha == 0:
    print(f"Ola {nome}, o que deseja fazer?")

    print("1 - Ver pontos e creditos")
    print("2 - comparar a emissao de dois veiculos")
    print("3 - Calcular a emissao de uma viagem")
    print("4 - Verificar a emissao de um veiculo")
    print("5 - Ver missoes")
    print("6 - Completar missoes")
    print("7 - Converter pontos em crédito")

    print("\t0 - para sair")
    escolha = input("Input: ")

    os.system("cls")

    match escolha:
        case '1': caso_ver_pontos()

        case '2': caso_comparar_emissao()

        case '3': caso_calcular_viagem()

        case '4': caso_verificar_emissao()

        case '5': caso_ver_missao()

        case '7': caso_converter_pontos()

        case '0': break

        case _: 
            print("Opcao invalida")
            #input()



