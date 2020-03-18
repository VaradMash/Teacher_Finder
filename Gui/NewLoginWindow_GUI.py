from PyQt5 import QtWidgets,uic
import excel1 as e
import sys
import SlotSelect as s


app=QtWidgets.QApplication([])
nlw=uic.loadUi('facultywindow.ui')
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
    tp1.backPB.clicked.connect(backLogin)
    

def backLogin():
    tp1.setVisible(False)
    nlw.setVisible(True)

def comboBox():
    tName=nlw.comboBox1.currentText()
    #the above will return the value of the selected name in the drop down menu/Combo box
    tSlot=nlw.comboBox2.currentIndex()
    #the above will get the time slot in string format

    #Getting he cel value
    f=s.get_slot(tName,tSlot,1)
    print(f)

    #temporary labels to test the values
    nlw.labelx.setText(str(tName))
    nlw.labely.setText(str(tSlot))

'''app1=QtWidgets.QApplication([])
newui=uic.loadUi('PasswordCheck.ui')'''
nlw.proceedNLW.clicked.connect(teacherlogin)
#nlw.proceedNLW.clicked.connect(clo)
nlw.submitNLW.clicked.connect(comboBox)
pdisplay.proceedPB.clicked.connect(passwordDisplay)
nlw.show()
app.exec()

