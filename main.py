# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:30:03 2019

@author: Pedro Casella
"""

"""
Descrição:
Uma empresa fechou o ano de operação com lucro e deseja reparti-lo entre seus 
funcionários, com o objetivo de ser justa criou uma regra para a distribuição 
deste montante por: área, tempo de empresa, e faixa salarial (os funcionários 
que ganham menos teriam sua participação incrementada). Para isso foi 
solicitado ao time de tecnologia que desenvolva uma API REST que 
receba um valor máximo para distribuir e distribua o montante para 
os funcionários já cadastrados com os dados abaixo. 
Tal distribuição segue determinadas regras descritas a seguir .

Foi estabelecido um peso por área de atuação:
Peso 1: Diretoria; 
Peso 2: Contabilidade, Financeiro, Tecnologia; 
Peso 3: Serviços Gerais; 
Peso 5: Relacionamento com o Cliente;

Foi estabelecido um peso por faixa salarial e uma exceção para estagiários:
Peso 5: Acima de 8 salários mínimos; 
Peso 3: Acima de 5 salários mínimos e menor que 8 salários mínimos; 
Peso 2: Acima de 3 salários mínimos e menor que 5 salários mínimos; 
Peso 1: Todos os estagiários e funcionários que ganham até 3 salários mínimos;

Foi estabelecido um peso por tempo de admissão:
Peso 1: Até 1 ano de casa; 
Peso 2: Mais de 1 ano e menos de 3 anos; 
Peso 3: Acima de 3 anos e menos de 8 anos; 
Peso 5: Mais de 8 anos


Equação:
    bonus = (((salario_bruto * peso_tempo_adimissao) + (peseo_faixa_salarial * peso_area))/(salario_bruto * peso_faixa_salarial))*12
Retorno:
    
"""

#bibliotecas importadas
import datetime
from classe_funcionarios import Funcionarios 
from xlrd import open_workbook

#variaveis
lista_bonus = []

if __name__== "__main__":
    
    #---------------leitura do banco de dados excel----------------------------
    
    wb = open_workbook('banco_dados_funcionarios.xlsx')
    sheet = wb.sheet_by_index(0)
        
    for row in range(1,sheet.nrows):
        for columns in range(0,sheet.ncols):
            print(sheet.cell_value(row,columns))
    print(sheet.row_values(1))
    
    
    for i in range(1,sheet.nrows): 
        
    #------------instanciando meus objetos = funcionarios----------------------
    
        funcionario = Funcionarios(sheet.row_values(i)[0],sheet.row_values(i)[1],
                                 sheet.row_values(i)[2],sheet.row_values(i)[3],
                                 sheet.row_values(i)[4],sheet.row_values(i)[5],
                                 sheet.row_values(i)[6],sheet.row_values(i)[7])
    
    #----------------------levantamento dos pesos da equação-------------------

        #pesos por area
        tabela_pesos_area = {"Diretoria":1,
                        "Contabilidade":2,
                        "Financeiro":2,
                        "Tecnologia":2,
                        "Serviços Gerais":3,
                        "Relacionamento com o Cliente":5}
        
        #pesos por salario
        salario_minimo = 1006
        
        if funcionario.salario_bruto > 8*salario_minimo:
            peso_faixa_salarial = 5
        elif funcionario.salario_bruto < 8*salario_minimo and funcionario.salario_bruto > 5*salario_minimo:
            peso_faixa_salarial = 3
        elif funcionario.salario_bruto < 5*salario_minimo and funcionario.salario_bruto > 3*salario_minimo:
            peso_faixa_salarial = 2
        else:
            peso_faixa_salarial = 1
        
        #pesos por tempo
        
        ano_atual = datetime.date.today().year
        anos_de_casa = ano_atual - funcionario.ano_de_admissao
        
        if anos_de_casa > 8:
            peso_tempo_adimissao = 5
        elif anos_de_casa > 3 and anos_de_casa < 8:
            peso_tempo_adimissao = 3
        elif anos_de_casa > 1 and anos_de_casa < 3:
            peso_tempo_adimissao = 2
        elif anos_de_casa <= 1:
            peso_tempo_adimissao = 1
    
    
        #-----------------------------equação do bonus-----------------------------
        
        bonus = (((funcionario.salario_bruto*peso_tempo_adimissao)+
                (funcionario.salario_bruto*tabela_pesos_area[funcionario.area]))
                /(funcionario.salario_bruto*peso_faixa_salarial))*12
        
        print(bonus)
        lista_bonus.append(bonus)

        #---------------Adicionando no banco de dados excel--------------------
        
        
    
    
    
    
    
