"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
game = True

secret_word = 'casa'

word_encryption = ''
for letter in secret_word:
    word_encryption += '*'

count = 0

while game:
    qtd_letter_input = 0
    word_letter = ''

    while not (qtd_letter_input == 1):
        print('\nTry to guess the word!!!')
        if qtd_letter_input > 1:
            print("Enter only one digit")
        word_letter = input('\nEnter that only one letter: ')
        qtd_letter_input = len(word_letter)

    index_letter = 0
    for index, letter in enumerate(secret_word):
        if word_letter == letter:
            # index_letter = index
            word_encryption = word_encryption[:index] + \
                word_letter + word_encryption[index+1:]

    print(word_encryption)
    count += 1

    if not ('*' in word_encryption):
        game = False
        print(
            f'\nCongratulations!!!\nYou got the secret word right!!!\n{secret_word.upper()}')
