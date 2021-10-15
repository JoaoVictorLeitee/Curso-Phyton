"""
mapas mais conhecidos como dicionários em python
"""
receita = {'jan':100, 'fev':250, 'mar':400}
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'o valor do mês {chave}: R$:{receita[chave]}')

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

print(receita.values())
print(receita.keys())

for valor in receita.values():
    print(valor)

for chave, valor in receita.items():
    print(f'chave:{chave} valor: {valor}')

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))