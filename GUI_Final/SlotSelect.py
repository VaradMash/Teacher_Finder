from xlrd import *
import os as o
from tkinter import *
import VerifyLeave as v

def get_slot(name,slot_no,day):
    ename=name+'.xlsx'
    p=open_workbook(ename)
    s=p.sheet_by_index(0)
    x=slot_no+2
    y=day+1
    u=s.cell_value(x,y)
    ret=v.leaverec(name)
    if ret==True:
        return "Faculty available today",str(u)
    else:
        return "Faculty on leave today",str(u)


  
