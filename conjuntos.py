"""
Conjuntos
em qualquer linguagem de programação, refêrencia a teoria dos conjuntos matemáticos
no python os conjuntos são chamados de sets
ele ignora as repetições
{}
"""
#menos usual
s = set({1, 3, 3, 4, 5, 6, 7, 7, 6})
print(s)
print(type(s))

s1 = {1, 2, 3, 4, 5, 5}
print(s1)
print(type(s1))

if 2 in s1:
    print('tem o número 2')
else:
    print('não tem o número 2')


lista = [1, 2, 3, 5, 5, 6, 6, 7, 8, 9]
print(f'Lista:{lista} com {len(lista)} elementos')

tupla = 1, 2, 3, 5, 5, 6, 6, 7, 8, 9
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys({1, 2, 3, 5, 5, 6, 6, 7, 8, 9}, 'teste')
print(f'dicionario{dicionario} com {len(dicionario)} elementos')

conjunto = {1, 2, 3, 5, 5, 6, 6, 7, 8, 9}
print(f'conjunto: {conjunto} com {len(conjunto)} elementos ')

conjunto.add(10)
print(conjunto)
conjunto.remove(10) #or discard, não gera erro
print(conjunto)

novo = conjunto.copy()
novo.add(20)
print(novo)

estudantes_python = {'mateus', 'joão', 'dayane', 'dagan', 'batista'}
estudantes_java = {'cirleide', 'dede', 'joão', 'dagan'}
unicos = estudantes_java.union(estudantes_python)
print(unicos)
#ou
unicos1 = estudantes_java | estudantes_python
print(unicos1)

ambos = estudantes_java.intersection(estudantes_python) #ou &
print(ambos)

pergunta = input('pesquise um nome')
if pergunta in estudantes_java:
    print(f'o {pergunta} está matriculado')
else:
    print('não esta matriculado')
