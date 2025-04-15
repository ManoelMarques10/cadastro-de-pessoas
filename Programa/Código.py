# Programa básico de cadastro de pessoas.

# Variáveis e listas.
parar = 'x'
lista = []
count = 0
soma = 0
acimadameia = []
mulheres = []

# Correção de ValueError
try:
    # Loop
    while parar != 's':
        count += 1
        dados = {'nome': 'x', 'sexo': 'x', 'idade': 'x'}
        dados['nome'] = nome = input('\33[33mNome: ')
        dados['sexo'] = sexo = input('\33[33mSexo [F] ou [M]: ').upper()
        while dados['sexo'] not in ['F', 'M']:
            print('\33[31mApenas é aceito F (Feminino) ou M (Masculino).')
            dados['sexo'] = sexo = input('\33[33mSexo [F] ou [M]: ').upper()
        while True:
            try:
                dados['idade'] = idade = int(input('Idade: '))
                break
            except ValueError:
                print('\33[31mDigite apenas números inteiros para a idade.')
        lista.append(dados.copy())
        soma += dados['idade']
        parar = input('\33[36mParar [S] ou [N] ').lower()

    # Média de idade
    media = soma / count

    # Adicionar pessoa acima da média na lista
    for pessoa in lista:
        if pessoa['idade'] > media:
            acimadameia.append(pessoa)

    # Adicionar mulheres na lista
    for pessoa2 in lista:
        if pessoa2['sexo'] == 'F':
            mulheres.append(pessoa2)
except ValueError:
    print('\33[31mAlgo deu errado, tente novamente.')
    exit()

# Resultado:
if count == 1:
    print(f'\33[35mFoi cadastrada {count} pessoa.')
else:
    print(f'\33[35mForam cadastradas {count} pessoas.')

print(f'\33[32mA média de idade das pessoas é: {media:.1f}.')
print('\33[34mAs pessoas com idade acima da média são:')
for pessoa in acimadameia:
    print(f"\33[36mNome: {pessoa['nome']}, Idade: {pessoa['idade']}, Sexo: {pessoa['sexo']}")

print('\33[37mA lista de mulheres cadastradas é:')
for mulher in mulheres:
    print(f"\33[37mNome: {mulher['nome']}, Idade: {mulher['idade']}")


