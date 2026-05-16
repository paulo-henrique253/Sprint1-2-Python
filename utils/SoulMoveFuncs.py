import utils.SoulMoveInfo as info



#verificar se uma string é um float valido
def is_float(texto : str) -> bool:

    #String vazia
    if len(texto) == 0:
        return False

    #contador de pontos na string
    pontos = 0
    for char in texto:
        #se encontrar um ponto, conta ele
        if char == '.': pontos +=1
        #Se o caractér nao for ponto nem numero, então nem numero é, retorna falso 
        elif not char.isdigit(): return False
    
    #se tiver um ou nenhum ponto, e todos os digitos forem numeros, é um float válido
    if pontos <= 1:
        return True  
    else: 
        return False




# verificar se o veiculo é um dos cadastrados
def veiculo_existe(veiculo : str) -> bool:

    match veiculo.lower().strip():

        case "carro": return True
        case "bicicleta": return True
        case "metro": return True
        case "moto": return True
        case "onibus": return True
        case "trem": return True
        case _: return False
        
# obter a emissao de um veiculo
def obter_emissao(veiculo : str) -> float:

    match veiculo.lower().strip():

        case "carro": return info.EMISSAO_CARRO
        case "bicicleta": return info.EMISSAO_BICICLETA
        case "metro": return info.EMISSAO_METRO
        case "moto": return info.EMISSAO_MOTO
        case "onibus": return info.EMISSAO_ONIBUS
        case "trem": return info.EMISSAO_TREM


# Comparar a emissao de um veiculo com outro 
def comparar_emissao(veiculo1 : str, veiculo2 : str) -> float:

    #obtem ambas as emissoes
    emissao1 = obter_emissao(veiculo1)
    emissao2 = obter_emissao(veiculo2)

    #retorna falso em caso de divisao por 0
    if emissao1 == 0 or emissao2 == 0:
        return False
    #Retorna a razão entre elas
    return emissao1/emissao2


# Verificar qual é a menor emissao entre dois veiculos
def menor_emissao(veiculo1 : str, veiculo2 : str) -> str:
    
    #Obtem ambas as emissoes
    emissao1 = obter_emissao(veiculo1)
    emissao2 = obter_emissao(veiculo2)

    #Se a primeira for menor, retorna o primeiro veiculo, se nao retorna o segundo
    if emissao1 < emissao2:
        return veiculo1
    return veiculo2



# Retorna a emissao total que um veiculo faria ao andar determinada distancia em km
def calcular_viagem(veiculo : str, km : float) -> float:

    #obtem a emissao 
    emissao = obter_emissao(veiculo)

    #multiplica a emissao pela distancia
    return emissao * km

