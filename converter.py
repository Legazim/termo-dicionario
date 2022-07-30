ENTRADA = 'palavras.txt'
SAIDA_TXT = 'dicionario.txt'
SAIDA_LIST = 'palavras_validas.py'

with open(ENTRADA, encoding='UTF-8') as f:
    testo = [e.strip() for e in f.readlines()]
    linhas = list(filter(lambda x: x != '', testo))

    for linha in linhas:
        linha.strip()
        if (len(linha) == 5 and linha.isalpha()):
            file_object = open(SAIDA_TXT, 'a', encoding='UTF-8')
            file_object.write(linha)
            file_object.write('\n')
            file_object.close()


with open(ENTRADA, encoding='UTF-8') as f:
    testo = [e.strip() for e in f.readlines()]
    linhas = list(filter(lambda x: x != '', testo))

    file_object = open(SAIDA_LIST, 'a', encoding='UTF-8')
    file_object.write('palavras_validas = [\n')
    for linha in linhas:
        linha.strip()
        if (len(linha) == 5 and linha.isalpha()):
            file_object.write(f'    \"{linha}\",\n')

    file_object.write(']')
    file_object.close()