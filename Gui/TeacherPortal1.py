from PyQt5 import QtWidgets,uic


app=QtWidgets.QApplication([])
dic=uic.loadUi('sample.ui')

def fun():
    user=dic.lineEdit.text()
    pass1='dc'
    pass2=dic.lineEdit_2.text()
    
    if pass1==pass2:
        dic.lineEdit_3.setText('Password is ok')
    else:
         dic.lineEdit_3.setText('Password incorrect')
        

dic.pushButton.clicked.connect(fun)
dic.show()
app.exec()
