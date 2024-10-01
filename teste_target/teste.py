import os
import time

## UTILITIES ##
# Clear Screen
def cls():
    os.system("cls");
# Kbhit
def kbhit():
    input("\nPressione qualquer tecla para continuar...");
# wait
def wait(sec):
    time.sleep(sec);
# ---------- #


## QUESTÃO 1 ##
def questao1():
    SOMA = 1; # numero subsequente a ser somado ao anterior
    SEQ = 0; # numero resultante da soma
    BASE = 0; # numero anterior

    NUMBER = int(input(f"Escolha uma numero e verificaremos se ele se encaixa na sequencia de Fibonacci: "));

    print(f"Numero escolhido: ", NUMBER);
    wait(0.8);
    while SEQ < NUMBER:
        SEQ = BASE + SOMA;
        print(BASE, " + ", SOMA, " = ", SEQ);
        wait(0.5);
        BASE = SOMA;
        SOMA = SEQ;
    
    if NUMBER == SEQ:
        print(f"\nO numero escolhido, ", NUMBER, ", pertence a sequência de Fibonacci.");
    else:
        print(f"\nO numero escolhido, ", NUMBER, ", não pertence a sequência de Fibonacci.");
    kbhit();
    cls();


## QUESTÃO 2 ##
def questao2():
    print("\nDigite uma palavra ou uma frase para verificarmos quanto caracteres 'A' existem na string");
    wait(0.3);
    DADOS = str(input(">> ")).lower();
    print(f"\nAnalisando a frase:", DADOS);
    wait(0.8);
    if 'a' in DADOS:
        REVIEW = DADOS;
        x = REVIEW.count('a');
        print(f"\nA letra 'a' foi encontrada no arquivo, ", x,"x");
    else:
        print(f"A letra 'a' não foi encontrada no arquivo...");
    kbhit();
    wait(0.3);
    cls();

## QUESTÃO 3 ##
def questao3():
    SOMA = 0;
    INDICE = 12;
    K = 1;
    spc = 1;

    while K < INDICE:
        K = K + 1;
        SOMA = SOMA + K;
        print(f" "*spc, SOMA);
        spc += 1;
        wait(0.3);
    
    print("\nFinal do processamento: ", SOMA);
    kbhit();
    cls();

## CODE FLOW ##
# Limpando terminal para
#inicio limpo do programa
cls();

# Questão 1
print("Questão 1 - Sequencia de Fibonacci");
kbhit();
cls();
questao1();

# Questão 2
print("Questão 2 - String 'A'");
questao2();

# Questão 3
print("Questão 3 - 'For/While'");
questao3();

## QUEBRA DO APLICATIVO ##
print("Código por Alvaro G. Ribeiro Netto");
input("\nPressione qualquer tecla para encerrar o programa...");