from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100,100,200,300)
    window.setWindowTitle("My Simple GUI")

    layout = QVBoxLayout()

    label = QLabel("Press The Button Below")
    textbox = QTextEdit()
    button = QPushButton("Press Me!")
    button.clicked.connect(lambda: on_click(textbox.toPlainText()))

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.setLayout(layout)

    window.show()
    app.exec_()

def on_click(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()

if __name__ == "__main__":
    main()