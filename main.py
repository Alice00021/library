import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTabWidget, QTableWidget, QTableWidgetItem, QWidget
import psycopg2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Библиотека")
        self.resize(675, 500)

        # Создаем объект для соединения с базой данных
        self.conn = psycopg2.connect(
            dbname="Library",
            user="postgres",
            password="2118",
            host="localhost"
        )

        self.central_widget = QTabWidget()
        self.setCentralWidget(self.central_widget)

        self.create_books_tab()
        self.create_books_loans_tab()
        self.create_readers_tab()

    def create_books_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["ID", "Название книги", "Автор", "Жанр", "Наличие"])
        table.setColumnWidth(0, 50)  # Установка ширины первого столбца (ID) в 50 пикселей
        table.setColumnWidth(1, 200) 
        table.setColumnWidth(2, 200)
        table.setColumnWidth(3, 100)
        table.setColumnWidth(4, 100)
        layout.addWidget(table)
        tab.setLayout(layout)

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Books")
        books_data = cursor.fetchall()

        for row_index, row_data in enumerate(books_data):
            table.insertRow(row_index)
            for column_index, column_data in enumerate(row_data):
                table.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))

        self.central_widget.addTab(tab, "Книги")

    def create_books_loans_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["ID", "Дата начала", "Дата конца", "Дата возвращения" ,"ID книги", "ID читателя",])
        layout.addWidget(table)
        tab.setLayout(layout)

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Books_loans")
        loans_data = cursor.fetchall()

        for row_index, row_data in enumerate(loans_data):
            table.insertRow(row_index)
            for column_index, column_data in enumerate(row_data):
                table.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))

        self.central_widget.addTab(tab, "Выданные книги")

    def create_readers_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        table = QTableWidget()
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["ID", "Фамилия читателя", "Имя", "почта", "телефон"])
        layout.addWidget(table)
        tab.setLayout(layout)

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Readers")
        readers_data = cursor.fetchall()

        for row_index, row_data in enumerate(readers_data):
            table.insertRow(row_index)
            for column_index, column_data in enumerate(row_data):
                table.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))

        self.central_widget.addTab(tab, "Читатели")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())