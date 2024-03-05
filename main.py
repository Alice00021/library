from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTabWidget, QTableWidget, QTableWidgetItem, QWidget
from view import *
from model import *
from controller import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = LibraryModel()
    view = LibraryView()
    controller = LibraryController(model, view)
    view.show()
    sys.exit(app.exec())