import csv


class Ambiente:
    largura = 0
    distancia_mesa_luminaria = 0
    comprimento = 0
    lumen_luminaria = 0
    tipo_ambiente = ''
    cor_teto = ''
    cor_parede = ''

    def __init__(self, largura = 0, distancia_mesa_luminaria = 0, comprimento = 0, lumen_luminaria = 0, cor_teto = '', cor_parede = '', tipo_ambiente=''):
        self.largura = largura
        self.distancia_mesa_luminaria = distancia_mesa_luminaria
        self.lumen_luminaria = lumen_luminaria
        self.cor_teto = cor_teto
        self.cor_parede = cor_parede
        self.tipo_ambiente = tipo_ambiente
        self.comprimento = comprimento

    def descobre_iluminancia_recomendada(self):
        tipo_ambiente = self.tipo_ambiente
        if tipo_ambiente in 'bB':
            iluminancia_recomendada = 200
        elif tipo_ambiente in 'cC' or tipo_ambiente in 'reuREU' or tipo_ambiente in 'tT':
            iluminancia_recomendada = 500
        elif tipo_ambiente in 'recREC':
            iluminancia_recomendada = 300
        return iluminancia_recomendada

    def calcula_area_ambiente(self):
        comprimento = float(self.comprimento)
        largura = float(self.largura)
        return (comprimento * largura)

    def calcula_indice_local_exato(self):
        comprimento = float(self.comprimento)
        largura = float(self.largura)
        distancia_mesa_luminaria = float(self.distancia_mesa_luminaria)
        indice_exato = (comprimento * largura / ((comprimento + largura) * distancia_mesa_luminaria))
        return indice_exato

    def calcula_indice_local_tabela(self):
        indice_exato = self.calcula_indice_local_exato()
        lista_indices_tabela = [0.6, 0.8, 1, 1.25, 1.5, 2, 2.5, 3, 4, 5]
        lista_indicetabela_indiceexato_diferenca = []

        for indice_tabela in lista_indices_tabela:
            indicetabela_indiceexato_diferenca = abs(indice_tabela - indice_exato)
            lista_indicetabela_indiceexato_diferenca.append(indicetabela_indiceexato_diferenca)
            menor_diferenca = min(lista_indicetabela_indiceexato_diferenca)
            posicao_menor_diferenca = lista_indicetabela_indiceexato_diferenca.index(menor_diferenca)

        return lista_indices_tabela[posicao_menor_diferenca]

    def descobre_refletancia(self):
        cor_teto = self.cor_teto
        cor_parede = self.cor_parede
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
        return indice_refletancia

    def descobre_fator_utilizacao(self):
        indice_tabela = self.calcula_indice_local_tabela()
        refletancia = self.descobre_refletancia()

        arquivo = open('fator_utilizacao_tcs029_32w.csv')
        arquivo_lido = list(csv.DictReader(arquivo))
        arquivo.close()

        for linha_fator_utilizacao in arquivo_lido:
            if float(linha_fator_utilizacao['K']) == indice_tabela:
                fator_utilizacao = linha_fator_utilizacao[str(refletancia)]
                return fator_utilizacao

    def calcula_total_lumens(self):
        iluminancia_recomendada = self.descobre_iluminancia_recomendada()
        area_ambiente = self.calcula_area_ambiente()
        fator_utilizacao_luminaria = float(self.descobre_fator_utilizacao())
        fator_depreciacao_luminaria = 0.85
        return (iluminancia_recomendada * area_ambiente) / (fator_utilizacao_luminaria * fator_depreciacao_luminaria)

    def calcula_qtd_luminarias(self):
        total_lumens = self.calcula_total_lumens()
        lumens_por_luminaria = self.lumen_luminaria
        return round(total_lumens / lumens_por_luminaria)


if __name__=='__main__':
    qtd_ambientes = int(input('Quantos ambientes deseja informar? '))

    for _ in range(qtd_ambientes):
        ambiente = Ambiente()
        
        ambiente.comprimento = float(input('Qual o comprimento do ambiente? '))
        ambiente.largura = float(input('Qual a largura do ambiente? '))
        ambiente.distancia_mesa_luminaria = float(input('Qual a distancia entre a área de trabalho (mesa ou bancada) e a luminária? '))
        ambiente.cor_teto = input('Qual a cor do teto no ambiente (B para branco, C para claro, E para escuro)? ')
        ambiente.cor_parede = input('Qual a cor da parede no ambiente (B para branca, C para clara, E para escura)? ')
        ambiente.tipo_ambiente = input('Qual o tipo de ambiente (B para banheiro, C para copa, REU para sala de reuniao, T para sala de trabalho, REC para recepcao)? ')
        ambiente.lumen_luminaria = int(input('Quantos lumens possui cada luminaria? '))

        print('~~~~')

        lista_qtd_lum = ambiente.calcula_qtd_luminarias()
        if ambiente.tipo_ambiente in 'bB':
            nome_ambiente = 'Banheiro:'
        elif ambiente.tipo_ambiente in 'cC':
            nome_ambiente = 'Copa:'
        elif ambiente.tipo_ambiente in 'reuREU':
            nome_ambiente = 'Sala de reunião:'
        elif ambiente.tipo_ambiente in 'tT':
            nome_ambiente = 'Sala de trabalho:'
        elif ambiente.tipo_ambiente in 'recREC':
            nome_ambiente = 'Recepção:'

        print(nome_ambiente, lista_qtd_lum, 'luminárias\n\n')

