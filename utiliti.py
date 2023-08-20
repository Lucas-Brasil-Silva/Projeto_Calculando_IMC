import json

def calcular_imc(altura, peso):
    altura_ = int(altura)/100
    peso_ = [float(peso.replace(',','.')) if any(letra in peso for letra in [',','.']) else int(peso)]
    resposta = (peso_[0]/(altura_**2))
    return resposta

def imc_infantil(imc,idade,sexo):
    with open('imc_infantil.json','r',encoding='utf-8') as arquivo:
        dados_imc_infantil = json.load(arquivo)
    if sexo in 'Masculino':
        resultado = [dados_imc_infantil['Masculino'][idade][dado] for dado in dados_imc_infantil['Masculino'][idade] if imc <= float(dado)]
        if not resultado:
            return 'OBESIDADE'
        return resultado[0]
    else:
        resultado = [dados_imc_infantil['Feminino'][idade][dado] for dado in dados_imc_infantil['Feminino'][idade] if imc <= float(dado)]
        if not resultado:
            return 'OBESIDADE'
        return resultado[0]

def imc_adulto(imc):
    with open('imc_adulto.json','r',encoding='utf-8') as arquivo:
        dados_imc_adulto = json.load(arquivo)
    resultado = [dados_imc_adulto[dado] for dado in dados_imc_adulto if imc <= float(dado)]
    if not resultado:
        return 'OBESIDADE GRAU 3'
    return resultado[0]

def imc_senil(imc):
    with open('imc_senil.json','r',encoding='utf-8') as arquivo:
        dados_imc_senil = json.load(arquivo)
    resultado = [dados_imc_senil[dado] for dado in dados_imc_senil if imc <= float(dado)]
    if not resultado:
        return 'OBESIDADE'
    return resultado[0]

def resultado_imc(sexo,idade,altura,peso):
    with open('color_status.json','r',encoding='utf-8') as arquivo:
        dados_color = json.load(arquivo) 

    imc = calcular_imc(altura,peso)
    imc_formatado = "{:.2f}".format(imc)
    
    if float(idade) <= 15:
        status = imc_infantil(imc,idade,sexo)
        color = dados_color[status]
        return status, imc_formatado, color
    
    elif float(idade) < 60:
        status = imc_adulto(imc)
        color = dados_color[status]
        imc_ideal = 21.70
        peso_ideal = f"{'{:.2f}'.format(imc_ideal*((int(altura)/100)**2)) if not status in 'PESO NORMAL' else ''}"
        return status, imc_formatado, color, peso_ideal
    
    else:
        status = imc_senil(imc)
        color = dados_color[status]
        imc_ideal = 24.50
        peso_ideal = f"{'{:.2f}'.format(imc_ideal*((int(altura)/100)**2)) if not status in 'PESO NORMAL' else ''}"
        return status, imc_formatado, color, peso_ideal