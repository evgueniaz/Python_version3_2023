# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь 
# также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения 
# и удаления данных


def add_contact(f):
    input_name = input('Input a first name:  ')
    input_surname = input('Input a last name:  ')
    input_phone = input('Input a phone number:  ')
    note = f'{input_surname} : {input_name} : {input_phone}'
    with open(f, 'a', encoding='utf-8') as pb:
        pb.write(f'{note}\n')
    print(f'The contact {note} has been added')


def read_phonebook(f):
    with open(f, 'r', encoding='utf-8') as pb:
        contacts = pb.readlines()
        return contacts


def print_all(f):
    ph_book = read_phonebook(f)
    for contact in ph_book:
        contact_1 = contact.replace(':', '')
        contact_1 = contact_1.replace('\n', '')
        print(contact_1)


def search_contact(f):
    search_key = input('Enter a name or a phone to be found:  ')
    ph_book = read_phonebook(f)
    print()
    count = 0
    contact = ''
    for line in ph_book:
        if search_key in line:
            count += 1
            contact = line.replace(':', '')
            contact = contact.replace('\n', '')
            print(contact)
    if contact == '':
        print(f'There is no such contact')
    print(f'There are {count} search results')
    

def replace_contact(f):
    search_key = input('Enter a name or a phone to be replaced:  ')
    ph_book = read_phonebook(f)
    print()
    count = 0
    for i in range(len(ph_book)):
        if search_key in ph_book[i]:
            count += 1
            contact = ph_book[i].replace(':', '')
            contact = contact.replace('\n', '')
            print(f'{i} {contact}')
    if count == 0:
        print(f'There is no such contact')
    else:
        print(f'There are {count} search results')
        confirm = input('\nChoose a number of the contact that will be replaced or '
                        'press z if you do not wish to change anything  > ')
        if confirm != 'z':
            input_name = input('Input a new first name:  ')
            input_surname = input('Input a new last name:  ')
            input_phone = input('Input a new phone number:  ')
            new_note = f'{input_surname} : {input_name} : {input_phone}\n'
            print(f'The contact   {ph_book[int(confirm)]}will be updated to   {new_note}')
            ph_book[int(confirm)] = new_note
            with open(f, 'w', encoding='utf-8') as pb:
                for line in ph_book:
                    pb.write(line)
        else:
            pass

        
def delete_contact(f):
    search_key = input('Enter a name or a phone to be replaced:  ')
    ph_book = read_phonebook(f)
    print()
    count = 0
    for i in range(len(ph_book)):
        if search_key in ph_book[i]:
            count += 1
            contact = ph_book[i].replace(':', '')
            contact = contact.replace('\n', '')
            print(f'{i} {contact}')
    if count == 0:
        print(f'There is no such contact')
    else:
        print(f'There are {count} search results')
        confirm = input('\nChoose a number of the contact that you wish to delete or '
                        'press z if you do not wish to change anything  > ')
        if confirm != 'z':
            print(f'The contact   {ph_book[int(confirm)]}will be deleted!')
            i = int(confirm)
            while i < len(ph_book) - 1:
                ph_book[i] = ph_book[i + 1]
                i += 1
            ph_book = ph_book[:-1]
            with open(f, 'w', encoding='utf-8') as pb:
                for line in ph_book:
                    pb.write(line)
        else:
            pass


def main():
    file = 'phonebook.txt'
    while True:
        print()
        user_choice = input('\n1 - add a contact,\n2 - read all phonebook,\n'
                            '3 - find a contact,\n4 - change a contact,\n'
                            '5 - delete a contact,\nz - to exit the phonebook\n> ')
        print()
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == '4':
            replace_contact(file)
        elif user_choice == '5':
            delete_contact(file)
        elif user_choice == 'z':
            print(f'Good bye!\n')
            break


if __name__ == '__main__':
    main()