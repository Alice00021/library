import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTabWidget, QTableWidget, QTableWidgetItem, QWidget
import psycopg2
from model import Data

class LibraryView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Библиотека")
        self.resize(675, 500)
        self.central_widget = QTabWidget()
        self.setCentralWidget(self.central_widget)

        self.create_books_tab()
        self.create_books_loans_tab()
        self.create_readers_tab()

    def create_books_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.books_table = QTableWidget()
        self.books_table.setColumnCount(5)
        self.books_table.setHorizontalHeaderLabels(["ID", "Название книги", "Автор", "Жанр", "Наличие"])
        self.books_table.setColumnWidth(0, 50)  # Установка ширины первого столбца (ID) в 50 пикселей
        self.books_table.setColumnWidth(1, 200) 
        self.books_table.setColumnWidth(2, 200)
        self.books_table.setColumnWidth(3, 100)
        self.books_table.setColumnWidth(4, 100)
        layout.addWidget(self.books_table)
        tab.setLayout(layout)
        self.central_widget.addTab(tab, "Книги")

    def create_books_loans_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.loans_table = QTableWidget()
        self.loans_table.setColumnCount(6)
        self.loans_table.setHorizontalHeaderLabels(["ID", "Дата начала", "Дата конца", "Дата возвращения", "ID книги", "ID читателя"])
        layout.addWidget(self.loans_table)
        tab.setLayout(layout)
        self.central_widget.addTab(tab, "Выданные книги")

    def create_readers_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.readers_table = QTableWidget()
        self.readers_table.setColumnCount(5)
        self.readers_table.setHorizontalHeaderLabels(["ID", "Фамилия читателя", "Имя", "почта", "телефон"])
        layout.addWidget(self.readers_table)
        tab.setLayout(layout)
        self.central_widget.addTab(tab, "Читатели")