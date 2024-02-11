main_menu = '''\nГлавное меню:
		1. Открыть файл  
		2. Записать файл 
		3. Показать заметки 
		4. Добавить заметку 
		5. Найти заметку 
		6. Изменить заметку 
		7. Удалить заметку 
		8. Выход  \n '''

input_choice = 'Выберите пункт меню: '
notes_file_name = 'data_file.txt'

load_successful = 'Запись успешно открыта'
save_successful = 'Запись успешно сохранена'

load_error = 'Заметок нет или они не прочитаны'

input_new_note = 'Введите данные нового контакта:\n НЕ забудьте после добавления заметки нажать на Записать файл \n  '
new_notes = {'title': 'Введите заголовок заметки: ',
               'note': 'Введите опимание заметки: '}

def new_note_successful(title: str):
		return f'Заметка {title} успешно добавлена.'

cancel_input = 'Отмена ввода'

index_del_note = 'Введите номер заметки, которую нужно удалить: '
def del_note(title: str):
		return f'Заметка {title} успешно удалёна!'

input_change = 'Какую заметку хотите изменить: '
input_index = 'Введите номер заметки: '

change_note = 'Введите новые данные или оставьте поле пустым: '

def change_successful(title: str | dict) -> str:
    return f'Заметка {title} успешно изменена!'

input_search = 'Какую заметку хотите найти? '
def empty_search(word) -> str:
    return f'Заметки содержащие слово "{word}" Не найдены!'