#!/usr/bin/env python
import logging,os
from datetime import datetime
dirpath = os.getcwd()

def write_result(automato,book):
    sheet = book.create_sheet('RESULT')
    write_states(automato,sheet)
    write_symbols(automato,sheet)
    write_transitions(automato,sheet)


########## Função responsável por escrever os estados na primeira coluna da planilha #########
def write_states(automato,sheet):
    aux_row = 2
    aux_column = 1
    for state in automato.get_states_list():
        state_name = state.get_name()
        if(state.is_final):
            state_name = f'*{state_name}'
        sheet.cell(column=aux_column, row=aux_row, value="{0}".format(str(state_name)))
        aux_row+=1

######## Função responsável por escrever os síbolos de entrada na primeira linha da planilha ########
def write_symbols(automato,sheet):
    aux_column = 2
    aux_row = 1
    for symbol in automato.get_input_symbols():
        sheet.cell(column=aux_column, row=aux_row, value="{0}".format(str(symbol)))
        aux_column +=1

def write_transitions(automato,sheet):
    start_row = 2
    start_column = 2
    for row in range(start_row,len(automato.get_states_list())+start_row):
        if sheet.cell(row=row,column=1).value is not None:
            cur_state = sheet.cell(row=row,column=1).value.strip('*')
            for column in range(start_column,len(automato.get_input_symbols())+start_column):
                symbol = sheet.cell(row=1,column=column).value
                aux = ' '
                if(cur_state is not None and symbol is not None):
                    state = automato.get_state_by_name(cur_state).get_transitions_list_by_symbol(symbol)
                    if(not state):continue
                    else:
                        for value in state:
                            #print(f"Escrevendo transição: {value.get_origin().get_name()} simbolo: {value.get_symbol()} destino: {value.get_destiny().get_name()}")
                            aux += ',' + value.get_destiny().get_name()
                            sheet.cell(column=column, row=row, value="{0}".format(str(aux[2:])))
