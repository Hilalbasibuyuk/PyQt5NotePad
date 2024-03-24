from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QTextEdit,QApplication, QWidget,QAction,QFileDialog,QShortcut,QColorDialog
from PyQt5.QtGui import QTextCharFormat, QFont, QColor,QKeySequence
import sys

class NotePad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.properties()

        self.setWindowTitle("NotePad")
        self.setGeometry(300,300,600,600)

    def properties(self):
        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        file_menu2 = menu.addMenu("Style")

        new_page = QAction("New page",self)
        new_page.setShortcut("Ctrl+N")
        new_page.triggered.connect(self.new_file)
        file_menu.addAction(new_page)

        open_page = QAction("Open page",self)
        open_page.setShortcut("Ctrl+O")
        open_page.triggered.connect(self.open_file)
        file_menu.addAction(open_page)

        save_page = QAction("Save file",self)
        save_page.setShortcut("Ctrl+S")
        save_page.triggered.connect(self.save_file)
        file_menu.addAction(save_page)

        file_menu.addSeparator()

        quit_page = QAction("Quit file",self)
        quit_page.setShortcut("Ctrl+Q")
        quit_page.triggered.connect(self.close)
        file_menu.addAction(quit_page)

        bold_style = QAction("Bold",self)
        bold_style.setShortcut("Ctrl+K")
        bold_style.triggered.connect(self.set_bold)
        file_menu2.addAction(bold_style)

        color = QAction("Color",self)
        color.triggered.connect(self.set_color)
        file_menu2.addAction(color)

    def set_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            cursor = self.text_edit.textCursor()
            char_format = QTextCharFormat()
            char_format.setForeground(color)
            cursor.mergeCharFormat(char_format)
            self.text_edit.setCurrentCharFormat(char_format)

    def init_bold(self):
        bold_shortCut = QShortcut(QKeySequence("Ctrl+K"),self)
        bold_shortCut.activated.connect(self.set_bold)

    def set_bold(self):
        cursor = self.text_edit.textCursor()
        if not cursor.hasSelection():
            return

        char_format = QTextCharFormat()
        char_format.setFontWeight(QFont.Bold)
        cursor.mergeCharFormat(char_format)
        self.text_edit.setCurrentCharFormat(char_format)

    def new_file(self):
        self.text_edit.clear()

    def open_file(self):
        file_name, _ =  QFileDialog.getOpenFileName(self,"Open file", ".", "Metin Dosyaları (*.txt)")
        if file_name:
            with open(file_name, "r") as file:
                self.text_edit.setText(file.read())
    
    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self,"Save file",".","Metin Dosyaları (*.txt)")
        if file_name:
            with open("file_name","w") as file:
                file.write(self.text_edit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotePad()
    window.show()
    sys.exit(app.exec_())