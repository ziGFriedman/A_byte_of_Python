'''Оператор Continue'''
while True:
    s = input('Введите что-нибудь: ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue  #пропускает все оставшиеся команды и продолжает цикл со след. итерации
    print('Введённая строка достаточной длины')
    # здесь могут быть разные действия