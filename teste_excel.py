# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 18:42:24 2019

@author: Pedro Casella
"""
from xlrd import open_workbook

wb = open_workbook('banco_dados_funcionarios.xlsx')
sheet = wb.sheet_by_index(0)
    
for row in range(1,sheet.nrows):
    for columns in range(0,sheet.ncols):
        print(sheet.cell_value(row,columns))
        print(sheet.row_values(1))