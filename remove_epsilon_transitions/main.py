from lib.read_xls_data import *
from lib.write_xls_data import *
import os,openpyxl,logging,time,sys
from datetime import datetime
dirpath = os.getcwd()
logging.basicConfig(filename=f'{dirpath}\\log\\process.log',level=logging.DEBUG)



#try:
print(
    '  /$$$$$$  /$$$$$$$$ /$$   /$$         /$$$$$$$$         /$$                      /$$$$$$  /$$$$$$$$ /$$   /$$')
print(
    ' /$$__  $$| $$_____/| $$$ | $$        | $$_____/        | $$                     /$$__  $$| $$_____/| $$$ | $$')
print(
    '| $$  \ $$| $$      | $$$$| $$        | $$             /$$$$$$    /$$$$$$       | $$  \ $$| $$      | $$$$| $$')
print(
    '| $$$$$$$$| $$$$$   | $$ $$ $$ /$$$$$$| $$$$$         |_  $$_/   /$$__  $$      | $$$$$$$$| $$$$$   | $$ $$ $$')
print(
    '| $$__  $$| $$__/   | $$  $$$$|______/| $$__/           | $$    | $$  \ $$      | $$__  $$| $$__/   | $$  $$$$')
print(
    '| $$  | $$| $$      | $$\  $$$        | $$              | $$ /$$| $$  | $$      | $$  | $$| $$      | $$\  $$$')
print(
    '| $$  | $$| $$      | $$ \  $$        | $$$$$$$$        |  $$$$/|  $$$$$$/      | $$  | $$| $$      | $$ \  $$')
print(
    '|__/  |__/|__/      |__/  \__/        |________/         \___/   \______/       |__/  |__/|__/      |__/  \__/')
print(
    '                                                                                                              ')
print(
    '                                                                                                              ')
print(
    '                                                                                                              ')
print(
    '                    /$$$$$$                                                      /$$                          ')
print(
    '                   /$$__  $$                                                    | $$                          ')
print(
    '                  | $$  \__/  /$$$$$$  /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$   ')
print(
    '                  | $$       /$$__  $$| $$__  $$|  $$  /$$//$$__  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$  ')
print(
    '                  | $$      | $$  \ $$| $$  \ $$ \  $$/$$/| $$$$$$$$| $$  \__/  | $$    | $$$$$$$$| $$  \__/  ')
print(
    '                  | $$    $$| $$  | $$| $$  | $$  \  $$$/ | $$_____/| $$        | $$ /$$| $$_____/| $$        ')
print(
    '                  |  $$$$$$/|  $$$$$$/| $$  | $$   \  $/  |  $$$$$$$| $$        |  $$$$/|  $$$$$$$| $$        ')
print(
    '                   \______/  \______/ |__/  |__/    \_/    \_______/|__/         \___/   \_______/|__/        ')
print(
    '                                                                                                              ')
print(
    '                                                                                                              ')
print(
    '                                                                                                              ')
print('\n\nCarregando a planilha')
for i in range(3):time.sleep(1);print('.')
xls_file = f'{dirpath}\\file\\input_file.xlsx'
book = openpyxl.load_workbook(xls_file)
sheet = book['IN']
print('Lendo informações da planilha')
for i in range(3): time.sleep(1);print('.')
automato = create_automata(sheet)
print('Convertendo o automato')
for i in range(3): time.sleep(1);print('.')
afn = remove_epsilon_transition(automato=automato)
print('Escrevendo o resultado')
for i in range(3): time.sleep(1);print('.')
write_result(afn,book= book)
book.save(xls_file)
book.close()
print('Conversão realizada com sucesso!\nVeja o resultado na planilha "input_table.xlsx"')
time.sleep(30)
'''
except Exception as e:
    print(f"Erro: Não foi possível executar a operação!(check os arquivos de log para mais detalhes)")
    logging.error(f'{str(datetime.now())}: {str(e)}')
    time.sleep(30)
    exit(1)
'''