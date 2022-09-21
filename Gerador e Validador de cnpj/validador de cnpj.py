import funcoes

while True:

    acao = input('Digite\n[0] para validar um cnpj ou \n[1] para gerar um cnpj: ')

    if acao == '0':
        cnpj1 = input('Digite um cnpj para validar: ')

        if funcoes.valida(cnpj1):
            print(f'{cnpj1} é válido.')
        else:
            print(f'{cnpj1} é inválido.')
    elif acao == '1':
        qtd_cnpj = int(input("Digite quantos cnpj's deseja gerar: "))
        for i in range(qtd_cnpj):
            novo_cnpj = funcoes.gera()
            formatado = funcoes.formata(novo_cnpj)
            print(formatado)
    
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break



