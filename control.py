from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import  QPushButton, QSizePolicy, QTextEdit
import re
import math

class ButtonOperation(QPushButton):
    def __init__(self,text,callback,fontSize=0):
        super().__init__()
        self.setText(str(text))
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        if (fontSize > 0):
            font = QFont()
            font.setPointSize(fontSize)
            self.setFont(font)
        self.clicked.connect(lambda : callback(str(text)))

#  fungsi controler dari class MathExecs gunakan untuk push number dan eksekusi operator
#  psuh number dan push opertor di sini langsung mengeksekusi sesuai operasi matematika

class MathExecs:
    def __init__(self):
        self.listNumber:str = ""
        self.operator = None
        self.text_edits: list[QTextEdit] = [] # ini buat nampung text edit
        
    def add_text_edit(self, widget: QTextEdit):
        self.text_edits.append(widget)

        
    # melakukan perulangan di semua widget yang ada di list 
    # text edit untuk mengubah text nya sesuai dengan list number
    # 
    def change_text_edit(self):
        for widget in self.text_edits:
            widget.setText(self.listNumber)
    def push_number(self, other):
        self.listNumber += other
        self.change_text_edit()

    def push_pangkat(self,_):
        if self.listNumber == "":
            return
        self.listNumber = str(int(self.listNumber) ** 2)
        self.change_text_edit()

    def push_pecahan(self,_):
        if self.listNumber == "":
            return
        self.listNumber = str(1 / int(self.listNumber))
        self.change_text_edit()

    def push_akar(self,_):
        if self.listNumber == "":
            return
        self.listNumber = str(math.sqrt(int(self.listNumber)))
        self.change_text_edit()
        

    def push_operator(self,operator):
        lastInput = self.listNumber[-1] if len(self.listNumber) > 0 else ""
        self.calculate(lastInput)
        
        if operator == "=":
            self.change_text_edit()
            return

        if lastInput in "+/*" and operator == "-":
            self.listNumber += operator
        elif lastInput not in "-+/*":
            self.listNumber += operator
            self.operator = operator
        self.change_text_edit()
        
    def calculate(self,lastInput):
        if (self.operator != None and lastInput not in "-+/*"):
            operasi = re.sub(r'\b0+(\d+)', r'\1',self.listNumber)
            self.listNumber = str(eval(operasi))
            self.operator = None
    def clearState(self,_):
        self.listNumber = ""
        self.operator = None
        self.change_text_edit()

    def __str__(self):
       return self.listNumber