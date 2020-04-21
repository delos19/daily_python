from PyQt5.QtWidgets import *
app = QApplication([])
app.setStyle('Fusion')

button = QPushButton('Click')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You pressed the button')
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()

window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()
        
