from PyQt5 import QtWidgets,uic
import excel1 as e
import sys


app=QtWidgets.QApplication([])
nlw=uic.loadUi('NewLoginWindow.ui')
app1=QtWidgets.QApplication([])
tp1=uic.loadUi('TeacherPortal1.ui')
app2=QtWidgets.QApplication([])
pdisplay=uic.loadUi('PasswordDisplay.ui')

def teacherlogin():
    
    username=nlw.usernameLE.text()
    password=nlw.passwordLE.text()

    v=e.logcheck()
    ver=v.verify(username,password)

    passwordDisplay(ver)
    
def passwordDisplay(ver):
    app2.exec()
    nlw.setVisible(False)
    pdisplay.setVisible(True)
    
    if ver==True:
        pdisplay.PasswordDisplayLE.setText('The password is correct')
        pdisplay.proceedPB.clicked.connect(passwordCorrect)

        
    else:
        pdisplay.PasswordDisplayLE.setText('The password is incorrect')
        pdisplay.proceedPB.clicked.connect(passwordIncorrect)


def passwordCorrect():
    app1.exec()
    pdisplay.setVisible(False)
    tp1.setVisible(True)
    teacherPortal1()
   

def passwordIncorrect():
    pdisplay.setVisible(False)
    nlw.setVisible(True)
                       
def teacherPortal1():
    
    #tp1.show()
    #app1.exec()
    tp1.pushButton.clicked.connect(backLogin)
    
def backLogin():
    tp1.setVisible(False)
    nlw.setVisible(True)
    

'''app1=QtWidgets.QApplication([])
newui=uic.loadUi('PasswordCheck.ui')'''
nlw.proceedNLW.clicked.connect(teacherlogin)
#nlw.proceedNLW.clicked.connect(clo)
pdisplay.proceedPB.clicked.connect(passwordDisplay)
nlw.show()
app.exec()

