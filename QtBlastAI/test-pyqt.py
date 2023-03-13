import sys
from PyQt5.QtWidgets import * 
from PyQt5 import uic
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

form_class = uic.loadUiType("test.ui")[0]

class MyWindow(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.btnClicked)
        self.lineEdit.setText("")
        self.label.setText("")

        self.lineEdit.textChanged.connect(self.lineeditTextFunction)
        self.lineEdit.returnPressed.connect(self.printTextFunction)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.count = 0
        self.colCnt = 2
        self.rowCnt = 2
        self.lcdNumber.display(10.0)

        self.tableWidget.setRowCount(self.rowCnt)
        self.tableWidget.setColumnCount(self.colCnt)        

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout_4.addWidget(self.canvas)


    def lineeditTextFunction(self) :
        self.label.setText(self.lineEdit.text())

    def printTextFunction(self) :
        #self.lineedit이름.text()
        #Lineedit에 있는 글자를 가져오는 메서드
        print(self.lineEdit.text())

    def btnClicked(self):
        print("Button clicked")
        self.listWidget.insertItem(self.count,self.lineEdit.text())
        self.tableWidget.setItem(1,self.count,QTableWidgetItem(self.lineEdit.text()))
        self.lineEdit.setText("Button clicked")        
        self.count = self.count + 1
        self.lcdNumber.display(self.count)
        self.colCnt = self.colCnt + 1
        self.tableWidget.setColumnCount(self.colCnt)        
        self.doGraph1()

    def doGraph1(self):
        x = np.arange(0, 10, 0.5)
        y1 = np.sin(x)
        y2 = np.cos(x)
        
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.plot(x, y1, label="sin(x)")
        ax.plot(x, y2, label="cos(x)", linestyle="--")
        
        ax.set_xlabel("x")
        ax.set_xlabel("y")
        
        ax.set_title("sin & cos")
        ax.legend()
        
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    # myWindow.show()
    app.exec_()
