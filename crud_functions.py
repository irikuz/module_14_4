import sqlite3


def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT ,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def database_filler(title_product, descr_product=' ', price_product=0):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    check_product = cursor.execute("SELECT * FROM Products WHERE title= ?", (title_product,))
    if check_product.fetchone() is None:
        cursor.execute('INSERT INTO Products (title,description,price ) VALUES(?, ?, ?)',
                       (f'{title_product}', f'{descr_product}', f'{price_product}')
                       )
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


initiate_db()

for i in range(1, 5):
    database_filler(f'Product {i}', f'Описание {i}', i * 100)