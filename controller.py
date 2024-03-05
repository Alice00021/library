from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTabWidget, QTableWidget, QTableWidgetItem, QWidget
from view import *
from model import *
class LibraryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.populate_books_table()
        self.populate_loans_table()
        self.populate_readers_table()

    def populate_books_table(self):
        books_data = self.model.get_books_data()
        self.populate_table(self.view.books_table, books_data)

    def populate_loans_table(self):
        loans_data = self.model.get_loans_data()
        self.populate_table(self.view.loans_table, loans_data)

    def populate_readers_table(self):
        readers_data = self.model.get_readers_data()
        self.populate_table(self.view.readers_table, readers_data)

    def populate_table(self, table, data):
        table.setRowCount(0)
        for row_index, row_data in enumerate(data):
            table.insertRow(row_index)
            for column_index, column_data in enumerate(row_data):
                table.setItem(row_index, column_index, QTableWidgetItem(str(column_data)))