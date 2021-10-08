"""
- Listas
-Listas em phyton funcional como vetores/matrizes (arrays) em outras lignuagens,
com a diferença de serem dinamico e tambem de podermos colocat qualquer tipo de dado
-C/Java:
possuem tamanho e tipo de dado fixo
-Em Python
-Dinamico:
Não possui tamanho fixo, crio e adiciono elementos
não possui tipo de dado fixo, cabe qualquer tipo em uma lista
listas no python ficam no colchete []
"""
lista1 = [1, 22, 34, 14, 51, 76, 7, 81, 19, 10]
lista2 = ['j', 'o', 'a', 'o', 'v']
lista3 = []
lista4 = list(range(11))
lista5 = list('victor')
num = 7
if num in lista4:
    print(f'encontrei o numero {num} ')
else:
    print(f'nao encontrei o numero {num}')

letra = 'j'
if letra in lista5:
    print(f'Encontrei a letra {letra}')

lista1.sort()

print(lista5.count('o'))

lista1.append([10, 11, 12])
print(lista1)

if [10, 11, 12] in lista1:
    print('achei os numeros')
else:
    print('não achei')

lista1.extend([100, 101, 102]) #posso usar pra juntar duas listas
print(lista1)

lista2.insert(5, 'i')
print(lista2)

lista1 = lista1 + lista5
print(lista1)
print(len(lista1))

curso = 'curso de python'
curso = curso.split()
print(curso)

curso1 = 'curso,de,python'
curso1 = curso1.split(',')
print(curso1)

curso2 = 'curso', 'de', 'python'
espaço = ' '.join(curso2)
print(curso2)

print(lista1)
lista1.pop(2)
print(lista1)















