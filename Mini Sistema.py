menu='MENU DE INTERAÇÃO'
print('=-'*30)
print(menu.center(55))
print('=-'*30)

print('[1] Cadastro de Produtos')
print('[2] Cadastro de Usuário')
print('[3] Cadastro de Mercados')
print('[4] Comparar preços de produtos')
print('[5] Comparar preços por cesta básica')
print('=-'*30)

RespostaUsuario=int(input('Resposta: '))
print('=-'*30)
if RespostaUsuario == 1:
    print("Opção 1 escolhida. Cadastre os produtos")
    produtos=[]
    preços=[]
    while True:
        produtos.append(input("Nome do produto: "))
        preços.append(float(input("Preço do produto: ")))
        resposta=input("Deseja continuar? [S/N]: ").upper()
        print('=-' * 30)
        if resposta == 'N':
            break
    print('Produtos Cadastrados')
    for c in range(len(produtos)):
        print(f'{produtos[c].upper()} : R${preços[c]}')
elif RespostaUsuario == 2:
    print('Opção 2 escolhida. Cadastre o Usuário')
    usuarios=[]
    while True:
        usuarios.append(input('Nome do usuário: '))
        resposta = input("Deseja continuar? [S/N]: ").upper()
        print('=-' * 30)
        if resposta == 'N':
            break
    print("Usuários Cadastrados")
    for c in usuarios:
        print(c)
elif RespostaUsuario == 3:
    print("Opção 3 escolhida. Cadastre o Mercado")
    mercado=[]
    while True:
        mercado.append(input("Nome do Mercado: "))
        resposta = input("Deseja continuar? [S/N]: ").upper()
        print('=-' * 30)
        if resposta == 'N':
            break
    print("Mercados Cadastrados")
    for c in mercado:
        print(c)
elif RespostaUsuario == 4:
    print('Opção 4 escolhida. Compare os preços')
    m1=input("Nome do mercado: ")
    p1=float(input(f"Preço do produto no {m1}: "))
    print('=-' * 30)
    m2=input("Nome do 2 mercado: ")
    p2=float(input(f"Preço do produto no {m2}: "))
    print('=-' * 30)
    if p1 < p2:
        print(f"O produto é mais barato no {m1}")
    else:
        print(f"O produto é mais barato no {m2}")
elif RespostaUsuario == 5:
    print('Opção 5 escolhida. Compare os preços')
    m1=input("Nome do mercado: ")
    p1=float(input(f"Preço da cesta básica no {m1}: "))
    print('=-' * 30)
    m2=input("Nome do 2 mercado: ")
    p2=float(input(f"Preço da cesta básica no {m2}: "))
    print('=-' * 30)
    if p1 < p2:
        print(f"A cesta mais barata é no {m1}")
    else:
        print(f"A cesta mais barata é no {m2}")
else:
    print("Opção Inválida")