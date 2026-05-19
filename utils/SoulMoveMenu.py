# SUBALGORITMOS CHAMADOS NO MENU
import utils.SoulMoveFuncs as funcs
import utils.SoulMoveInfo as info
import os

# Ver pontos e creditos acumulados
def caso_ver_pontos() -> None:
    print(f"⌞ .✦ ݁˖ Pontos: {info.Dados.pontos_acumulados} ⌝\n⌞ ⊹ ࣪ ˖ Creditos: R${(info.Dados.creditos_acumulados):.2f} ⌝")
    print("\n » Insira qualquer tecla para continuar.")
    input()

# Comparar a emissao entre 2 veiculos
def caso_comparar_emissao() -> None:
    veiculo1 = input("⋮ » Veículo 1 (sem acentos): ")

    while(not funcs.veiculo_existe(veiculo1)): #Força o usuário a colocar um veiculo cadastrado
        print("▸ Veículo não encontrado! Tente novamente sem acentos")
        veiculo1 = input(" » Veículo: ")

    veiculo2 = input("⋮ » Veículo 2 (sem acentos): ")

    while(not funcs.veiculo_existe(veiculo2) or veiculo1.lower().strip() == veiculo2.lower().strip()): # Forca o Veiculo2 a ser cadastrado E ser diferente do veiculo1

        if veiculo1.lower().strip() == veiculo2.lower().strip(): #caso veiculos iguais
            print("▸ Os veículos não podem ser iguais! Digite outro veículo.")

        else: # Se não, veiculo2 nao existe
            print("▸ Veículo não encontrado! Tente novamente sem acentos")

        veiculo2 = input(" » Veículo 2: ")

     #garantir a não divisão por 0
    if funcs.obter_emissao(veiculo1) == 0 or funcs.obter_emissao(veiculo2) == 0:

        print(".ᐟ ⌞ Bicicleta não emite carbono ⌝ .ᐟ")

        # Mostrar a emissao do veiculo que não emite 0 (bicicleta)
        if veiculo1.lower().strip() == "bicicleta": 
            print(f"⋮ » ⌞ Emissao {veiculo2}: {funcs.obter_emissao(veiculo2)} ⌝")
        else:
            print(f"Emissao {veiculo1}: {funcs.obter_emissao(veiculo1)} ⌝")

        print("\n » Insira qualquer tecla para continuar.")
        input()
        return

    #comparar veiculos
    diff = abs(1 - funcs.comparar_emissao(veiculo1, veiculo2))

    # Mostrar diferenca
    print(f"⋮ » ⌞ {veiculo1} emite {((diff * 100.00)):.2f}%", end=" ")
    print("a menos ⌝") if funcs.menor_emissao(veiculo1, veiculo2) == veiculo1 else print("a mais ⌝")

    print("\n » Insira qualquer tecla para continuar.")
    input()
    os.system("cls")


# Calcula a emissao de um veiculo em determinada distância
def caso_calcular_viagem() -> None:

    veiculo = input("⋮ » Insira um veículo (sem acentos): ")

    while not funcs.veiculo_existe(veiculo): #Força o usuário a colocar um veiculo cadastrado
        veiculo = input("▸ Veículo invalido!!\n⋮ » Insira um veículo (sem acentos): ")

    km = input("⋮ » Quantos quilometros deseja calcular: ")

    while (not funcs.is_float(km)): #Força o usuário a colocar um numero na quilometragem
        km = input("⋮ » Insira uma quilometragem válida: ")

    #Obtem a emissao na distancia descrita
    emissao = funcs.obter_emissao(veiculo) * float(km)

    print(f"⋮ » ⌞ {veiculo} emitirá {emissao:.1f}KG de carbono em {km}KM ⌝")
    
    print("\n » Insira qualquer tecla para continuar.")
    input()

# Verificar quanto um veiculo emite
def caso_verificar_emissao() -> None:

    veiculo = input("⋮ » Insira um veículo (sem acentos): ")

    while not funcs.veiculo_existe(veiculo): #Força o usuário a colocar um veiculo cadastrado
        veiculo = input("▸ Veiculo invalido!!\n⋮ » Insira um veículo (sem acentos): ")

    # Exibe a emissao por km por pessoa
    emissao = funcs.obter_emissao(veiculo)
    print(f"⋮ » ⌞ A emissão de {veiculo} é de {emissao}KG por KM ⌝")
    
    print("\n » Insira qualquer tecla para continuar.")
    input()

    

# Ver missoes cadastradas
def caso_ver_missao() -> None:
    print(".✦ ݁˖ Missões: ")

    #Para cada missao
    for i in range(len(info.MISSOES)):
        #exibe o titulo e a pontuação
        print()
        print(f"⌞ ⋮ » Titulo: {info.MISSOES[i][0]} ⌝ \n ⊹ ࣪ ˖ Pontuacao: {info.MISSOES[i][1]} ")

    print("\n » Insira qualquer tecla para continuar.")
    input()

# Adiciona os pontos da missao aos pontos acumulados
def caso_completar_missao() -> None:

    print("⌞ Qual missao gostaria de registrar? ⌝")

    #para cada missao
    for i in range(len(info.MISSOES)):
        #Exibir infos da missao
        print(f"\n⌞ ⋮ » {i+1} - {info.MISSOES[i][0]}. Pontos: {info.MISSOES[i][1]}⌝")

    escolha = input(".ᐟ.ᐟ ─── Escolha: ")

    #força o usuário a colocar uma das opções
    while True:

        if escolha.isnumeric():
            escolha = int(escolha)
            if escolha >= 1 and escolha <= len(info.MISSOES):
                break

        print("escolha invalida !!!")
        escolha = input(".ᐟ.ᐟ ─── Escolha: ")

    # Adiciona os pontos da missao nos pontos do usuário
    info.Dados.pontos_acumulados += info.MISSOES[escolha-1][1]
    print(f"\n⋮ » ⌞ Missao Concluida.\nAgora voce tem {info.Dados.pontos_acumulados} pontos ⌝")


    print("\n » Insira qualquer tecla para continuar.")
    input()

    #Retorna os pontos para que possam ser colocados no programa principal



# Converte quantos pontos quiser em creditos
def caso_converter_pontos() -> None:

    pontos = input(f"⋮ » Voce tem {info.Dados.pontos_acumulados} pontos. Quantos pontos gostaria de converter: ")
    
    #forca o usuário a digitar um numero menor que a quantidade de pontos atual
    #Se pontos for numerico, verifica se é menor que os pontos acumulados e se sim atribui True, se não  for numerico nao checa e atribui falso
    valido = True if pontos.isnumeric() and int(pontos) <= info.Dados.pontos_acumulados else False
    while(not valido): 

        print(f"▸ Insira um valor inteiro menor que {info.Dados.pontos_acumulados}: ")
        pontos = input("⋮ » Quantos pontos gostaria de converter: ")

        valido = True if pontos.isnumeric() and int(pontos) <= info.Dados.pontos_acumulados else False

    #Muda as variavies temporárias
    info.Dados.pontos_acumulados -= int(pontos)
    info.Dados.creditos_acumulados += float(pontos) * info.CREDITOS_POR_PONTO

    print(f"▸ Isso equivale a {float(pontos) * info.CREDITOS_POR_PONTO:.2f} creditos\n ⟢ ⌞ Você tem R${(info.Dados.creditos_acumulados):.2f} ⌝ de créditos.")

    print("\n » Insira qualquer tecla para continuar.")
    input()
    # Retorna ambos os valores para que possam ser tratados no codigo principal
    
    

