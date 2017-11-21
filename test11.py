#coding: utf8
import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        okButton=QtGui.QPushButton("OK")
        cancelButton=QtGui.QPushButton("Cancel")

######################################################
        hbox=QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox=QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
######################################################
        # vbox=QtGui.QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addWidget(okButton)
        # vbox.addWidget(cancelButton)
        #
        # hbox=QtGui.QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addLayout(vbox)
        #
        # self.setLayout(hbox)
######################################################


        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Button')
        self.show()

def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()