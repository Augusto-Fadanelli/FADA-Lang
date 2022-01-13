import re

# Palavras Reservadas
PR = [
    #(lexema, token)
    ('if', 'if'),
    ('input', 'input'),
    ('int', 'int'),
    ('str', 'str'),
    ('print', 'print'),
    ('else', 'else'),
    ('while', 'while'),
    ('break', 'break'),
    ('TRUE', 'True'),
    ('FALSE', 'False'),
    ('and', 'and'),
    ('or', 'or'),
]

# Operadores Relacionais
OR = [
    #(lexema, token)
    ('>', '>'),
    ('>=', '>='),
    ('<', '<'),
    ('<=', '<='),
    ('==', '=='),
    ('!=', '!='),
]

# Operadores Aritméticos
OAr = [
    #(lexema, token)
    ('+', '+'),
    ('-', '-'),
    ('/', '/'),
    ('*', '*'),
]

# Operador de Atribuição
OAt = [
    # (lexema, token)
    ('=', '='),
]

# Delimitadores
Del = [
    ('(', '('),
    (')', ')'),
    ('{', '{'),
    ('}', '}'),
    (',', ','),
    ('"', '"'),
]

# Verifica se é um lexema válido e mostra token
def verify(vet, word, tipo):
    r = False
    for y in vet:
        if word == y[0]:
            r = True
            print(f'{x} ({y[1]}, {tipo})')
            break
    return r

script = 'if a == ba = == a + c x,y 1a 10 b1 c4c 9.8'

lista = script.split()
lexemes = []
for indice, valor in enumerate(lista):
    temp = valor.split(',')
    lexemes += temp

for x in lexemes:

    next = False #Pular para a próxima palavra

    if verify(PR, x, 'PR'):
        continue

    if verify(OR, x, 'OR'):
        continue

    if verify(OAr, x, 'OAr'):
        continue

    if verify(OAt, x, 'OAt'):
        continue

    if verify(Del, x, 'Del'):
        continue

    # Ids de variáveis
    Id = re.findall(r'[a-zA-Z]+[a-zA-Z0-9]*', script)
    for y in Id:
        if x == y:
            next = True
            print(f'{x} ([a-zA-Z]+[a-zA-Z0-9]*, Id)')
            break

    if next:
        continue

    # NI - Números Inteiros
    NI = re.findall(r'[0-9]+', script)
    for y in NI:
        if x == y:
            print(f'{x} ([0-9]+, NI)')
            break
    else:
        print(f'ERRO: {x} não é um lexema válido!')
