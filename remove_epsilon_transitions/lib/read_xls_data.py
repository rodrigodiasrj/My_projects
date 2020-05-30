#!/usr/bin/env python

from lib.convert_to_afn import *

def get_input_symbols(xls_table):
    input_symbols = {}
    for column in range(2,xls_table.max_column+1):
        if(xls_table.cell(row=1,column=column).value is not None):
            #print(xls_table.cell(row=1,column=column).value)
            input_symbols[column] = xls_table.cell(row=1,column=column).value
        else:pass
            #raise RuntimeError("Existem células vazias na primeira linha!")
    return input_symbols

def create_automata(xls_table):
    input_symbols = get_input_symbols(xls_table)
    automato = Automato()
    create_states(automato=automato,xls_table=xls_table)
    get_table_transitions(automato=automato,input_symbols=input_symbols,xls_table=xls_table)
    return automato

def create_transitions(input_symbol,origin,destiny,automato):
    if (automato.get_state_by_name(str(destiny))):
        origin.set_transition(symbol=input_symbol, destiny=automato.get_state_by_name(str(destiny)))
    else:
        raise Exception(
            f"ERROR: A transiçao: {origin.get_name()}:{input_symbol}:{destiny} Não faz parte do automato!")


def get_table_transitions(input_symbols,automato,xls_table):
    for line in range(2,xls_table.max_row+1):
        state = automato.get_state_by_name(str(xls_table.cell(row=line, column=1).value).strip('*'))
        if (state is None):
            raise Exception ("Existem transições para estados que não fazem parte do automato")
        for column in range(2,xls_table.max_column+1):
            state_name = xls_table.cell(row=line, column=column).value
            if (state_name is None): continue
            elif(not (str(state_name).find('{') and str(state_name).find('}'))):
                t = str(state_name).replace('{','').replace('}','')
                for state_name in t.split(","):
                    create_transitions(automato=automato,input_symbol=input_symbols[column],origin=state,destiny=state_name)
            else:
                create_transitions(automato=automato,input_symbol=input_symbols[column],origin=state,destiny=state_name)

def create_states(automato,xls_table):
    for line in range(2,xls_table.max_row+1):
        is_final = False
        state_name = xls_table.cell(row=line,column=1).value
        if(state_name is not None):
            if (str(state_name[0]) == '*'):
                is_final = True
            if(not automato.get_state_by_name(str(state_name))):
                automato.create_state(name=str(state_name).strip('*'),is_final=is_final)
            else:
                raise Exception("[ERROR]: Existem estados com o mesmo nome na primeria coluna!")



