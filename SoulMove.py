import os


EMISSAO_BICICLETA = 0
EMISSAO_CARRO = 0.2
EMISSAO_METRO = 0.005
EMISSAO_MOTO = 0.08
EMISSAO_ONIBUS = 0.04 #1.30kg que o onobus emite dividio pela média de passageiros (30 pessoas)
EMISSAO_TREM = 0.005


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


def caso_comparar_emissao():
    veiculo1 = input("(sem acentos)Veiculo 1: ")
    
    while(not veiculo_existe(veiculo1)):
        print("Veiculo  não encontrado! Tente novamente sem acentos")
        veiculo1 = input("Veiculo: ")

    veiculo2 = input("(sem acentos)Veiculo 2: ")
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


os.system("cls")
nome = input("Nome: ")
os.system("cls")

escolha = -1
while not escolha == 0:
    print(f"Ola {nome}, o que deseja fazer?")
    print("1- comparar a emissao de dois veiculos")
    print("2 - Calcular a emissao de 2 viagens")
    print("3 - Verificar a emissao de um veiculo")
    print("\t0 - para sair")
    escolha = int(input())
    os.system("cls")
    match escolha:
        case 1: caso_comparar_emissao()



