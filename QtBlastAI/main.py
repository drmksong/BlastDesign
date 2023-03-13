import sys
sys.path.append('./Blast_AI/')
sys.path.append('./Rand_AI/')

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from random import *

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import numpy as np

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout


randAI = __import__('2_randAI')
ksns_eval = __import__('4_ksns_eval_cpu')

form_class = uic.loadUiType("main_rev1.ui")[0]

class Reg():
    def __init__(self):
        self.rng = np.random
        self.W = tf.Variable(self.rng.randn(), name='weight')
        self.b = tf.Variable(self.rng.randn(), name='bias')
        self.X = []
        self.Y = []
        self.learning_rate = 0.01
        self.train_step = 1001
        self.disp_step = 1000
        self.optim = tf.optimizers.SGD(self.learning_rate)

    def setXY(self,x,y):
        self.X = x
        self.Y = y
        
        print(self.W.numpy())
        print(self.b.numpy())
        print(self.X)
        print(self.Y)

    def line_reg(self,x):
        return self.W*x + self.b

    def mse(self, y_pred, y_true):
        return tf.reduce_sum(tf.pow(y_pred-y_true,2))/(2*y_pred.shape[0])

    def run_optim(self):
        with tf.GradientTape() as g:
            pred = self.line_reg(self.X)
            loss = self.mse(pred,self.Y)
        
        grad = g.gradient(loss,[self.W,self.b])
        self.optim.apply_gradients(zip(grad,[self.W,self.b]))

    def train(self,epoch):
        for step in range(1,self.train_step+1):
            self.run_optim()

            if step % self.disp_step == 0:
                pred = self.line_reg(self.X)
                loss = self.mse(pred,self.Y)
                print(f'epoch = {epoch}, step = {step}, loss =  {loss:3.3},W =  {self.W.numpy():3.3}, b =  {self.b.numpy():3.3}')
        return pred

class MyApp(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.progressBar.setValue(0)

        self.X = []
        self.Y = []

        self.reg = Reg()

        self.exp = 1 # 에멀전C 등
        self.det = 0 # 전자뇌관 등
        self.rot = 0 # 퇴적암, 변성암 등
        self.roc = 0 # 화강암, 편암 등     
        self.cen = 0 # V-Cut 등

        self.exp_dict = {
                        '모든 화약':0,
                        '에멀젼C':1, 
                        '정밀폭약':2 ,
                        '벌크에멀젼':3 ,
                        }

        self.det_dict = {
                        '모든 뇌관':0,    
                        '비전기' : 1,
                        '전기' : 2,
                        '전자' : 3
                        }

        self.rot_dict = {
                        '모든 암석분류':0,
                        '변성암' : 1,
                        '퇴적암' : 2,
                        '화성암' : 3
                        }

        self.roc_dict = {
                        '모든 암석':0,
                        '규장암': 1, 
                        '사암': 2, 
                        '석회암': 3, 
                        '섬록암'  : 4, 
                        '셰일': 5, 
                        '안산암': 6, 
                        '응회암': 7, 
                        '편마암'  : 8,  
                        '편암': 9, 
                        '화강반암': 10,
                        '화강암':11
                        }

        self.cen_dict = {
                        '모든 심발':0,
                        'Cylinder-cut' : 1,
                        'TBM 선굴착' : 2,
                        'V-CUT' : 3,
                        '라인 드릴링':4,
                        '분착식 다단발파':5,
                        '선대구경':6,
                        '수직구':7
                        }
 
        self.combo_set()

    def initUI(self):
        self.setupUi(self)
        self.show()

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout_3.addWidget(self.canvas)

        self.doGraph()

        self.actionSave.triggered.connect(self.save)
        self.actionExit.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.loadModel)
        self.pushButton.clicked.connect(self.loadModel)
        
        self.combo_exp.currentTextChanged.connect(self.exp_select)
        self.combo_det.currentTextChanged.connect(self.det_select)
        self.combo_rot.currentTextChanged.connect(self.rot_select)
        self.combo_roc.currentTextChanged.connect(self.roc_select)
        self.combo_cen.currentTextChanged.connect(self.cen_select)     

        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)   
        column_headers = ['50m', '100m', '150m', '200m']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        row_headers = ['0.02kine', '0.3kine', '0.5kine', '0.8kine', '1.0kine']
        self.tableWidget.setVerticalHeaderLabels(row_headers)

        for j in range(4):
            self.tableWidget.setColumnWidth(j,120)

        for j in range(4):
            for i in range(5):
                item = QTableWidgetItem(f'({i},{j})')
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                self.tableWidget.setItem(i,j,item)
        
        self.tableWidget.selectAll()

    def save(self):
        fname = QFileDialog.getSaveFileName(self, 'Save file', './', 'all files (*.*) ;; comma seprated files (.csv)')
        df = pd.DataFrame({'X':self.X,'Y':self.Y})
        df.to_csv(fname[0])
        self.fig.savefig(fname[0].split('.')[0]+'.png', format='png',dpi=300)

        try:
            file = fname[0].split('.')[0]+'_list.txt'
            list_widget = self.listWidget
            entries = '\n'.join(list_widget.item(ii).text() for ii in range(list_widget.count()))
            with open(file, 'w') as fout:
                fout.write(entries)
        except OSError as err:
            print(f"file {file} could not be written")

        self.exportToExcel(fname[0].split('.')[0]+'_tab.xls')
        print(f'save {fname[0]} selected')


    def exportToExcel(self,fname):
        columnHeaders = []
        rowHeaders = []

        for i in range(self.tableWidget.model().rowCount()):
            rowHeaders.append(self.tableWidget.verticalHeaderItem(i).text())

        # create column header list
        for j in range(self.tableWidget.model().columnCount()):
            columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=columnHeaders, index=rowHeaders)

        # create dataframe object recordset
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                df.at[rowHeaders[row], columnHeaders[col]] = self.tableWidget.item(row, col).text()

        df.to_excel(fname, index=True)
        print('Excel file exported')

    def exp_select(self):
        self.exp = self.exp_dict[self.combo_exp.currentText()]
        self.listWidget.insertItem(0,f' 화약 종류는 {self.combo_exp.currentText()}, {self.exp}')

    def det_select(self):
        self.det = self.det_dict[self.combo_det.currentText()]
        self.listWidget.insertItem(0,f' 뇌관 종류는 {self.combo_det.currentText()}, {self.det}')        

    def rot_select(self):
        self.rot = self.rot_dict[self.combo_rot.currentText()]
        self.listWidget.insertItem(0,f' 암석 분류는 {self.combo_rot.currentText()}, {self.rot}')

    def roc_select(self):
        self.roc = self.roc_dict[self.combo_roc.currentText()]
        self.listWidget.insertItem(0,f' 암석명 {self.combo_roc.currentText()}, {self.roc}')

    def cen_select(self):
        self.cen = self.cen_dict[self.combo_cen.currentText()]
        self.listWidget.insertItem(0,f' 심발은 {self.combo_cen.currentText()}, {self.cen}')

    def combo_set(self):

        self.exp = self.exp_dict[self.combo_exp.currentText()]
        self.det = self.det_dict[self.combo_det.currentText()]
        self.rot = self.rot_dict[self.combo_rot.currentText()]
        self.roc = self.roc_dict[self.combo_roc.currentText()]
        self.cen = self.cen_dict[self.combo_cen.currentText()]

        df = pd.read_csv('./openpit2.csv')

    # def save(self,x,y,tit):
    #     df = pd.DataFrame(columns=['SD','PPV'])
        
    #     pass
            
    def doGraph(self):
        x = np.arange(0, 10, 0.5)
        y1 = np.sin(x)
        
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.scatter(x, y1, label="sin(x)")
        
        ax.set_xlabel("Logarithmic Scale Distance (m/$\sqrt{kg}$)")
        ax.set_ylabel("Logarithmic PPV (cm/sec) ")
        
        ax.set_title("Evaluation of Peak Partical Velocity")
        ax.legend()
        
        self.canvas.draw()

    def loadModel(self):
        self.model = ksns_eval.load_model()
        self.scaler = ksns_eval.set_scaler()
        self.predict()

    def predict(self):
        exp = self.exp
        det = self.det
        rot = self.rot
        roc = self.roc
        cen = self.cen

        key_in = [exp,det,rot,roc,cen]

        print(f'key_in:{key_in}')
        
        ksns_eval.scaler = ksns_eval.set_scaler()
        
        K,n,s = ksns_eval.predict(key_in, self.model) # K is in log scale
        K = np.exp(K) # K is in original scale

        print(f' K:{K:3.3} n:{n:3.3} s:{s:3.3}')
        self.listWidget.insertItem(0,f' K:{K:3.3} n:{n:3.3}, s:{s:3.3}')


        seq = randAI.gen_seq([K,n,s],200)
        X = seq[:,0]
        Y = seq[:,1]
        
        self.X = X
        self.Y = Y

        logX = np.log(X)
        logY = np.log(Y)

        # clear listWidget and describe current selection    
        self.listWidget.clear()
        self.exp_select()
        self.det_select()
        self.rot_select()
        self.roc_select()
        self.cen_select()

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        
        ax.plot(X, Y, 'o', label="eval PPV")
        ax.set_yscale('log')
        ax.set_xscale('log')

        ax.set_xlabel("Logarithmic Scale Distance (m/$\sqrt{kg}$)")
        ax.set_ylabel("Logarithmic PPV (cm/sec) ")
        
        ax.set_title("Evaluation of Peak Partical Velocity")
        ax.legend()
        
        self.canvas.draw()
        self.canvas.flush_events()

        dist = [10, 50, 100, 200]
        ppv = [0.02, 0.3, 0.5, 0.8, 1.0]

        column_headers = list(map(lambda x: f'{x}m', dist))
        row_headers = list(map(lambda x: f'{x}kine', ppv))

        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.tableWidget.setVerticalHeaderLabels(row_headers)

        for j,d in enumerate(dist):
            item = QTableWidgetItem(f'{d:3}m')
            self.tableWidget.setItem(0,j,item)

        for i,w in enumerate(ppv):
            item = QTableWidgetItem(f'{w:3.3}m')
            self.tableWidget.setItem(i,0,item)


        for j,d in enumerate(dist):
            for i, v in enumerate(ppv):
                item = QTableWidgetItem(' ')
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                self.tableWidget.setItem(i,j,item)

        self.tableWidget.selectAll()

        # reg = Reg()
        self.reg.setXY(logX, logY)
        for i in range(50):
            self.progressBar.setValue((i+1)/50*100)
            self.fig.clear()
            ax = self.fig.add_subplot(111)

            ax.plot(X, Y, 'o', label="eval PPV")            
            ax.set_yscale('log')
            ax.set_xscale('log')
            ax.set_xlabel("Logarithmic Scale Distance (m/$\sqrt{kg}$)")
            ax.set_ylabel("Logarithmic PPV (cm/sec) ")
            
            ax.set_title("Evaluation of Peak Partical Velocity")\

            pred = self.reg.train(i)
            epred = np.exp(pred)
            ax.plot(X, epred, label="mean regression")

            delt_b = 1.96*s*np.sqrt(self.reg.W.numpy()*self.reg.W.numpy()+1)
            YY = pred + delt_b
            eYY = np.exp(YY)
            ax.plot(X,eYY, label='95% confidence regression', color='#008800')

            ax.legend(loc="upper right")

            K = np.exp(self.reg.b.numpy()+delt_b)
            n = (self.reg.W.numpy())
            
            ax.text(0.05,0.05,f'PPV = {K:7.4} ( D / $\sqrt{{W}}$ )$^{{{n:4.3}}}$ ',transform=ax.transAxes)
            
            # to prevent scientific tick label
            ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
            ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
            ax.ticklabel_format(useOffset=False, style='plain')

            self.canvas.draw()
            self.canvas.flush_events()
        
        self.listWidget.insertItem(0,f' K = {np.exp(self.reg.b.numpy()+delt_b)}')        
        self.listWidget.insertItem(0,f' n = {(self.reg.W.numpy())}')        

        print('95% confidence level plotted')

        n = self.reg.W.numpy()
        K = np.exp(self.reg.b.numpy()+delt_b) # of 95% confidence 


        for j,d in enumerate(dist):
            for i, v in enumerate(ppv):
                w =  np.exp(-2/n*np.log(v)+2/n*np.log(K)+2*np.log(d))     
                item = QTableWidgetItem(f'{w:3.3}kg')
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                self.tableWidget.setItem(i,j,item)

        self.tableWidget.selectAll()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())