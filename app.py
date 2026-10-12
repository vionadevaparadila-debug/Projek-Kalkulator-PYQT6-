import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget,
    QTabWidget,
    QMainWindow, 
    QVBoxLayout,
    QHBoxLayout, 
    QLineEdit, 
    QGridLayout,
    QSizePolicy,
)
from PyQt6.QtGui import QAction
from control import ButtonOperation,MathExecs

font_size = 20
class GirdCalc(QWidget):
    def __init__(self,controller : MathExecs):
        super().__init__()
        input = QLineEdit()
        # memanggil variabel input
        controller.add_text_edit(input)
        input.setStyleSheet("width: 100%; height: 50px; qproperty-alignment: 'AlignRight'; font-size: 30px;")
        input.setReadOnly(True)
        # grid Layout
        grid = QGridLayout()
        input.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        grid.addWidget(input, 0, 0, 1, 4)
        grid.addWidget(ButtonOperation("C",controller.clearState,font_size),1,0)
        grid.addWidget(ButtonOperation("7",controller.push_number,font_size),2,0)
        grid.addWidget(ButtonOperation("3",controller.push_number,font_size),3,0)
        grid.addWidget(ButtonOperation("0",controller.push_number,font_size),4,0)
        grid.addWidget(ButtonOperation(".",controller.push_number,font_size),5,0)
        grid.addWidget(ButtonOperation("x²",controller.push_pangkat,font_size),1,1)
        grid.addWidget(ButtonOperation("8",controller.push_number,font_size),2,1)
        grid.addWidget(ButtonOperation("4",controller.push_number,font_size),3,1)
        grid.addWidget(ButtonOperation("1",controller.push_number,font_size),4,1)
        grid.addWidget(ButtonOperation("1/x ",controller.push_pecahan,font_size),1,2)
        grid.addWidget(ButtonOperation("9",controller.push_number,font_size),2,2)
        grid.addWidget(ButtonOperation("6",controller.push_number,font_size),3,2)
        grid.addWidget(ButtonOperation("2",controller.push_number,font_size),4,2)
        grid.addWidget(ButtonOperation("=",controller.push_operator,font_size),5,1,1,2)
        grid.addWidget(ButtonOperation("√x",controller.push_akar,font_size),1,3)
        grid.addWidget(ButtonOperation("/",controller.push_operator,font_size),2,3)
        grid.addWidget(ButtonOperation("*",controller.push_operator,font_size),3,3)
        grid.addWidget(ButtonOperation("-",controller.push_operator,font_size),4,3)
        grid.addWidget(ButtonOperation("+",controller.push_operator ,font_size),5,3)
        self.setLayout(grid)


class VboxHbox(QWidget):
    def __init__(self,controller : MathExecs):
        super().__init__()
        
        input = QLineEdit()
        # input.setFontPointSize(font_size)
        controller.add_text_edit(input)
        input.setStyleSheet("width: 100%; height: 50px; qproperty-alignment: 'AlignRight'; font-size: 30px;")
        input.setReadOnly(True)

        # layout Vertikal 
        layout = QVBoxLayout()
        layout.addWidget(input)

        #baris 1 
        row1 = QHBoxLayout()
        row1.addWidget(ButtonOperation("C",controller.clearState,font_size))
        row1.addWidget(ButtonOperation("x²",controller.push_pangkat,font_size))
        row1.addWidget(ButtonOperation("1/x",controller.push_pecahan,font_size))
        row1.addWidget(ButtonOperation("√x",controller.push_akar,font_size))

        #baris 2 
        row2 = QHBoxLayout()
        row2.addWidget(ButtonOperation("7",controller.push_number,font_size))
        row2.addWidget(ButtonOperation("8",controller.push_number,font_size))
        row2.addWidget(ButtonOperation("9",controller.push_number,font_size))
        row2.addWidget(ButtonOperation("/",controller.push_operator,font_size))

        #baris 3 
        row3= QHBoxLayout()
        row3.addWidget(ButtonOperation("3",controller.push_number,font_size))
        row3.addWidget(ButtonOperation("4",controller.push_number,font_size))
        row3.addWidget(ButtonOperation("6",controller.push_number,font_size))
        row3.addWidget(ButtonOperation("*",controller.push_operator,font_size))

        #baris 4 
        row4 = QHBoxLayout()
        row4.addWidget(ButtonOperation("0",controller.push_number,font_size))
        row4.addWidget(ButtonOperation("1",controller.push_number,font_size))
        row4.addWidget(ButtonOperation("2",controller.push_number,font_size))
        row4.addWidget(ButtonOperation("-",controller.push_operator,font_size))

        # baris 5
        row5 = QHBoxLayout()
        row5.addWidget(ButtonOperation(".",controller.push_number,font_size))
        # row5.addWidget(ButtonOperation("0",controller.push_number,font_size))
        row5.addWidget(ButtonOperation("=",controller.push_operator,font_size))
        row5.addWidget(ButtonOperation("+",controller.push_operator,font_size))

        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addLayout(row3)
        layout.addLayout(row4)
        layout.addLayout(row5)
        self.setLayout(layout)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KALKULATOR KELOMPOK 1")
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        controller = MathExecs()
        tabs.setMovable(True)       
        grid_clas = GirdCalc(controller)
        tabs.addTab(grid_clas,"Gird")

        vbox = VboxHbox(controller)
        tabs.addTab(vbox,"vbox")

        def GenerateAction(text,callback,operator=""):           
            action = QAction(f"&{text}",self)
            action.triggered.connect(lambda : callback(str(operator)))
            return action
        operasi_menu = self.menuBar()
        menu = operasi_menu.addMenu("&Operasi")
        
        menu.addAction(GenerateAction("Pangkat",controller.push_pangkat))
        menu.addAction(GenerateAction("Akar",controller.push_akar))
        menu.addAction(GenerateAction("Pecahan",controller.push_pecahan))
        menu.addAction(GenerateAction("Kali",controller.push_operator,"*"))
        menu.addAction(GenerateAction("Bagi",controller.push_operator,"/"))
        menu.addAction(GenerateAction("Pengurangan",controller.push_operator,"-"))
        menu.addAction(GenerateAction("Penjumlahan",controller.push_operator,"+"))
        
        self.setCentralWidget(tabs)

        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
