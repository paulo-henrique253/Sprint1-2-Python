EMISSAO_BICICLETA = 0
EMISSAO_CARRO = 0.2
EMISSAO_METRO = 0.005
EMISSAO_MOTO = 0.08
EMISSAO_ONIBUS = 0.04 #1.30kg que o onobus emite dividio pela média de passageiros (30 pessoas)
EMISSAO_TREM = 0.005


total_carbono_emitido = 0

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
    return emissao1/emissao2

def calcular_viagem(veiculo : str, km : float):
    emissao = obter_emissao(veiculo)
    return emissao * km


