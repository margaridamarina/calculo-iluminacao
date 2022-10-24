import csv


def descobre_iluminancia_recomendada(lista_ambientes):
    lista_iluminancia_recomendada = []
    for ambiente in lista_ambientes:
        tipo_ambiente = (ambiente['tipo_ambiente'])
        if tipo_ambiente in 'bB':
            iluminancia_recomendada = 200
        elif tipo_ambiente in 'cC' or tipo_ambiente in 'reuREU' or tipo_ambiente in 'tT':
            iluminancia_recomendada = 500
        elif tipo_ambiente in 'recREC':
            iluminancia_recomendada = 300
        lista_iluminancia_recomendada.append(iluminancia_recomendada)
    return lista_iluminancia_recomendada  

    
def calcula_area_ambiente(lista_ambientes):
    lista_areas_ambientes = []
    for ambiente in lista_ambientes:
        comprimento = float(ambiente['comprimento'])
        largura = float(ambiente['largura'])
        area_ambiente = (comprimento * largura)
        lista_areas_ambientes.append(area_ambiente)
    return lista_areas_ambientes


def calcula_indice_local_exato(lista_ambientes):
    lista_indices_exatos = []
    for ambiente in lista_ambientes:
        comprimento = float(ambiente['comprimento'])
        largura = float(ambiente['largura'])
        altura_trabalho = float(ambiente['altura_trabalho'])
        indice_exato = (comprimento * largura / ((comprimento + largura) * altura_trabalho))
        lista_indices_exatos.append(indice_exato)
    return lista_indices_exatos


def calcula_indice_local_tabela(lista_ambientes):
    lista_indices_exatos = calcula_indice_local_exato(lista_ambientes)
    lista_indices_tabela = [0.6, 0.8, 1, 1.25, 1.5, 2, 2.5, 3, 4, 5]
    lista_indicetabela_indiceexato_diferenca = []
    lista_indicetabela_menor_diferenca = []
    for indice_exato in lista_indices_exatos:
        for indice_tabela in lista_indices_tabela:
            indicetabela_indiceexato_diferenca = abs(indice_tabela - indice_exato)
            lista_indicetabela_indiceexato_diferenca.append(indicetabela_indiceexato_diferenca)
            menor_diferenca = min(lista_indicetabela_indiceexato_diferenca)
            posicao_menor_diferenca = lista_indicetabela_indiceexato_diferenca.index(menor_diferenca)
        lista_indicetabela_menor_diferenca.append(lista_indices_tabela[posicao_menor_diferenca])
    return lista_indicetabela_menor_diferenca


def descobre_refletancia():
    lista_indice_refletancia = []
    for ambiente in lista_ambientes:
        cor_teto = ambiente['cor_teto']
        cor_parede = ambiente['cor_parede']
        refletancia_teto = ''
        refletancia_parede = '' 
        refletancia_piso = '1' 
        
        if cor_teto in 'bB':
            refletancia_teto = '7'
        elif cor_teto in 'cC':
            refletancia_teto = '5'
        elif cor_teto in 'eE':
            refletancia_teto = '3'
        
        if cor_parede in 'bB':
            refletancia_parede = '5'
        elif cor_parede in 'cC':
            refletancia_parede = '3'
        elif cor_parede in 'eE':
            refletancia_parede = '1'
        
        indice_refletancia = refletancia_teto, refletancia_parede, refletancia_piso
        indice_refletancia = ''.join(indice_refletancia)
        lista_indice_refletancia.append(indice_refletancia)
    return lista_indice_refletancia


def descobre_fator_utilizacao(lista_itabela_menor_dif, lista_irefletancia):
    arquivo = open('fator_utilizacao_tcs029_32w.csv')
    arquivo_lido = list(csv.DictReader(arquivo))
    lista_fatores_utilizacao = []
    for (i, indice_tabela) in enumerate(lista_itabela_menor_dif):
      for linha_fator_utilizacao in arquivo_lido:
        refletancia = lista_irefletancia[i]
        if float(linha_fator_utilizacao['K']) == indice_tabela:
            fator_utilizacao = linha_fator_utilizacao[str(refletancia)]
            lista_fatores_utilizacao.append(fator_utilizacao)
    return lista_fatores_utilizacao
    

def calcula_total_lumens(iluminancia_rec, areas, fator_utiliz):
    iluminancia_recomendada = int(iluminancia_rec)
    area_ambiente = float(areas)
    fator_utilizacao_luminaria = float(fator_utiliz)
    fator_depreciacao_luminaria = 0.85
    return (iluminancia_recomendada * area_ambiente) / (fator_utilizacao_luminaria * fator_depreciacao_luminaria)


def calcula_qtd_luminarias(lista_ambientes):
    iluminancia_recomendada = descobre_iluminancia_recomendada(lista_ambientes)
    area_ambiente = calcula_area_ambiente(lista_ambientes)
    fator_utilizaca = descobre_fator_utilizacao(calcula_indice_local_tabela(lista_ambientes), descobre_refletancia())
    # Refatorar para deixar as funcoes recebendo argumentos como valores unicos em vez de listas
    lista_total_lumens = []
    for i in range(len(lista_ambientes)):
       total_lumens = calcula_total_lumens(iluminancia_recomendada[i], area_ambiente[i], fator_utilizaca[i])
       lista_total_lumens.append(total_lumens)
    lista_qtd_luminarias = []
    lista_lumens_por_luminaria = []
    for i in range(qtd_ambientes):
        lumens_por_luminaria = int(lista_ambientes[i]['lumens_por_luminaria'])
        lista_lumens_por_luminaria.append(lumens_por_luminaria)
        qtd_luminarias = round(lista_total_lumens[i] / lumens_por_luminaria)
        lista_qtd_luminarias.append(qtd_luminarias)
    return lista_qtd_luminarias


if __name__=='__main__':
    qtd_ambientes = int(input('Quantos ambientes deseja informar? '))
    lista_ambientes = []
    for _ in range(qtd_ambientes):
        info_ambiente = {}
        info_ambiente['comprimento'] = input('Qual o comprimento do ambiente? ')
        info_ambiente['largura'] = input('Qual a largura do ambiente? ')
        info_ambiente['altura_trabalho'] = input('Qual a altura de trabalho (altura da mesa ou da bancada)? ')
        info_ambiente['cor_teto'] = input('Qual a cor do teto no ambiente (B para branco, C para claro, E para escuro)? ')
        info_ambiente['cor_parede'] = input('Qual a cor da parede no ambiente (B para branca, C para clara, E para escura)? ')
        info_ambiente['tipo_ambiente'] = input('Qual o tipo de ambiente (B para banheiro, C para copa, REU para sala de reuniao, T para sala de trabalho, REC para recepcao)? ')
        info_ambiente['lumens_por_luminaria'] = input('Quantos lumens possui cada luminaria? ')
        lista_ambientes.append(info_ambiente)
        print('~~~~')
    lista_qtd_lum = calcula_qtd_luminarias(lista_ambientes)
    for i in range(qtd_ambientes):
        if lista_ambientes[i]['tipo_ambiente'] in 'bB':
            ambiente = 'Banheiro:'
        elif lista_ambientes[i]['tipo_ambiente'] in 'cC':
            ambiente = 'Copa:'
        elif lista_ambientes[i]['tipo_ambiente'] in 'reuREU':
            ambiente = 'Sala de reunião:'
        elif lista_ambientes[i]['tipo_ambiente'] in 'tT':
            ambiente = 'Sala de trabalho:'
        elif lista_ambientes[i]['tipo_ambiente'] in 'recREC':
            ambiente = 'Recepção:'
        print(ambiente, lista_qtd_lum[i], 'luminárias')
