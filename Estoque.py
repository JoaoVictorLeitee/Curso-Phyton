estoque = []
produto = []
quantidade = ''
verificar = ''
venda = ''
RetiradaVendaQtd = ''
RetiradaVendaNome = ''
remover = ''

while produto != 'sair':
    print("Adicione o nome do  produto")
    produto = input()
    if produto != 'sair':
        print('adicione a quantidade do produto em estoque por favor')
        quantidade = input()
    if produto != 'sair':
        estoque.append(produto)

print("quer verificar o estoque?")
verificar = input()
if verificar == 'sim':
    for produto in estoque:
        print('--------------------------------------------------')
        print(produto, quantidade)
"""
print('houve venda ?')
venda = input()
if venda == 'sim':
    print(produto, quantidade)
    print("qual produto da lista acima?")
RetiradaVendaNome = input()
for RetiradaVendaNome in produto:
    produto.pop(RetiradaVendaNome)
"""






