from PyQt5 import QtWidgets,uic
import excel1 as e

app=QtWidgets.QApplication([])
dic=uic.loadUi('loginwindow1.ui')

def teacherlogin():
    
    username=dic.usernameLE.text()
    
    '''Accept username and fetch password for the same'''
    password=dic.passwordLE.text()

    v=e.logcheck()
    print('dd')
    ver=v.verify(username,password)
    print('jiss')
    
    if ver==True:
        print('hi')
        dic.lineEdit.setText('Password is ok')
       
    else:
        print('ji')
        dic.lineEdit.setText('Password incorrect')
        
        

dic.pushButton.clicked.connect(teacherlogin)
dic.show()
app.exec()
