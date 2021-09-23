import sys,os
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
import ShowDataFrame

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        ui = ShowDataFrame.Ui_MainWindow()
        ui.setupUi(self)
        ui.btn_open_file.clicked.connect(self.open_file)
        ui.btn_show.clicked.connect(self.show_data)

        # self.open_file()
        
        # self.show_data()
        


    def open_file(self):
        #fname = QFileDialog.getOpenFileName(self, "Open File","/home", "Data sheet (*.csv)")[0]
        fname = r"C:\Users\VY\Desktop\demo.csv"
        df = pd.read_csv(fname)
        self.numcolumn = len(df.columns)
        self.numrow = df.shape[0]
        self.all_data = df
        
    def show_data(self):
        # Modify table_widget
        self.table.setColumnCount(self.numcolumn)
        self.table.setRowCount(self.numrow)
        self.table.setHorizontalHeaderLabels(self.numcolumn)

        for i in range(self.numrow):
            for j in range(self.numcolumn):
                self.table.setItem(i, j, QTableWidgetItem(str(self.all_data[i, j])))
    #     # self.

app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
sys.exit(app.exec_())