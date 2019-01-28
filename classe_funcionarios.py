# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:09:10 2019

@author: Pedro Casella
"""

class Funcionarios:
    
    objetos = []
    
    def __init__(self,matricula,nome,area,cargo,salario_bruto,ano_de_admissao,mes_de_admissao,dia_de_admissao):
        self.matricula = matricula
        self.nome = nome
        self.area = area
        self.cargo = cargo
        self.salario_bruto = salario_bruto
        self.ano_de_admissao = ano_de_admissao
        self.mes_de_admissao = mes_de_admissao
        self.dia_de_admissao = dia_de_admissao
        
    def calcula_parametros(self,data_de_admissao):
        return 
    

    def calcula_bonus(self):
        bonus = (((salario_bruto*peso_tempo_adimissao)+(peso_salario_bruto*peso_area))/(salario_bruto*peso_faixa_salarial))*12
        return
    
    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.objects.append(self)
    