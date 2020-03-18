from PyQt5 import QtWidgets,uic
import sys

app=QtWidgets.QApplication([])
dic=uic.loadUi('TeacherPortal1.ui')

def comboBox():
    tName=dic.comboBox1.currentText()
    #the above will return the value of the selected name in the drop down menu/Combo box
    tSlot=dic.comboBox2.currentText()
    #the above will get the time slot in string format

    #temporary labels to test the values
    dic.labelx.setText(tName)
    dic.labely.setText(tSlot)
    

    
dic.submitPB.clicked.connect(comboBox)
dic.show()
app.exec()
