import os

#DECLARACAO DE CONSTANTES

#Emissao de veiculkos
EMISSAO_BICICLETA = 0
EMISSAO_CARRO = 0.2
EMISSAO_METRO = 0.005
EMISSAO_MOTO = 0.08
EMISSAO_ONIBUS = 0.04 #1.30kg que o onobus emite dividio pela média de passageiros (30 pessoas)
EMISSAO_TREM = 0.005


#Conversao de pontos para creditos
CREDITOS_POR_PONTO = 0.009

#delcaracao dos atributos do usuário
pontos_acumulados = 0
creditos_acumulados = 0


#missoes[i][0] é no nome da missao i. 
#missoes[i][1] é os pontos da missao i.
missoes = [
    ["DIÁRIA: Faça um trajeto simples (curto) de bicicleta!", 50],
    ["DIÁRIA: Faça um trajeto complexo (longo) utilizando o transporte público!", 100],
    ["DIÁRIA: Assista 5 anúncios", 50],
    ["SEMANAL: Use o transporte publico 5 dias seguidos", 350]
]

#verificar se uma string é um float valido
def is_float(texto : str):
    pontos = 0
    for char in texto:
        if char == '.': pontos +=1
        elif not char.isdigit(): return False
    if pontos <= 1:
        return True  
    else: 
        return False




# verificar se o veiculo é um dos cadastrados
def veiculo_existe(veiculo : str):
    match veiculo.lower().strip():
        case "carro": return True
        case "bicicleta": return True
        case "metro": return True
        case "moto": return True
        case "onibus": return True
        case "trem": return True
        case _: return False
        
# obter a emissao de um veiculo
def obter_emissao(veiculo : str):
    match veiculo.lower().strip():
        case "carro": return EMISSAO_CARRO
        case "bicicleta": return EMISSAO_BICICLETA
        case "metro": return EMISSAO_METRO
        case "moto": return EMISSAO_MOTO
        case "onibus": return EMISSAO_ONIBUS
        case "trem": return EMISSAO_TREM


# Comparar a emissao de um veiculo com outro 
def comparar_emissao(veiculo1 : str, veiculo2 : str):
    emissao1 = obter_emissao(veiculo1)
    emissao2 = obter_emissao(veiculo2)
    if emissao1 == 0 or emissao2 == 0:
        return False
    return emissao1/emissao2


# Verificar qual é a menor emissao entre dois veiculos
def menor_emissao(veiculo1 : str, veiculo2 : str):
    emissao1 = obter_emissao(veiculo1)
    emissao2 = obter_emissao(veiculo2)
    if emissao1 < emissao2:
        return veiculo1
    return veiculo2



# Retorna a emissao total que um veiculo faria ao andar determinada distancia em km
def calcular_viagem(veiculo : str, km : float):
    emissao = obter_emissao(veiculo)
    return emissao * km


# SUBALGORITMOS CHAMADOS NO MENU


def caso_ver_pontos():
    print(f"⌞ .✦ ݁˖ Pontos: {pontos_acumulados} ⌝\n⌞ ⊹ ࣪ ˖ Creditos: R${creditos_acumulados} ⌝")
    print("\n » Insira qualquer tecla para continuar.")
    input()

def caso_comparar_emissao():
    veiculo1 = input("⋮ » Veículo 1 (sem acentos): ")

    while(not veiculo_existe(veiculo1)):
        print("▸ Veículo não encontrado! Tente novamente sem acentos")
        veiculo1 = input(" » Veículo: ")

    veiculo2 = input("⋮ » Veículo 2 (sem acentos): ")

    while(not veiculo_existe(veiculo2) or veiculo1.lower().strip() == veiculo2.lower().strip()):

        if veiculo1.lower().strip() == veiculo2.lower().strip():
            print("▸ Os veículos não podem ser iguais! Digite outro veículo.")
        else:
            print("▸ Veículo não encontrado! Tente novamente sem acentos")

        veiculo2 = input(" » Veículo 2: ")

    if obter_emissao(veiculo1) == 0 or obter_emissao(veiculo2) == 0:

        print(".ᐟ ⌞ Bicicleta não emite carbono ⌝ .ᐟ")

        if veiculo1.lower().strip() == "bicicleta":
            print(f"⋮ » ⌞ Emissao {veiculo2}: {obter_emissao(veiculo2)} ⌝")
        else:
            print(f"Emissao {veiculo1}: {obter_emissao(veiculo1)} ⌝")

        print("\n » Insira qualquer tecla para continuar.")
        input()
        return

    diff = abs(1 - comparar_emissao(veiculo1, veiculo2))

    print(f"⋮ » ⌞ {veiculo1} emite {((diff * 100.00)):.2f}%", end=" ")
    print("a menos ⌝") if menor_emissao(veiculo1, veiculo2) == veiculo1 else print("a mais ⌝")

    print("\n » Insira qualquer tecla para continuar.")
    input()
    os.system("cls")


def caso_calcular_viagem():
    veiculo = input("⋮ » Insira um veículo (sem acentos): ")
    while not veiculo_existe(veiculo):
        veiculo = input("▸ Veículo invalido!!\n⋮ » Insira um veículo (sem acentos): ")
    km = input("⋮ » Quantos quilometros deseja calcular: ")
    while (not is_float(km)):
        km = input("⋮ » Insira uma quilometragem válida: ")
    emissao = obter_emissao(veiculo) * float(km)

    print(f"⋮ » ⌞ {veiculo} emitirá {emissao:.1f}KG de carbono em {km}KM ⌝")
    
    print("\n » Insira qualquer tecla para continuar.")
    input()


def caso_verificar_emissao():
    veiculo = input("⋮ » Insira um veículo (sem acentos): ")
    while not veiculo_existe(veiculo):
        veiculo = input("▸ Veiculo invalido!!\n⋮ » Insira um veículo (sem acentos): ")
    emissao = obter_emissao(veiculo)
    print(f"⋮ » ⌞ A emissão de {veiculo} é de {emissao}KG por KM ⌝")
    
    print("\n » Insira qualquer tecla para continuar.")
    input()

    


def caso_ver_missao():
    print(".✦ ݁˖ Missões: ")

    for i in range(len(missoes)):
        print()
        print(f"⌞ ⋮ » Titulo: {missoes[i][0]} ⌝ \n ⊹ ࣪ ˖ Pontuacao: {missoes[i][1]} ")

    print("\n » Insira qualquer tecla para continuar.")
    input()


def caso_completar_missao():
    global pontos_acumulados
    print("⌞ Qual missao gostaria de registrar? ⌝")
    for i in range(len(missoes)):
        print(f"\n⌞ ⋮ » {i+1} - {missoes[i][0]}. Pontos: {missoes[i][1]}⌝")
    escolha = int(input(".ᐟ.ᐟ ─── Escolha: "))
    if escolha >= 1 and escolha <= len(missoes):

        pontos_acumulados += missoes[escolha-1][1]
        print(f"\n⋮ » ⌞ Missao Concluida.\nAgora voce tem {pontos_acumulados} pontos ⌝")
    else:
        print("▸ Missão invalida")

    print("\n » Insira qualquer tecla para continuar.")
    input()




def caso_converter_pontos():
    global pontos_acumulados
    global creditos_acumulados
    pontos = input(f"⋮ » Voce tem {pontos_acumulados} pontos. Quantos pontos gostaria de converter: ")
    while(not pontos.isnumeric and pontos > pontos_acumulados):
        print(f"▸ Insira um valor inteiro menor que {pontos_acumulados}: ")
        pontos = input("⋮ » Quantos pontos gostaria de converter: ")
    pontos_acumulados -= int(pontos)
    creditos_acumulados += float(pontos) * CREDITOS_POR_PONTO
    print(f"▸ Isso equivale a {float(pontos) * CREDITOS_POR_PONTO:.2f} creditos\n ⟢ ⌞ Você tem R${creditos_acumulados:.2f} ⌝ de créditos.")

    print("\n » Insira qualquer tecla para continuar.")
    input()
    
    


os.system("cls")
nome = input(".ᐟ.ᐟ ─── Insira seu nome: ")
os.system("cls")

escolha = -1
while escolha != 0:
    print(f"⌞ Ola {nome}, o que deseja fazer? ⌝")
    print("\n")
    print("\t" + "⋮ ┆ 1 - Ver pontos e créditos")
    print("\t" + "⋮ ┆ 2 - Comparar a emissão de dois veiculos")
    print("\t" + "⋮ ┆ 3 - Calcular a emissão de uma viagem")
    print("\t" + "⋮ ┆ 4 - Verificar a emissão de um veiculo")
    print("\t" + "⋮ ┆ 5 - Ver missões disponíveis")
    print("\t" + "⋮ ┆ 6 - Completar uma missão")
    print("\t" + "⋮ ┆ 7 - Converter pontos em crédito")
    print("\t" + "⋮ ┆ 0 - Sair do programa")
    print("\n")

    escolha = input(".ᐟ.ᐟ ─── Insira a opção: ")

    os.system("cls")

    match escolha:
        case '1': 
            caso_ver_pontos()
            print("\n")

        case '2': 
            caso_comparar_emissao()
            print("\n")

        case '3': 
            caso_calcular_viagem()
            print("\n")

        case '4': 
            caso_verificar_emissao()
            print("\n")

        case '5': 
            caso_ver_missao()
            print("\n")

        case '6': 
            caso_completar_missao()
            print("\n")

        case '7': 
            caso_converter_pontos()
            print("\n")

        case '0': break

        case _: 
            print("▸ Opção invalida!")
            print("\n")
            #input()



