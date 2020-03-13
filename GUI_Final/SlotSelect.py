from xlrd import *
import os as o
from tkinter import *

def get_slot(name,slot_no,day):
    name=name+'.xlsx'
    p=open_workbook(name)
    s=p.sheet_by_index(0)
    x=slot_no+2
    y=day+2
    v=s.cell_value(x,y)
    return str(v)


  
