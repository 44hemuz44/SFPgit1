import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit


def addLabel(layout, text):
    layout.addWidget(QLabel(text))


# Create the Qt Application
app = QApplication(sys.argv)

# Create the parent Widget and the QVBoxLayout Layout Manager
window = QWidget()
layout = QVBoxLayout(window)

# Create a label Widget and add it to the layout
label = QLabel('Введите номер телефона')
layout.addWidget(label)

line_edit = QLineEdit()
layout.addWidget(line_edit)

# Create a QPushButton object with a caption on it
qbtn = QPushButton('Зарегестрироваться')

# Add the QPushButton to the layout
layout.addWidget(qbtn)

# Close the application when the button is pressed
# Here I am using slots & signals, which I will demonstrate later in this tutorial
qbtn.clicked.connect(lambda: addLabel(layout, line_edit.text()))

# Create a QPushButton object with a caption on it
qbtn = QPushButton('Далее')

# Add the QPushButton to the layout
layout.addWidget(qbtn)


# Show the parent Widget
window.show()

# Run the main Qt loop
sys.exit(app.exec())