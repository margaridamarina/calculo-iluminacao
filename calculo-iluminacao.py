import csv


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


def descobre_iluminancia_recomendada():
    lista_iluminancia_recomendada = []
    for _ in range(qtd_ambientes):
        tipo_ambiente = (lista_ambientes[_]['tipo_ambiente'])
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
    for _ in range(qtd_ambientes):
        comprimento = float(lista_ambientes[_]['comprimento'])
        largura = float(lista_ambientes[_]['largura'])
        area_ambiente = (comprimento * largura)
        lista_areas_ambientes.append(area_ambiente)
    return lista_areas_ambientes


def calcula_indice_local_exato():
    calcula_area_ambiente(lista_ambientes)
    lista_indices_exatos = []
    for _ in range(qtd_ambientes):
        comprimento = float(lista_ambientes[_]['comprimento'])
        largura = float(lista_ambientes[_]['largura'])
        altura_trabalho = float(lista_ambientes[_]['altura_trabalho'])
        indice_exato = (comprimento * largura / ((comprimento + largura) * altura_trabalho))
        lista_indices_exatos.append(indice_exato)
    return lista_indices_exatos