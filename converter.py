ENTRADA = 'C:\\Users\\PC\\Desktop\\Telegrambot\\criandotermo\\palavras.txt'
SAIDA = 'C:\\Users\\PC\\Desktop\\Telegrambot\\criandotermo\\dicionario.txt'

with open(ENTRADA, encoding='UTF-8') as f:
    # linhas = f.readlines()
    testo = [e.strip() for e in f.readlines()]
    linhas = list(filter(lambda x: x != '', testo))

    for linha in linhas:
        linha.strip()
        if (len(linha) == 5 and linha.isalpha()):
            file_object = open(SAIDA, 'a', encoding='UTF-8')
            file_object.write(linha)
            file_object.write('\n')
            file_object.close()
