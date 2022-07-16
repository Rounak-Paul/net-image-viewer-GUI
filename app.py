from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils
from cv2 import waitKey
import numpy as np

#Rounak's Python Module
import netmod.netmod.imageprocessing as ip

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("../2.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setLineWidth(2)
        self.label_6.setMidLineWidth(2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sRed = QtWidgets.QSlider(self.centralwidget)
        self.sRed.setMaximum(255)
        self.sRed.setSliderPosition(255)
        self.sRed.setOrientation(QtCore.Qt.Horizontal)
        self.sRed.setObjectName("sRed")
        self.verticalLayout_2.addWidget(self.sRed)
        self.sGreen = QtWidgets.QSlider(self.centralwidget)
        self.sGreen.setMaximum(255)
        self.sGreen.setSliderPosition(255)
        self.sGreen.setOrientation(QtCore.Qt.Horizontal)
        self.sGreen.setObjectName("sGreen")
        self.verticalLayout_2.addWidget(self.sGreen)
        self.sBlue = QtWidgets.QSlider(self.centralwidget)
        self.sBlue.setMaximum(255)
        self.sBlue.setSliderPosition(255)
        self.sBlue.setOrientation(QtCore.Qt.Horizontal)
        self.sBlue.setObjectName("sBlue")
        self.verticalLayout_2.addWidget(self.sBlue)
        self.sGamma = QtWidgets.QSlider(self.centralwidget)
        self.sGamma.setMaximum(10)
        self.sGamma.setSliderPosition(1)
        self.sGamma.setOrientation(QtCore.Qt.Horizontal)
        self.sGamma.setObjectName("sGamma")
        self.verticalLayout_2.addWidget(self.sGamma)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(125, 457))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bGray = QtWidgets.QPushButton(self.widget)
        self.bGray.setObjectName("bGray")
        self.verticalLayout_3.addWidget(self.bGray)
        self.bEdge = QtWidgets.QPushButton(self.widget)
        self.bEdge.setObjectName("bEdge")
        self.verticalLayout_3.addWidget(self.bEdge)
        self.bSharp = QtWidgets.QPushButton(self.widget)
        self.bSharp.setObjectName("bSharp")
        self.verticalLayout_3.addWidget(self.bSharp)
        self.bSmooth = QtWidgets.QPushButton(self.widget)
        self.bSmooth.setObjectName("bSmooth")
        self.verticalLayout_3.addWidget(self.bSmooth)
        self.bHistEQ = QtWidgets.QPushButton(self.widget)
        self.bHistEQ.setObjectName("bHistEQ")
        self.verticalLayout_3.addWidget(self.bHistEQ)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.verticalLayout_5.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setMinimumSize(QtCore.QSize(0, 0))
        self.widget1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        self.bSave = QtWidgets.QPushButton(self.widget1)
        self.bSave.setObjectName("bSave")
        self.gridLayout_3.addWidget(self.bSave, 0, 1, 1, 1)
        self.bApply = QtWidgets.QPushButton(self.widget1)
        self.bApply.setObjectName("bApply")
        self.gridLayout_3.addWidget(self.bApply, 0, 2, 1, 1)
        self.bOpen = QtWidgets.QPushButton(self.widget1)
        self.bOpen.setObjectName("bOpen")
        self.gridLayout_3.addWidget(self.bOpen, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.widget1, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        #controller
        self.retranslateUi(MainWindow)
        self.bOpen.clicked.connect(self.loadImage)
        self.bApply.clicked.connect(self.apply)
        self.bSave.clicked.connect(self.savePhoto)
        self.bGray.clicked.connect(self.gray)
        self.bSharp.clicked.connect(self.sharp)
        self.bSmooth.clicked.connect(self.smooth)
        self.bEdge.clicked.connect(self.edge)
        self.bHistEQ.clicked.connect(self.histEQ)
        self.sRed.valueChanged['int'].connect(self.redValue)
        self.sGreen.valueChanged['int'].connect(self.greenValue)
        self.sBlue.valueChanged['int'].connect(self.blueValue)
        self.sGamma.valueChanged['int'].connect(self.gammaValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




        #variables
        self.filename = None
        self.tmp = None
        
        #setting max rgb value for sliders
        self.red_value_now = 255
        self.green_value_now = 255
        self.blue_value_now = 255
        self.gamma_value_now = 1

    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)

    #method to display image in the GUI
    def setPhoto(self,image):
        try:
            self.tmp = image
            image = imutils.resize(image,width=640)
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))
        except: print('error displaying photo')

    #change image to modified image for multiple modifications
    def apply(self):
        try: self.image = self.tmp
        except: return

    def savePhoto(self):
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        
        cv2.imwrite(filename,self.tmp)
        print('Image saved as:',self.filename)

    def gray(self):
        try:
            self.setPhoto(ip.gray(self.image))
        except: 
            return

    def sharp(self):
        try:
            self.setPhoto(ip.sharp(self.image))
        except:
            return

    def smooth(self):
        try:
            self.setPhoto(ip.smooth(self.image))
        except:
            return

    def edge(self):
        try:
            self.setPhoto(ip.edge(self.image))
        except:
            return

    def histEQ(self):
        try:
            self.setPhoto(ip.histogramEqualization(self.image))
        except:
            return
    
    #get slider value
    def redValue(self,value):
        self.red_value_now = float(value)
        self.updateRGB()
    def greenValue(self,value):
        self.green_value_now = float(value)
        self.updateRGB()
    def blueValue(self,value):
        self.blue_value_now = float(value)
        self.updateRGB()
    def gammaValue(self,value):
        self.gamma_value_now = float(value)
        self.updateGamma()
    

# update window on slider change
    def updateRGB(self):
        # gamma = self.gamma_value_now
        rgb = np.array([self.blue_value_now,self.green_value_now,self.red_value_now])
        # print(rgb)
        try:
            # img = ip.powerlaw(self.image,self.gamma_value_now)
            img = ip.colorFilter(self.image,rgb)
            
            self.setPhoto(img)

            
        except:
            print('error:unable to update RGB sliders')

# update on gamma change
    def updateGamma(self):
        gamma = self.gamma_value_now
        print(gamma)
        try:
            img = ip.powerlaw(self.image,gamma)
            self.setPhoto(img)
            print(img)
        except:
            return











    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Net Image Viewer"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Designed &amp; </p><p>Developed by:</p><p><span style=\" font-weight:600;\">MAKAUT AI LAB</span></p><p><a href=\"www.net-work.in\"><span style=\" text-decoration: underline; color:#0000ff;\">www.net-work.in</span></a></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "RED"))
        self.label_3.setText(_translate("MainWindow", "GREEN"))
        self.label_4.setText(_translate("MainWindow", "BLUE"))
        self.label_5.setText(_translate("MainWindow", "GAMMA"))
        self.bGray.setText(_translate("MainWindow", "GRAY"))
        self.bEdge.setText(_translate("MainWindow", "EDGE"))
        self.bSharp.setText(_translate("MainWindow", "SHARP"))
        self.bSmooth.setText(_translate("MainWindow", "SMOOTH"))
        self.bHistEQ.setText(_translate("MainWindow", "HIST EQ"))
        self.bSave.setText(_translate("MainWindow", "SAVE"))
        self.bApply.setText(_translate("MainWindow", "APPLY"))
        self.bOpen.setText(_translate("MainWindow", "OPEN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
