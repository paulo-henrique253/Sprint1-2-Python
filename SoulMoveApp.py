import os
import utils.SoulMoveInfo as info
import utils.SoulMoveMenu as menu
#DECLARACAO DE CONSTANTES

# Analisa se a nota 1 é um número e é válida: True se for False se não for

#delcaracao dos atributos do usuário
pontos_acumulados = 0
creditos_acumulados = 0


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
            menu.caso_ver_pontos(pontos_acumulados, creditos_acumulados)
            print("\n")

        case '2': 
            menu.caso_comparar_emissao()
            print("\n")

        case '3': 
            menu.caso_calcular_viagem()
            print("\n")

        case '4': 
            menu.caso_verificar_emissao()
            print("\n")

        case '5': 
            menu.caso_ver_missao()
            print("\n")

        case '6': 
            pontos_acumulados = menu.caso_completar_missao(pontos_acumulados)
            print("\n")

        case '7': 
            retorno = menu.caso_converter_pontos(pontos_acumulados, creditos_acumulados)
            pontos_acumulados = retorno[0]
            creditos_acumulados = retorno[1]
            print("\n")

        case '0': break

        case _: 
            print("▸ Opção invalida!")
            print("\n")
            #input()



