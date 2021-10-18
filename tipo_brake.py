"""
Saindo de loops com Break
"""

for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)
print('sai do loop')

while True:
    comando = input('digite "sair" para finalizar o loop')
    if comando == 'sair':
        break
    print('loop finalizado')