import sqlite3


def iterativeSearch():
    DBusername = []
    DBpassword = []
    connection = sqlite3.connect('BSLComprehension.login_credentials')
    transfer = connection.cursor()
    transfer.execute('SELECT username FROM username')
    DBusername = transfer.fetchall()
    transfer.execute('SELECT password FROM password')
    DBpassword = transfer.fetchall()
    connection.close()
    return(DBusername, DBpassword)


def authorise(usernamePy, passwordPy):
    tablevalues = iterativeSearch()
    for i in range(len(tablevalues[0])):
        username = list(tablevalues[0][i]).pop()
        password = list(tablevalues[1][i]).pop()
        if username == usernamePy:
            if password == str(passwordPy):
                return True
    return False


