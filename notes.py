def show_all(fileName):
    print(' Мои заметки: ')
    with open(fileName, 'r', encoding='utf-8') as data:
         for i, line in enumerate(data):
            print('%02d %s'%(i+1, line), end='')
    print('')


def export_note(fileName):
    with open(fileName, 'a', encoding = 'utf-8') as data: 
        noteName = input('Введите название заметки: ')
        noteText = input('Введите текст: ')
        data.write(f'{str.upper(noteName)}. {noteText}\n')
        print(f'Добавлена новая заметка :\n {str.upper(noteName)} \n {noteText}\n')


def edit_note(fileName):
    print(' Мои заметки:')
    with open(fileName, 'r', encoding='utf-8') as data:
        for i, line in enumerate(data):
            print('%02d %s'%(i+1, line), end='')
    print('')
    with open(fileName, 'r', encoding='utf-8') as data:
        all_notes = data.read()
    index_edit_note = int(input('Введите номер заметки для редактирования: ')) - 1
    note_lines = all_notes.split('\n')
    edit_note_lines = note_lines[index_edit_note]
    elements = edit_note_lines.split('. ')
    name = input('Введите название заметки: ')
    text = input('Введите текст: ')
    if len(name) == 0:
        name = elements[1]
    if len(text) == 0:
        text = elements[2]
    edited_line = f'{str.upper(name)}. {text}'
    note_lines[index_edit_note] = edited_line
    print(f'Запись: {edit_note_lines}. Изменена на: {edited_line}\n')
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write('\n'.join(note_lines))


def delete_note(fileName):
    print(' Мои замеки:')
    with open(fileName, 'r', encoding='utf-8') as data:
        for i, line in enumerate(data):
            print('%02d %s'%(i+1, line), end='')
    print('')
    with open(fileName, 'r', encoding='utf-8') as data:
        all_notes = data.read()
    index_delete_note = int(input('Введите номер заметки для удаления: ')) - 1
    note_lines = all_notes.split('\n')
    del_note = note_lines[index_delete_note]
    note_lines.pop(index_delete_note)
    print(f'Удалена запись: {del_note}\n')
    with open(fileName, 'w', encoding='utf-8') as data:
        data.write("\n".join(note_lines))

def main():
    selection = -1
    myNotes = 'notes.csv'

    while selection != 0:
        print('Выберите необходимое действие:')
        print('1 - Показать все заметки')
        print('2 - Добавить новую заметку')
        print('3 - Изменить существующую заметку')
        print('4 - Удалить заметку')
        print('0 - Завершить работу программы')
        select = int(input('Ваш выбор: '))
        if select == 1:
            show_all(myNotes)
        elif select == 2:
            export_note(myNotes)
        elif select == 3:
            edit_note(myNotes)
        elif select == 4:
            delete_note(myNotes)
        else:
            selection = 0


if __name__ == '__main__':
    main()
