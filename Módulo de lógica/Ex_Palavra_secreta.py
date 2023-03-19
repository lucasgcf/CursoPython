tentativa = input('Digite uma letra: ')
palavra_secreta = 'laranja'
palavra_formatada = len(palavra_secreta) * '*'
t = 1
tentativa_l = tentativa.lower()
while True:
    if palavra_secreta == palavra_formatada:
        break
    while len(tentativa_l) > 1 or tentativa_l not in 'abcdefghijklmnopqrstuvwxyz':
        x = len(tentativa) > 1
        y = tentativa_l not in 'abcdefghijklmnopqrstuvwxyzçãõáéíóúâêîô'
        if x:
            print('Você digitou mais de um caractere!!!\n\n')

            tentativa = input('Digite novamente: ')
            t += 1
            tentativa_l = tentativa.lower()
            continue
        if y:
            print('Você não digitou uma letra!!!\n\n\n')

            tentativa = input('Digite novamente: ')
            t += 1
            tentativa_l = tentativa.lower
            continue
    while tentativa_l not in palavra_secreta:
        print(f'\n\nVocê errou, a letra "{tentativa_l}" não está na palavra!! ')
        tentativa = input('Tente outra letra: ')
        t += 1
        tentativa_l = tentativa.lower()
        break

    while tentativa_l in palavra_secreta:
        i = 0
        while i < len(palavra_secreta):
            if tentativa_l == palavra_secreta[i]:
                palavra_formatada = palavra_formatada[:i] + tentativa_l + palavra_formatada[i + 1:]

            i += 1
        if tentativa_l in palavra_formatada:

            if palavra_formatada == palavra_secreta:
                print('\n\nParabéns!!! você descobriu a palavra secreta.')
                print(f'\nNúmero de tentativas: {t}')
                break

            print(f'Acertou a letra {tentativa_l}!! A palavra ficou: {palavra_formatada}')
            tentativa = input(f'Digite outra letra: ')
            t += 1
            tentativa_l = tentativa.lower()
            i = 0
            if tentativa_l not in palavra_secreta:
                break
            continue

















