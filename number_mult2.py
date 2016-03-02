from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)



        nameLabel = QLabel("1st number:")
        self.nameLine = QLineEdit()
        self.submitButton = QPushButton("SUBMIT_1")

        nameLabel_2 = QLabel("2nd number:")
        self.nameLine_2 = QLineEdit()
        self.submitButton_2 = QPushButton("SUBMIT_2")

        nameLabel_3 = QLabel(" ")
        self.submitButton_3 = QPushButton("CALCULATE")

        nameLabel_4 = QLabel("answer to 2 decimal places")

        nameLabel_5 = QLabel("answer")
        self.nameLine_5 = QLineEdit()





        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(nameLabel)
        buttonLayout1.addWidget(self.nameLine)


        buttonLayout2 = QVBoxLayout()
        buttonLayout2.addWidget(nameLabel_2)
        buttonLayout2.addWidget(self.nameLine_2)


        buttonLayout3 = QVBoxLayout()
        buttonLayout3.addWidget(nameLabel_3)
        buttonLayout3.addWidget(self.submitButton_3)

        buttonLayout4 = QVBoxLayout()
        buttonLayout4.addWidget(nameLabel_4)

        buttonLayout5 = QVBoxLayout()
        buttonLayout5.addWidget(nameLabel_5)
        buttonLayout5.addWidget(self.nameLine_5)





        self.submitButton_3.clicked.connect(self.submitContact_3)


        mainLayout = QGridLayout()
        # mainLayout.addWidget(nameLabel, 2, 2)

        mainLayout.addLayout(buttonLayout4, 0, 0)
        mainLayout.addLayout(buttonLayout1, 1, 0)
        mainLayout.addLayout(buttonLayout2, 1, 1)
        mainLayout.addLayout(buttonLayout3, 2, 0)
        mainLayout.addLayout(buttonLayout5, 2, 1)

        self.setLayout(mainLayout)
        self.setGeometry(100, 100, 300, 100)
        self.setWindowTitle("2 number multiplication")






    def submitContact_3(self):
        name = self.nameLine.text()
        name2 = self.nameLine_2.text()
        x = float(name)
        y = float(name2)

        answer = x * y
        answer = format(answer, '.2f')
        z = str(answer)


        self.nameLine_5.setText(z)




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
