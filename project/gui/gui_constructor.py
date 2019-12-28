from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import __main__ 

class Example(QWidget):
    
    def __init__(self, ticker_list):
        super().__init__()
        self.ticker_list = ticker_list
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('gui/icongui.png'))
            
        # Initialization
        self.selected_ticker = 'UNSELECTED'
        self.ticker_been_selected = 0
        self.strat1 = "1"
        self.strat2 = "1"
        self.strat3 = "1"
        
        #TEKST
        label_stock = QLabel("Select stock to analyze: ",self)
        label_stock.move(40,10)
    
    
        # Text Box #1 - Epochs
        label_e1 = QLabel("Epochs",self)
        label_e1.move(80,180)
        self.e1 = QLineEdit(self)
        self.e1.setText(str(__main__.ml_parameters['epochs']))
        self.e1.setValidator(QIntValidator())
        self.e1.setMaxLength(3)
        self.e1.setAlignment(Qt.AlignRight)
        self.e1.resize(100,25)
        self.e1.setFont(QFont("Arial",12))
        self.e1.textChanged.connect(lambda: self.text_box_changed(1))
        self.e1.move(60,200)
        
        # Text Box #2 - Epochs
        label_e2 = QLabel("Batch Size",self)
        label_e2.move(80,230)
        self.e2 = QLineEdit(self)
        self.e2.setText(str(__main__.ml_parameters['batch_size']))
        self.e2.setValidator(QIntValidator())
        self.e2.setMaxLength(3)
        self.e2.setAlignment(Qt.AlignRight)
        self.e2.resize(100,25)
        self.e2.setFont(QFont("Arial",12))
        self.e2.textChanged.connect(lambda: self.text_box_changed(2))
        self.e2.move(60,250)

        # Dropdown list  
        self.cb = QComboBox(self)
        for ticker in self.ticker_list:
            self.cb.addItems([ticker['name']])
        self.cb.currentIndexChanged.connect(self.dropdown_selection)
        self.cb.move(40,40)
    
        # Create a button in the window
        self.button = QPushButton('Run Neural Network', self)
        self.button.move(40,290)
        self.button.resize(150,25)
        self.button.clicked.connect(self.btn_on_click)  
    
        # Text
        label2 = QLabel("Wanted Strategies:",self)
        label2.move(425,50)
    
        # Checkbox #1
        self.ch_check = QCheckBox(self)
        self.ch_check.move(425,75)
        label2 = QLabel("Shorting Disallowed",self)
        label2.move(450,75)
        self.ch_check.toggle()
        self.ch_check.stateChanged.connect(lambda: self.state_changed(1))
    
        # Checkbox #2
        self.ch_check2 = QCheckBox(self)
        self.ch_check2.move(425,100)
        label3 = QLabel("Shorting Allowed",self)
        label3.move(450,100)
        self.ch_check2.toggle()
        self.ch_check2.stateChanged.connect(lambda: self.state_changed(2))
    
        # Vinduet i seg sjølv
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Alchemy2k")
        self.resize(600,400)
        self.show()
        
    def btn_on_click(self):
        stratstring = self.strat1 + self.strat2 + self.strat3
        
        # Exception case if the user has not selected a stock
        if(self.ticker_been_selected == 0):
            self.selected_ticker = self.ticker_list[0]['paper']
            __main__.run_algorithm_on_stock(self.selected_ticker, stratstring)
        else:             
            __main__.run_algorithm_on_stock(self.selected_ticker, stratstring)
                
    def dropdown_selection(self,i):
        self.selected_ticker = self.ticker_list[i]['paper']
        self.ticker_been_selected = 1
        
    def text_box_changed(self, *args):
        for arg in args:
            if arg == 1:
                __main__.ml_parameters['epochs'] = int(self.e1.text())
            if arg == 2:
                __main__.ml_parameters['batch_size'] = int(self.e2.text())       
    
    def state_changed(self,*args):
        for arg in args:
            if arg == 1:
                if self.ch_check.isChecked():
                    self.strat1 = "1"
                else:
                    self.strat1 = "0"
            elif arg == 2:
                if self.ch_check2.isChecked():
                    self.strat2 = "1"
                else:
                    self.strat2 = "0"
            elif arg == 3:
                if self.ch_check3.isChecked():
                    self.strat3 = "1"
                else:
                    self.strat3 = "0"
            else:
                return