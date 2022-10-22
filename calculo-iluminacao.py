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
