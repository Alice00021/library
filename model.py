import psycopg2
class LibraryModel:
    def __init__(self):
        # Инициализация модели, например, соединение с базой данных
        self.conn = psycopg2.connect(
            dbname="Library",
            user="postgres",
            password="2118",
            host="localhost"
        )

    def get_books_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Books")
        return cursor.fetchall()

    def get_loans_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Books_loans")
        return cursor.fetchall()

    def get_readers_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Readers")
        return cursor.fetchall()