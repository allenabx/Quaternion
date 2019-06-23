import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import  QtCore
from PyQt5.QtCore import  Qt
from PyQt5.uic import loadUi
from PyQt5.QtGui import QCursor
import subprocess

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi('widget.ui', self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(self.sizeHint())
        self.buttonClose.clicked.connect(self.close_window)
        self.buttonMax.clicked.connect(self.max_window)
        self.buttonMin.clicked.connect(self.min_window)
        self.buttonGen.clicked.connect(self.genarate)

    #鼠标拖动
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))


    def close_window(self):
        """
        关闭窗口
        """
        self.close()

    def min_window(self):
        """
        最小化窗口
        """
        self.showMinimized()

    def max_window(self):
        """
        最大化窗口
        """
        if self.isMaximized():
        	self.showNormal()
        else:
        	print("max")
        	self.showMaximized()
        	self.layout().setContentsMargins(0, 0, 0, 0)	

    def write_file(self,filename,content):
        with open(filename,'a+') as fw:
            fw.seek(0) # 移动文件指针
            fw.truncate() # 清空文件内容
            fw.write(str(content))
    # write_file('a','hello world') # 调用函数

    def genarate(self):
        text = self.plainTextEdit.toPlainText()
        self.write_file('D://dataStructure//408//Program.txt',text)
        # subprocess.Popen('.\Quant.exe',shell=True)
        subprocess.call('.\Quant.exe',shell = True)

        print("Genarated")
    #     setTextBrowser(self)

    # def setTextBrowser(self):
        f = open('D://dataStructure//408//Code.txt')
        Quant = f.read()
        self.textBrowser.setText(Quant)
        

    
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
