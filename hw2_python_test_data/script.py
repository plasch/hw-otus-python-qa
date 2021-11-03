import json
from csv import DictReader
from books_parsing import divide_books_btw_users

books = []
result = []

with open('data/books.csv', 'r', encoding='utf-8') as file_csv:
    reader = DictReader(file_csv)
    for book in reader:
        data = {
            'title': book['Title'],
            'author': book['Author'],
            'pages': book['Pages'],
            'genre': book['Genre']
        }
        books.append(data)

    with open('data/users.json', 'r', encoding='utf-8') as file_json:
        users = json.load(file_json)

        for user, book in zip(users, divide_books_btw_users(books, users)):
            data = {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age'],
                'books': book
            }
            result.append(data)

with open('result.json', 'w', encoding='utf-8') as file:
    result = json.dumps(result, indent=4)
    file.write(result)
