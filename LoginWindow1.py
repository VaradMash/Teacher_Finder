from PyQt5 import QtWidgets,uic
import excel1 as e
import sys


app=QtWidgets.QApplication([])
dic=uic.loadUi('loginwindow1.ui')

def teacherlogin():
    
    username=dic.usernameLE.text()
    
    '''Accept username and fetch password for the same'''
    password=dic.passwordLE.text()

    v=e.logcheck()
    ver=v.verify(username,password)
    
    if ver==True:
        dic.lineEdit.setText('Password is correct')
       
    else:
        dic.lineEdit.setText('Password incorrect')

def clo():
    #app.close()
    
    dic.setVisible(False)
    newui.show()
    app1.exec()
    newui.pushButton.clicked.connect(ope)
def ope():
    newui.setVisible(False)
    dic.setVisible(True)
    

app1=QtWidgets.QApplication([])
newui=uic.loadUi('sample.ui')
dic.pushButton.clicked.connect(teacherlogin)
dic.pushButton_3.clicked.connect(clo)
dic.show()
app.exec()

