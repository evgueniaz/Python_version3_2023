import text

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '='*len(message))
    print(message)
    print('='*len(message) + '\n')


def print_contacts(book: list[dict[str, str]], error: str):
    if book:
        for contact in book:
            print('\n' + '='*71)
            print(f'{contact.get("id"):>3}. {contact.get("name"):<20} | {contact.get("phone"):<20} | {contact.get("comment"):<20}')
            print('='*71 + '\n')
    else:
        print(error)


def input_contact(message) -> dict[str, str]:
    new = {}
    print(message)
    for key, txt in text.new_contact.items():
        value = input(txt)
        if value:
            new[key] = value
    return new
    

def input_search(message) -> str:
    return input(message)


def input_index(message) -> str:
    return input(message)





