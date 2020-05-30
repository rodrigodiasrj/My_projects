  /$$$$$$  /$$$$$$$$ /$$   /$$         /$$$$$$$$         /$$                      /$$$$$$  /$$$$$$$$ /$$   /$$
 /$$__  $$| $$_____/| $$$ | $$        | $$_____/        | $$                     /$$__  $$| $$_____/| $$$ | $$      
| $$  \ $$| $$      | $$$$| $$        | $$             /$$$$$$    /$$$$$$       | $$  \ $$| $$      | $$$$| $$      
| $$$$$$$$| $$$$$   | $$ $$ $$ /$$$$$$| $$$$$         |_  $$_/   /$$__  $$      | $$$$$$$$| $$$$$   | $$ $$ $$      
| $$__  $$| $$__/   | $$  $$$$|______/| $$__/           | $$    | $$  \ $$      | $$__  $$| $$__/   | $$  $$$$      
| $$  | $$| $$      | $$\  $$$        | $$              | $$ /$$| $$  | $$      | $$  | $$| $$      | $$\  $$$      
| $$  | $$| $$      | $$ \  $$        | $$$$$$$$        |  $$$$/|  $$$$$$/      | $$  | $$| $$      | $$ \  $$      
|__/  |__/|__/      |__/  \__/        |________/         \___/   \______/       |__/  |__/|__/      |__/  \__/      
                                                                                                                    
                                                                                                                    
                                                                                                                    
                    /$$$$$$                                                      /$$                                
                   /$$__  $$                                                    | $$                                
                  | $$  \__/  /$$$$$$  /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$         
                  | $$       /$$__  $$| $$__  $$|  $$  /$$//$$__  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$        
                  | $$      | $$  \ $$| $$  \ $$ \  $$/$$/| $$$$$$$$| $$  \__/  | $$    | $$$$$$$$| $$  \__/        
                  | $$    $$| $$  | $$| $$  | $$  \  $$$/ | $$_____/| $$        | $$ /$$| $$_____/| $$              
                  |  $$$$$$/|  $$$$$$/| $$  | $$   \  $/  |  $$$$$$$| $$        |  $$$$/|  $$$$$$$| $$              
                   \______/  \______/ |__/  |__/    \_/    \_______/|__/         \___/   \_______/|__/              
                                                                                                                    
                                                                                                                    
                                                                                                                    





**********************************************************************************************************************************

O programa trabalha com a tabela de transições de automatos finitos não determinísticos com transições vazias visando a remoção 
transições vazias do autômato em questão



***************
*** ENTRADA ***
***************

A entrada é das informações é realizada através da planilha xlsx da pasta input files

___________Prenchimento____________
A planilha deve ser preenchida de modo que: 

***Coluna A****
- Será utilizada para descrever os estados que o automato possui

***Linha 1****
- Utilizada para o preenchimento dos símbolos de entrada

***Linha x Coluna****
- A interseção entre o estado(da linha que está sendo lida), e o símbolo de entrada(refente a coluna) deve ser utilizado para
descrever as transições do automato


***Entrada Vazia****
- Para representar as transições vazias deve ser utilizado o símbolo '{}'

OBS: 
    1- Quando um estado não possuir transições para um determinado símbolo, a célula referente ao estado x símbolo deve ser
    não deve ser preenchida
    2 - A célula A1 não deve ser utilizada no preenchiment
    
    
***************
**** SAIDA ****
***************

- O resultado da conversão será impresso na planilha xlsx na aba RESULT 
- A cada execução do programa será gerada uma nova aba RESULT 










