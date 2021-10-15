"""
Dicionários
em outras linguagens são os mapas.
Sempre em {}
"""

paises = {'br': 'brasil', 'eua': 'Estados unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))
#forma menos comum
paises2 = dict(br='brasil', eua='Estados unidos', py='Paraguai')
print(paises2)
print(type(paises2))

#menos usado
print(paises2['br'])

#mais usado
print(paises2.get('br'))

if 'br' in paises:
    brasil = paises['br']

localidades = {
    (35.578, 35.4585): 'escritorio do Brasil'
}
print(type(localidades))

#adicionar elementos em dict

receita = {'jan':100, 'fev':250}
print(receita)
receita['mar'] = 650
print(receita)

novo_dado = {'abr':500}
receita.update(novo_dado) #receita.update({'abr':500})
print(receita)

#atualizando dados do dict

receita.update({'abr':550})
print(receita)
receita['abr'] = 600
print(receita)

outro = {}.fromkeys('a', 'b')
usuario = {}.fromkeys(['nome', 'pontos', 'email'], 'desconhecido')
print(usuario)
print(type(usuario))
print(outro)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
