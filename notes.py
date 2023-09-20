"""Необходимо написать проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, сохранять её,
 читать список заметок, редактировать заметку, удалять заметку."""
 
def show_all(fileName):
    print(' Мои заметки: ')
    with open(fileName, 'r', encoding='utf-8') as data:
        print(data.read())
    print('')


def export_data(fileName):
    with open(fileName, 'a', encoding = 'utf-8') as data: 
        noteName = input('Введите название заметки: ')
        noteText = input('Введите текст: ')
        data.write(f'{noteName} - {noteText}\n')
        print(f'Добавлена новая заметка :\n {str.upper(noteName)} \n {noteText}\n')

