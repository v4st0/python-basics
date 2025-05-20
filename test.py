"""PRIMEIRO EXERCICIO: entrada = input('Digite um numero:') 

if entrada.isdigit(): 
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O numero {entrada_int} e {par_impar_texto}')
else:
    print('Voce nao digitou um numero inteiro') """


"""SEGUNDO EXERCICIO: entrada = input('Digite a hora em numeros inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Nao conheco essa hora')
except:
    print('Por favor, digite apenas numeros inteiros!') """


"""TERCEIRO EXERCICIO: nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome e curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome e normal')
    else:
        print('Seu nome e muito grande')
else:
    print('Digite mais de uma letra.') """

""" TESTE DE LOOP COM WHILE

condicao = True 

while condicao:
    nome = input('Qual o seu nome:')
    print(f'Seu nome e {nome}')
    
while condicao:
    print(1)
    print(2)
    print(3) """

""" WHILE DENTRO DE WHILE: 


qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou') """

"""
INTERANDO STRINGS COM WHILE:


nome = 'Pedro Lucas'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1 

novo_nome += '*'
print(novo_nome)
"""

"""CALCULADORA COM WHILE:

while True:
    print("\n== Calculadora Simples ===")
    print("Operacoes disponiveis: + - * /")

    operacao = input("Escolha a operacao: ")

    if operacao not in ["+", "-", "*", "/"]:
        print("Operacao invalida. Tente novamente.")
        continue

    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
    except ValueError:
        print("Voce digitou algo que nao e um numero. Tente de novo.")
        continue

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 == 0:
            print("Erro: divisao por zero nao e permitida.")
            continue
        resultado = num1 / num2

    print(f"Resultado: {resultado}")

    continuar = input("Dejesa fazer outra operacao? (s/n): ")
    if continuar.lower() != 's':
        print("Encerrando a calculadora. Ate mais!")
        break 
"""

""" WHILE/ELSE

string = 'valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break
    
    print(letra)
    i += 1 
else:
    print('Nao encontrei um espaco na string.')
print('Fora do while.')

"""

"""
frase = 'O Python e uma linguagem de programacao ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
"""


"""INTRODUCAO AO FOR/IN:

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)
"""


"""FOR + RANGE:

numeros = range(10)

for numero in numeros:
    print(numero)
"""


"""FOR POR BAIXO DOS PANOS:

texto = 'Pedro' #iteravel
iteratador = iter(texto) # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break
"""



"""O QUE DA PRA USAR NO WHILE TAMBEM DA NO FOR:

for i in range(10):
    if i ==2:
        print('i e 2, pulando...') 
        continue

    if i == 8:
        print('i e 8, seu else nao executara')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
"""


"""EXERCICIO JOGO DA PALAVRA SECRETA:

palavra_secreta = 'python'
letras_descobertas = ['*'] * len(palavra_secreta)
tentativas = 0

while '*' in letras_descobertas:
    print('Palavra:', ''.join(letras_descobertas))
    letra = input('Digite uma letra: ').lower()
    tentativas += 1
    letra_encontrada = False

    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            letras_descobertas[i] = letra
            letra_encontrada = True

    if letra_encontrada:
        print('Letra correta!')
    else:
        print('Letra incorreta.')

print(f'\nParabens! Voce descobriu a palavra "{palavra_secreta}" em {tentativas} tentativas.')
"""

"""TIPO LIST:
Listas em Python
Tipo list - mutavel
suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis: append, insert, pop, del, clear, extend, +

string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#       0    1        2               3    4
#      -5   -4       -3              -2   -1
lista = [1123, True, 'adadsadad', 1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
"""




"""ALTERANDO UMA LIST COM INDICES

#EVITE AO MAXIMO REMOVER ITENS DA LISTA POIS REQUER MUITO PROCESSAMENTO!!!

lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])
lista.append(50)
lista.pop() # remove o ultimo valor da lista antes do pop
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) # remove o valor do indice da lista selecionado no caso o "3"
print(lista, 'Removido', ultimo_valor)

"""



"""INSERINDO ITEMS NA LISTA

lista = [10, 20, 30, 40]
lista.append('Pedro')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lisa[4])
"""



"""CONCATENANDO E ESTENDENDO LISTAS EM PYTHON

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
"""



"""CUIDADOS QUE DEVEMOS TER COM DADOS MUTAVEIS (LIST/COPY)

lista_a = ['Pedro', 'Lucas', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
"""



"""FOR IN COM LISTAS

lista = ['Pedro', 'Lucas', 'ADADASD']

for nome in lista:
    print(nome, type(nome))
"""

"""EXERCICIO EXIBIR OS INDICES DA LISTA

lista = ['adda', 'sdwd', 'wdwf']
lista.append('trt')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
"""



"""INTRODUCAO AO DESEMPACOTAMENTO E TUPLES

_, _, nome, *resto = ['uwyuad', 'opiiu', 'kjh']
print(nome, resto)
"""



"""TYPE TUPLE

nomes = ['uwyuad', 'opiiu', 'kjh']
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)
"""

"""ENUMERATE PARA ENUMERAR VALORES ITERAVEIS

lista = ['uwyuad', 'opiiu', 'kjh']
lista.append('poiu')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')

"""


"""EXERCICIO DE LISTAS: CRIAR UMA LISTA DE COMPRAS"""

lista_compras = []

while True:
    print('\nO que deseja fazer?')
    print('1 - Inserir item')
    print('2 - Apagar item')
    print('3 - Listar itens')
    print('4 - Sair')

    opcao = input('Escolha uma opcao: ')

    if opcao == '1':
        item = input('Digite o nome do item: ')
        lista_compras.append(item)
        print(f'"{item}" foi adicionado a lista.')

    elif opcao == '2':
        if not lista_compras:
            print('A lista esta vazia.')
        else:
            for i, item in enumerate(lista_compras):
                print(f'{i} - {item}')
            try:
                indice = int(input('Digite o indice do item que deseja apagar: '))
                item_removido = lista_compras.pop(indice)
                print(f'"{item_removido}" foi removido da lista.')
            except (ValueError, IndexError):\
            print('Indice invalido.')
                
    elif opcao == '3':
        if not lista_compras:
            print('A lista esta vazia.')
        else:
            print('\nLista de compras:')
            for i, item in enumerate(lista_compras):
                print(f'{i} - {item}')

    elif opcao == '4':
        print('Encerrando o programa. ate mais!')
        break

    else:
        print('Opcao invalida. Escolha 1, 2, 3 ou 4.')
