from PyQt5 import QtWidgets
from PyQt5 import QtGui

from PyQt5.QtCore import Qt, QSize,QDate

import sys

class chargment(QtWidgets.QLabel):
    def __init__(self):
        super(chargment, self).__init__()
        self.anim=QtGui.QMovie("animation\\a.gif")
        self.setMovie(self.anim)
        self.anim.start()
        self.msg=QtWidgets.QLabel("veuillez patienter..",self)
        self.msg.setGeometry(100,120,250,250)
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.msg.setFont(font)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.move(250,100)
        self.show()

app = QtWidgets.QApplication(sys.argv)
#test = regrouper()
#test=MenuMed()
#test=seconnecter()
attente=chargment()
#est=menuprincipale()
#test=comptemed("sofia","asmi nskon f hussein dey","0987654321")
app.exec_()