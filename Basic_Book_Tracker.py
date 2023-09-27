import mysql.connector

def create_table():
    db = mysql.connector.connect(host="localhost", user="root", password="Gande", database="MyBooks")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255))")
    db.close()

def add_book(title, author):
    db = mysql.connector.connect(host="localhost", user="root", password="Gande", database="MyBooks")
    cursor = db.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    db.commit()
    db.close()

def view_books():
    db = mysql.connector.connect(host="localhost", user="root", password="Gande", database="MyBooks")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    db.close()
    return books

def delete_book(id):
    db = mysql.connector.connect(host="localhost", user="root", password="Gande", database="MyBooks")
    cursor = db.cursor()
    cursor.execute("DELETE FROM books WHERE id=%s", (id,))
    db.commit()
    db.close()

create_table()
add_book('To Kill a Mockingbird', 'Harper Lee')
add_book('1984', 'George Orwell')
print(view_books())
delete_book(1)
print(view_books())
