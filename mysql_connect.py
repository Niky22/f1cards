def sql_write_AllUsers(username, url, fullname, user_id):
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'Nikita2303',
                'database': 'telegrambot', }
    import mysql.connector
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into AllUsers  
           (username, url, fullname, user_id)  
           values 
           (%s, %s, %s, %s)"""
    cursor.execute(_SQL, (username, url, fullname, user_id))
    conn.commit()
    pass


def get_catalog():
    import mysql.connector
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'Nikita2303',
                'database': 'telegrambot', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT catalog FROM catalog ORDER BY id DESC LIMIT 1;''')
    result = cursor.fetchall()
    return result


def write_catalog(catalog, date):
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'Nikita2303',
                'database': 'telegrambot', }
    import mysql.connector
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into catalog 
               (catalog, date)  
               values 
               (%s, %s)"""
    cursor.execute(_SQL, (catalog, date))
    conn.commit()
    pass


def get_url_allusers():
    import mysql.connector
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'Nikita2303',
                'database': 'telegrambot', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT url FROM AllUsers;''')
    result = cursor.fetchall()
    return result


def get_id_allusers():
    import mysql.connector
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'Nikita2303',
                'database': 'telegrambot', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT user_id FROM AllUsers;''')
    result = cursor.fetchall()
    return result

def get_numberusers():
    import mysql.connector
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'Nikita2303',
                'database': 'telegrambot', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT COUNT(1) FROM ALLUsers;''')
    result = cursor.fetchall()
    return result


def write_catalog_stat(user, date):
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'Nikita2303',
                'database': 'telegrambot', }
    import mysql.connector
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into catalog_stat
               (user, date)  
               values 
               (%s, %s)"""
    cursor.execute(_SQL, (user, date))
    conn.commit()
    pass


def get_numbercatalog():
    import mysql.connector
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'Nikita2303',
                'database': 'telegrambot', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT COUNT(1) FROM catalog_stat;''')
    result = cursor.fetchall()
    return result


def allusers():
    import mysql.connector
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'Nikita2303',
                'database': 'telegrambot', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT * FROM AllUsers;''')
    result = cursor.fetchall()
    return result


def catalog():
    import mysql.connector
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'Nikita2303',
                'database': 'telegrambot', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT * FROM catalog;''')
    result = cursor.fetchall()
    return result


def stat_catalog():
    import mysql.connector
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'Nikita2303',
                'database': 'telegrambot', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT * FROM catalog_stat;''')
    result = cursor.fetchall()
    return result