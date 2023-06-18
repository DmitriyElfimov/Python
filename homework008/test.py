phone_book = {}
path: str = 'homework008/phones.txt'
import console as cl

def open_file():
    phone_book.clear()
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}
    print(cl.print_input)


def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i),contact.get('name'),contact.get('phone'),contact.get('comment')])
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    print(data)
    print(cl.print_save)
    print('=' * 200 + '\n')

def show_contacts(book: dict[int, dict]):
    print('\n' + '=' * 200)
    for i, cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
    print('=' * 200 + '\n')

def add_contact():
    uid = max(list(phone_book.keys())) + 1

    name = input(cl.input_name)
    phone = input(cl.input_phone)
    comment = input(cl.input_comment)
    phone_book[uid] = {'name': name, 'phone': phone, 'comment': comment}

    print(f'{cl.print_contact} {name} {cl.add_ok}')


def search():
    result = {}
    word = input(cl.input_search)
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
            result[i] = contact
    return result


def replace():
    replace_id = int(input(cl.input_replace))
    name = input(cl.input_name)
    phone = input(cl.input_phone)
    comment = input(cl.input_comment)
    phone_book[replace_id] = {'name': name, 'phone': phone, 'comment': comment}

    print(f'{cl.print_contact} {name} {cl.replace_ok}')


def delete():
    del_id = int(input(cl.input_delete))
    name = phone_book[del_id].get("name")
    phone_book.pop(del_id)
    print(f'{cl.print_contact} {name} {cl.del_ok}')


def menu() -> int:
    main_menu = cl.main_menu
    print(main_menu)
    while True:
        select = input(cl.input_select)
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print(cl.print_error)


open_file()
while True:
    select = menu()
    match select:
        case 1:
            open_file()
    match select:
        case 2:
            save_file()
    match select:
        case 3:
            show_contacts(phone_book)
    match select:
        case 4:
            add_contact()
    match select:
        case 5:
            result = search()
            show_contacts(result)
    match select:
        case 6:
            replace()
    match select:
        case 7:
            delete()
    match select:
        case 8:
            print(cl.print_goodbay)
            break