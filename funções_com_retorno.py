#teste1
def quadrado_de_7():
    return 7 * 7
print(f'Retorno {quadrado_de_7() + 1}')



#moeda
from random import random
def joga_moeda():
    if random() > 0.5:
        return 'cara'
    return 'coroa'
print(joga_moeda())


#ímpar_par
def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False
print(eh_impar())


#teste2
def erro():
    return 'Favor Preencher o campo obrigatório'

resposta = input("preencha o campo: ")

if resposta == '':
    print(erro())

if resposta == 'teste':
    print('Campo preenchido')


