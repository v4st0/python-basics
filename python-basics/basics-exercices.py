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