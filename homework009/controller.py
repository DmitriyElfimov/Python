import text
import view
import model


def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                repl_id = int(view.replace_contact())
                new = view.add_contact()
                model.replace(repl_id, new)
                view.print_message(text.repl_successful(new.get('name')))
            case 7:
                del_id = view.del_contact()
                name = model.del_contact(del_id)
                view.print_message(text.del_successful(name))
            case 8:
                view.print_message(text.exit_file)
                break
        