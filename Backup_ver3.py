'''Программа не работет, но нужна для урока'''
import os
import time

# 1) Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\My Documents"']       # Если есть пробелы, нужно ставить "двойные скобки"
# Заметьте, что для имен, содержащих пробелы, необходимо использовать двойные кавычки внутри строки.

# 2) Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'D:\\Backup1'

# 3) Файлы помещаются в zip-архив.
# 4) Текущая дата служит именем подкаталога в основном каталоге.
today = target_dir + os.sep + time.strftime('%Y%m%d')     # os.sep - для переносимости на все ОС, В винде ставит "\\"
now = time.strftime('%H%M%S')     # Текущее время служит именем zip-архива.

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0:     #Проверяем, введен ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ','_') + '.zip'      #Операнд \ указывает на продолжение логической строки

#Создаем каталог, если его нет.
if not os.path.exists(today):
    os.mkdir(today) # создание подкаталога
print('Каталог успешно создан',today)

# 5) Используем команду "zip" для помещения файлов в zip-архив.
zip_command = 'C:\\"Program Files"\\7-Zip\\7z a -t7z "%s" %s' %(target,' '.join(source))  # join - превращает список в строку
#Открывает программу 7-zip в фоновом режиме и создает через нее архив
# %s - плайсхолдер строки, %d - плейсхолдер числа

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в',target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
