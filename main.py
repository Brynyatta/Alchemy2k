# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 00:02:50 2018

@author: Eier
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from predictor import predict
from data_retriever import ticker_list_retriever
import sys

strat1,strat2,strat3 = "1","1","1"


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('gui/icongui.png'))
        self.initUI()

    def initUI(self):
        # Initialization
        self.selected_ticker = 'UNSELECTED'
        self.ticker_been_selected = 0
        self.strat1 = "1"
        self.strat2 = "1"
        self.strat3 = "1"
        
        # Retrieve the current list of tickers:
        dataframe_tickers = ticker_list_retriever()
        self.ticker_list = dataframe_tickers.to_dict(orient='records')
        
        #TEKST
        label1 = QLabel("Select stock to analyze: ",self)
        label1.move(40,10)

        # Dropdown list
        
        self.cb = QComboBox(self)
        for ticker in self.ticker_list:
            self.cb.addItems([ticker['name']])
        self.cb.currentIndexChanged.connect(self.dropdown_selection)
        self.cb.move(40,40)

        # Create a button in the window
        self.button = QPushButton('Run Neural Network', self)
        self.button.move(40,95)
        self.button.resize(150,25)
        # Connect button to function on_click
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
        self.resize(600,500)
        self.show()
    def dropdown_selection(self,i):
        self.selected_ticker = self.ticker_list[i]['paper']
        self.ticker_been_selected = 1
    def btn_on_click(self):
        stratstring = self.strat1 + self.strat2 + self.strat3
        
        # Exception case if the user has not selected a stock
        if(self.ticker_been_selected == 0):
            self.selected_ticker = self.ticker_list[0]['paper']
            
        predict(self.selected_ticker,stratstring)
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
            

if __name__ == '__main__':    
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())