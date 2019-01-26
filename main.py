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
    bonus = (((salario_bruto * peso_tempo_adimissao) + (peso_salario_bruto * peso_area))/(salario_bruto * peso_faixa_salarial))*12


Retorno:
    
    
"""

#Variaveis
salario_minimo =  1006


class Funcionario:
    
    def __init__(self,matricula,nome,area,cargo,salario_bruto,data_de_admissao):
        self.matricula = matricula
        self.nome = nome
        self.area = area
        self.cargo = cargo
        self.salario_bruto = salario_bruto
        self.data_de_admissao = data_de_admissao
        
    def calcula_parametros(self,data_de_admissao):
        
        return 
    
    
    
    def calcula_bonus(self):
        bonus = (((salario_bruto*peso_tempo_adimissao)+(peso_salario_bruto*peso_area))/(salario_bruto*peso_faixa_salarial))*12
        return bonus_pessoa
        
        
if __name__== "__main__":
