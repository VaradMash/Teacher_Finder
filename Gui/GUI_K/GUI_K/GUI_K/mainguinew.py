from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage,QPalette,QBrush,QPixmap
from PyQt5.QtWidgets import*
import sys
import excel1 as e
import SlotSelect as s

app=QtWidgets.QApplication([])
fp=uic.loadUi('FirstPage.ui')
app1=QtWidgets.QApplication([]) #student window
sw=uic.loadUi('studentwindow.ui')
app2=QtWidgets.QApplication([]) #faculty window
fw=uic.loadUi('facultywindow.ui')
app3=QtWidgets.QApplication([])
pdisplay=uic.loadUi('PasswordDisplay.ui')
app4=QtWidgets.QApplication([])
tp=uic.loadUi('TeacherPortal1.ui')

def studentwin():
    app1.exec()
    fp.setVisible(False)
    sw.setVisible(True)

    sw.submitNLW_2.clicked.connect(comboBox)

def comboBox():
    tName=sw.comboBox1_2.currentText()
    #the above will return the value of the selected name in the drop down menu/Combo box
    tSlot=sw.comboBox2_2.currentIndex()
    #the above will get the time slot in string format

    #Getting he cel value
    f=s.get_slot(tName,tSlot,1)
    print(f)

    #temporary labels to test the values
    sw.labelx_2.setText(str(tName))
    sw.labely_2.setText(str(tSlot))

def facultywin():
    app2.exec()
    fp.setVisible(False)
    fw.setVisible(True)
    #teacherlogin()

#def teacherlogin():
    
    username=fw.usernameLE.text()
    password=fw.passwordLE.text()

    v=e.logcheck()
    ver=v.verify(username,password)
    passwordDisplay(ver)
    
    
def passwordDisplay(ver):
    app3.exec()
    fw.setVisible(False)
    pdisplay.setVisible(True)
    
    if ver==True:
        pdisplay.PasswordDisplayLE.setText('The password is correct')
        pdisplay.proceedPB.clicked.connect(passwordCorrect)

        
    else:
        pdisplay.PasswordDisplayLE.setText('The password is incorrect')
        pdisplay.proceedPB.clicked.connect(passwordIncorrect)


def passwordCorrect():
    app4.exec()
    pdisplay.setVisible(False)
    tp.setVisible(True)
    teacherPortal1()

def teacherPortal1():
    #tp1.show()
    #app1.exec()
    tp.backPB.clicked.connect(backLogin)

def passwordIncorrect():
    pdisplay.setVisible(False)
    fw.setVisible(True)

def backLogin():
    tp.setVisible(False)
    fw.setVisible(True)    

fp.student_button.clicked.connect(studentwin)

fp.teacher_button.clicked.connect(facultywin)
oImage=QImage("back.png")
sImage=oImage.scaled(QSize(939,939))
palette=QPalette()
palette.setBrush(QPalette.Window,QBrush(sImage))
fp.setPalette(palette)

fp.show()
app.exec()

