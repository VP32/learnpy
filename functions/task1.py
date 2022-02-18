documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def validate_doc_no(doc_no):
    for document in documents:
        if document['number'] == doc_no:
            return True
    return False


def validate_directory(dir_no):
    for number in directories.keys():
        if number == dir_no:
            return True
    return False


def people(document_no):
    if not validate_doc_no(document_no):
        print(f'Документа номер {document_no} не существует!')
        return None
    for document in documents:
        if document['number'] == document_no:
            return document['name']
    return None


def shelf(document_no):
    if not validate_doc_no(document_no):
        print(f'Документа номер {document_no} не существует!')
        return None
    for direct, documents in directories.items():
        if document_no in documents:
            return direct
    return None


def list():
    docs = ''
    for document in documents:
        docs += f'{document["type"]} "{document["number"]}" "{document["name"]}"\n'
    return docs


def add(type, number, name, directory):
    if not validate_directory(directory):
        print(f'Полки {directory} не существует!')
    documents.append({"type": type, "number": number, "name": name})
    directories[directory].append(number)


def delete(document_no):
    if not validate_doc_no(document_no):
        print(f'Документа номер {document_no} не существует!')
        return
    directory = shelf(document_no)
    directories[directory].remove(document_no)

    doc = None
    for document in documents:
        if document['number'] == document_no:
            doc = document
            break
    documents.remove(doc)


def move(document_no, to_dir):
    if not validate_doc_no(document_no):
        print(f'Документа номер {document_no} не существует!')
        return
    if not validate_directory(to_dir):
        print(f'Полки {to_dir} не существует!')
        return
    from_dir = shelf(document_no)
    directories[from_dir].remove(document_no)
    directories[to_dir].append(document_no)


def add_shelf(directory):
    if validate_directory(directory):
        print(f'Полка {directory} уже существует')
        return
    directories.setdefault(directory, [])


while True:
    user_command = input('Введите команду (p,s,l,a,d,m,as, quit)')
    if user_command == 'p':
        doc_no = input('Введите номер документа: ')
        print(people(doc_no))
    elif user_command == 's':
        doc_no = input('Введите номер документа: ')
        print(shelf(doc_no))
    elif user_command == 'l':
        print(list())
    elif user_command == 'a':
        doc_type = input('Введите тип документа: ')
        doc_no = input('Введите номер документа: ')
        doc_name = input('Введите имя владельца: ')
        dir_no = input('Введите номер полки: ')
        add(doc_type, doc_no, doc_name, dir_no)
    elif user_command == 'd':
        doc_no = input('Введите номер документа: ')
        delete(doc_no)
    elif user_command == 'm':
        doc_no = input('Введите номер документа: ')
        dir_no = input('Введите целевой номер полки: ')
        move(doc_no, dir_no)
    elif user_command == 'as':
        dir_no = input('Введите номер новой полки: ')
        add_shelf(dir_no)
    elif user_command == 'quit':
        break
