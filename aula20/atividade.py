# Novo Projeto
# Apresentar uma análise mais detalhada sobre os casos de estelionato registrados no estado do Rio de Janeiro
# Identificar quais meses e anos (coluna: mês_ano) apresentam as menores e maiores quantidades de estelionatos, comparando esses períodos com o total geral de registros
# Apresentar como os casos estão distribuidos ao longo do tempo, verificando se existe algum padrão nas ocorrências, bem como identificar os períodos com menores e maiores índices
#além de expor meses/anos, que apresentem quantidades muito acima do comportamento dos demais períodos analisados.

# Ambiente virtual

# bibliotecas necessárias
import os 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# Limpeza do terminal
os.system('cls')

# Adquirindo os dados para análise
try:
    print('\nAdquirindo os dados... ')

    # definição da variavel para os dados da URL: https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv
    endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_seguranca_publica = pd.read_csv(endereco_dados, sep= ';', encoding= 'iso-8859-1')
    
    # Visualização dos dados obtidos
    #print(df_seguranca_publica)

except Exception as e:
    print(f'Erro ao adquirir os dados: {e}')

try:
    print('\nDelimitando os dados adquiridos... ')

    df_estelionato = df_seguranca_publica[['mes_ano', 'estelionato']]

    # Visualização dos dados delimitados
    #print(df_estelionato)

except Exception as e:
    print(f'Erro ao delimitar os dados: {e}')

try:
    print('\nAgrupando e totalizandos os dados... ')

    df_estelionato = df_estelionato.groupby('mes_ano', as_index=False)['estelionato'].sum()

    # Visualizando o agrupamento e total
    #print(df_estelionato)

except Exception as e:
    print(f'Erro ao agrupar e totalizar os dados: {e}')

try:
    print('\nOrganizando as informações... ')

    df_estelionato = df_estelionato.sort_values(by='estelionato', ascending=False)

    # Visualizando a organização
    #print(df_estelionato)

except Exception as e:
    print(f'Erro ao organizar as informações: {e}')

try:
    print('\nCalculando as quantidades de estelionato... ')

    # Utilizando o Numpy
    array_estelionato = np.array(df_estelionato['estelionato'])
    
    # Visualização do array
    #print(array_estelionato)

    # Verificando os meses que houveram mais, menos e o total de estelionatos
    total_estelionato = sum(array_estelionato)
    menor_mes_estelionato = min(array_estelionato)
    maior_mes_estelionato = max(array_estelionato)
    df_menor_mes_estelionato = df_estelionato[df_estelionato['estelionato'] == menor_mes_estelionato]
    df_maior_mes_estelionato = df_estelionato[df_estelionato['estelionato'] == maior_mes_estelionato]

    # Visualização dos calculos
    # print(total_estelionato)
    # print(menor_mes_estelionato)
    # print(maior_mes_estelionato)
    # print(df_menor_mes_estelionato) 
    # print(df_maior_mes_estelionato)    

except Exception as e:
    print(f'Erro ao calcular as métricas: {e}')

try:
    print('\nCalculando as Medidas de tendência Central... ')

    media_estelionato = np.mean(array_estelionato)
    mediana_estelionato = np.median(array_estelionato)
    distancia_media_mediana = abs((media_estelionato - mediana_estelionato) / mediana_estelionato * 100)

    # Visualização dos calculos
    # print(media_estelionato)
    # print(mediana_estelionato)
    # print(distancia_media_mediana)

except Exception as e:
    print(f'Erro ao calcular as medidas: {e}')

try:
    print('\nCalculando as distribuições... ')

    quartil_inferior = np.quantile(array_estelionato, 0.25)
    quartil_superior = np.quantile(array_estelionato, 0.75)
    IQR = quartil_superior - quartil_inferior
    limite_inferior = quartil_inferior - (1.5 * IQR)
    limite_superior = quartil_superior + (1.5 * IQR) 
    amplitude = quartil_superior - quartil_inferior
    
except Exception as e:
    print(f'Erro ao calcular a distribuição: {e}')

try:
    print('\nEncontrando os períodos com Maiores e Menores índices de estelionato...')

    df_menor_qtd_estelionato = df_estelionato[df_estelionato['estelionato'] < quartil_inferior]
    df_maior_qtd_estelionato = df_estelionato[df_estelionato['estelionato'] > quartil_superior]
    df_extremo_inferior = df_estelionato[df_estelionato['estelionato'] < limite_inferior]
    if len(df_extremo_inferior) == 0:
        print('Não existem valores extremos inferiores')

    else:
        print(df_extremo_inferior.sort_values(by= 'estelionato', ascending=True))
        
    df_extremo_superior = df_estelionato[df_estelionato['estelionato'] > limite_superior]
    
    # Visualizaçãod dos periodos
    # print(df_menor_qtd_estelionato)
    # print(df_maior_qtd_estelionato)
    # print(df_extremo_inferior)
    # print(df_extremo_superior)
    
except Exception as e:
    print(f'Erro ao encontrar as informações: {e}')

# Resumo das informações solicitadas
print(75*"=")
print('Relatório de Casos de Estelionato no Estado do Rio de Janeiro - 2003 a 2026(atual):')
print(75*"=")

print(f'Foram observados um total de {total_estelionato} casos durante o período analisado')
print(f'O Período com menor índice de estelionatos teve, {menor_mes_estelionato} casos e refere-se ao mês {df_menor_mes_estelionato['mes_ano'].values[0]}')
print(f'O Período com maior índice de estelionatos teve, {maior_mes_estelionato} casos e refere-se ao mês {df_maior_mes_estelionato['mes_ano'].values[0]}')
print(75*"=")
print(f'Não há um padrão nos dados analisados, a quantidade de casos tem variação acentuada em dirversos meses')
print(f'A Média de casos é de {media_estelionato:.2f},\nsendo que 50% dos períodos analisados correspondem a {mediana_estelionato:.2f} casos,\ndemonstrando que os números sofreram influência de períodos com quantidade de casos muito acima do considerao padrão')
print(75*"=")
print(f'Existe uma alta dispersão entre os valores, tendencia de não ter um padrão nos dados analisados')

print('\nMeses com valores anormais: ')
print(75 * '=')
print(df_extremo_superior.sort_values(by='estelionato', ascending=False))

try:
    print('\nVisualização dos dados...')
    plt.figure(figsize=(18,8))
    plt.subplots(2, 1)

    plt.subplot(2, 1, 1)
    plt.boxplot(array_estelionato, vert=False, showmeans=True) # aparecer a média
    
    plt.subplot(2, 1, 2)
    plt.text(0.1, 0.9, f'Média: {media_estelionato:.2f}')
    plt.text(0.1, 0.8, f'Mediana: {mediana_estelionato:.2f}')
    plt.text(0.1, 0.7, f'Distância: {distancia_media_mediana:.2f}')
    plt.text(0.1, 0.6, f'Amplitude: {amplitude:.2f}')
    plt.text(0.1, 0.5, f'Menor mês: {menor_mes_estelionato:.2f}')
    plt.text(0.1, 0.4, f'Maior mês: {maior_mes_estelionato:.2f}')

    plt.show()

except Exception as e:
    print(f'Erro ao visualizaro os dados: {e}')
    exit()