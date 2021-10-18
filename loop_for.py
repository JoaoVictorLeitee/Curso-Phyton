"""
Loop for

loop -> estrutura de repetição
for(para) -> uma dessas estruturas

C ou Java
for(int i = 0; i < 10;  i++){
    //execução loop
}
Python

for item in interavel:
    //execução loop

loops sao usados para iterar sequências ou valores interáveis.

Ex iteráveis:
Strinf
    nome = joao
Lista
    lista = [1.3.5.4]
Range
    numeros = range(1,10)
"""
#nome = 'joao'
#lista = [1,3,5,7,9]
#numeros = range(1,10)

#for letra in nome:
    #print(letra)
#print('   ')
#for numeros in lista:
    #print(numeros)
#print('   ')
#for numero in range(1,10):
    #print(numero)

qtd = int(input('Insira a quantidade do loop'))


for n in range(1,qtd+1):
    print(n * '\U0001F60D')


