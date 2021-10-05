"""
Recebendo dados do usuário
"""

# Entrada
nome = input("Qual é o seu nome? ")
print(f'Seja Bem Vindo(a) {nome}')
idade = int(input("Qual é a sua idade? "))


# Processamento


# Saída
if idade >= 18:
    print(f'Nossa você tem {idade} anos? como você e velho(a)!')
else:
    print(f'Nossa você tem {idade} anos? como você e novinho(a)!')

