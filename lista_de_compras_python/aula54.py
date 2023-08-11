"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os


def listing(shopping_list):
    if len(shopping_list) == 0:
        print('Your shopping list is empty!!')
    else:
        for index, item in enumerate(shopping_list):
            print(index, item)


shopping_list = []

while True:
    option = ''
    count = 0

    while option != 'i' and option != 'd' and option != 'r':
        if count >= 1:
            print('Enter an letter valid!\n')

        print('Select option for you:')
        option = input('[i]nsert [d]elete [r]ead? ').lower()

        count += 1
        os.system('cls')  # usa o comando no terminal

    if option == 'i':
        listing(shopping_list)
        new_item = input('\nEnter an new item: ')
        shopping_list.append(new_item)
        print('new item saved')

    if option == 'd':
        while True:
            listing(shopping_list)
            index_del = input('\nEnter the index you want to delete: ')
            try:
                index_del = int(index_del)
                shopping_list.pop(index_del)
                print('successfully deleted')
                break
            except:
                os.system('cls')
                print('Enter an integer above!!\n')

    if option == 'r':
        print('*'*5, 'Shopping list', '*'*5, '\n')
        listing(shopping_list)

    print('\nWant to get off the shopping list')
    option = input('Quit?(y / n) ').lower()
    if option == 'y':
        break
    else:
        os.system('cls')
        continue
