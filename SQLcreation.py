import sqlite3

connection = sqlite3.connect("BSLComprehension.login_credentials")

connection.execute('''CREATE TABLE IF NOT EXISTS username(
                    firstname text,
                    lastname text,
                    email text,
                    username text
                    ) ''')
connection.execute('''CREATE TABLE IF NOT EXISTS password(
                    firstname text,
                    lastname text,
                    password text
                    )''')

connection.execute("INSERT INTO username VALUES(:firstname, :lastname, :email, :username)",
                   {"firstname": "master", "lastname": "master", "email": "master@gmail.com", "username": "master"})

connection.execute("INSERT INTO password VALUES(:firstname, :lastname, :password)",
                   {"firstname": "master", "lastname": "master", "password": "b'w5rDgsOmw6jDisOk'"})
connection.commit()

connection.close()
