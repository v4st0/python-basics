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


"""EXERCICIO DE LISTAS: CRIAR UMA LISTA DE COMPRAS

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
"""



"""IMPRECISAO DOS NUMEROS FLOAT + ROUND E DECIMAL.DECIMAL

import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))
"""



"""SPLIT, JOIN E STRIP METODOS UTEIS DA STR

frase = '   Olha so que   , MASSA VIADO          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
"""



"""LISTAS DENTRO DE LISTAS, ITERAVEIS DENTRO DE ITERAVEIS

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0        1        2
    ['Luiz', 'Joao', 'Eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala e {sala}')
    for aluno in sala:
        print(aluno)
"""



"""DETALHES SOBRE O INTERPRETADOR DO PYTHON

python mod.py (executa o mod)
python -u (unbuffered)
python -m mod (lib mod como script)
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)

The zen of Python, por Tim Peters

bonito e melhor que feio.
explicito e melhor que implicito.
simples e melhor que complexo.
complexo e melhor que complicado.
plano e melhor que aglomerado.
esparso e melhor que denso.
legibilidade conta.
casos especiais nao sao especiais o bastante para quebrar as regras.
embora a praticidade venca a pureza.
erros nunca devem passar silenciosamente.
a menos que sejam explicitamente silenciados.
diante da ambiguidade, recure a tentacao de adivinhar.
deve haver um -- e so um -- modo obvio para fazer algo.
embora esse modo possa nao ser obio a primeira vista menos que voce seja holandes.
agora e melhor que nunca.
embora nunca frequentemente seja melhor que *exatamente* agora.
se a implementacao e dificil de explicar, e uma ma ideia
se a implementacao e facil de explicar, pode ser uma boa ideia.
namespaces sao uma grande ideia -- vamos fazer mais dessas!
"""



"""DESEMPACOTAMENTO EM CHAMADAS DE FUNCAO

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'e', 'massa'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0        1        2
    ['Luiz', 'Joao', 'Eduarda', ],  # 2
]

# p, b, *_, ap, u =lista
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')
"""


"""OPERACAO TERNARIA

# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)
# digito = 9  # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)
print('Valor' if True else 'Outro valor' if True else 'Fim')
"""



"""EXERCICIO - GERAR O PRIMEIRO E O SEGUNDO DIGITO DE UM CPF EVENTUALMENTE O CPF COMLETO:

Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva comecando de 10

ex.:  746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*   7  4  6  8  2  4  8  9  0
    70  36  48  56  12  20  32 27 0

Somar todos so resultados:
70+36+48+56+12+20+32+27+0 = 301
multiplicar o resultado anterior por 10
301 * 10 = 3010
obvter o resto da divisao da conta anterior por 11
3010 % 11 = 7
se o resultado anterior for maior que 9:
    resultado e 0
contrario disso:
    resultado e o valor da conta

O primeiro digito do CPF e 7
"""
"""CODIGO DO EXERCICO:

cpf = '746824890'

soma = 0
multiplicador = 10

for digito in cpf:
    soma += int(digito) * multiplicador
    multiplicador -= 1

resultado = (soma * 10) % 11
primeiro_digito = 0 if resultado > 9 else resultado

cpf_com_primeiro = cpf +str(primeiro_digito)
soma = 0
multiplicador = 11

for digito in cpf_com_primeiro:
    soma += int(digito) * multiplicador
    multiplicador -= 1

resultado = (soma * 10) % 11
segundp_digito = 0 if resultado > 9 else resultado

cpf_completo = cpf + str(primeiro_digito) + str(segundp_digito)
print(f'CPF gerado completo: {cpf_completo}')
"""

"""CRIANDO UM GERADOR DE CPFs E VALIDADOR

import random

def calcular_digito(cpf_base, fator):
    soma = 0
    for digito in cpf_base:
        soma += int(digito) * fator
        fator -= 1
        resultado = (soma * 10) % 11
        return 0 if resultado > 9 else resultado
    
def gerar_cpf():
    cpf_base = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    d1 = calcular_digito(cpf_base, 10)
    d2 = calcular_digito(cpf_base + str(d1), 11)
    return cpf_base + str(d1) + str(d2)

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    
    cpf_base = cpf[:9]
    d1 = calcular_digito(cpf_base, 10)
    d2 = calcular_digito(cpf_base + str(d1), 11)
    return cpf == cpf_base + str(d1) + str(d2)

while True:
    print("\n1 - Gerar CPF")
    print("2 - Validar CPF")
    print("3 - Sair")

    escolha = input("Escolha uma opcao: ")

    if escolha == "1":
        cpf_gerado = gerar_cpf()
        print(f"CPF Gerado: {cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}")
    elif escolha == "2":
        cpf_input = input("Digite o CPF para validar (somente numeros ou formatado): ")
        if validar_cpf(cpf_input):
            print("CPF valido!")
        else:
            print("CPF invalido!")
    elif escolha == "3":
        print("Saindo...")
        break
    else:
        print("Opcao invalido. Tente novamente.")
"""