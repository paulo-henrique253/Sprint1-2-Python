#Emissao de veiculkos
EMISSAO_BICICLETA = 0
EMISSAO_CARRO = 0.2
EMISSAO_METRO = 0.005
EMISSAO_MOTO = 0.08
EMISSAO_ONIBUS = 0.04 #1.30kg que o onobus emite dividio pela média de passageiros (30 pessoas)
EMISSAO_TREM = 0.005


#Conversao de pontos para creditos
CREDITOS_POR_PONTO = 0.009

#MISSOES[i][0] é no nome da missao i. 
#MISSOES[i][1] é os pontos da missao i.
MISSOES = [
    ["DIÁRIA: Faça um trajeto simples (curto) de bicicleta!", 50],
    ["DIÁRIA: Faça um trajeto complexo (longo) utilizando o transporte público!", 100],
    ["DIÁRIA: Assista 5 anúncios", 50],
    ["SEMANAL: Use o transporte publico 5 dias seguidos", 350]
]
#delcaracao dos dados do usuário
class Dados:
    pontos_acumulados = 0
    creditos_acumulados = 0