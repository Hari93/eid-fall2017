#!/usr/bin/python

##################************* CODE FOR TEMPERATURE AND HUMIDITY SENSOR *****************######################

##################************** AUTHOR : HARI SHREENIVASH MADRAS VANAMAMALAI *************######################

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import Adafruit_DHT
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import datetime
import time


####### Creating Sensor arguments  ##########
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

##### Defining sensor type and pin number at run time
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]

###### Exiting from application########
else:
    sys.exit(1)

####### Defining Tab  Function
def Tab():
    ##### Defining global variables for the function ############
    global t3,t4,p1,p2
    ##### Creating an object for the application ################
    app = QApplication(sys.argv)
    ####### Declaring Tabs ########################################
    tabs = QtGui.QTabWidget()
    tab1 = QtGui.QWidget()
    tab2 = QtGui.QWidget()
    tabs.resize (500, 500)
    ####### Setting a Window Title ################################
    tabs.setWindowTitle("Temperature and Humidity")
    ######  Creating Vertical Box layout for tab1  ################
    vBoxlayout = QtGui.QVBoxLayout()
    tab1.setLayout(vBoxlayout)
    ####### Creating Vertical Box Layout for tab2  ################
    vBoxlayout = QtGui.QVBoxLayout()
    tab2.setLayout(vBoxlayout)
    ######## Adding names for tab1 and tab2 ########################
    tabs.addTab(tab1,"Temperature")
    tabs.addTab(tab2,"Humidity")
    #######   Creating Labels for Tabs and defining size ############
    t3 = QLabel(tab1)
    t3.move(150,150)
    t3.resize(250,60)
    t4 = QLabel(tab2)
    t4.move(150,150)
    t4.resize(250,60)


    ################### Creating buttons for tab1####################
    button1 = QPushButton(tab1)
    button2 = QPushButton(tab1)
    ################### Names of button1   #############################
    button1.setText("Refresh")
    button1.move(200,200)
    ################### Setting color for the buttons ################
    button1.setStyleSheet('background-color : Yellow')
    ##################  Name of Button2 #############################
    button2.setText("Quit")
    button2.move(200,250)
    button2.setStyleSheet('background-color :  Red')
    ################ Creating buttons for Tab2 ########################
    b1 = QPushButton(tab2)
    b2 = QPushButton(tab2)
    b1.setText("Refresh")
    b1.move(200,200)
    b1.setStyleSheet('background-color : Yellow')

    b2.setText("Quit")
    b2.move(200,250)
    b2.setStyleSheet('background-color : Red')
    ################ Defining one progress bar for each tab ###########
    p1 = QtGui.QProgressBar(tab1)
    p2 = QtGui.QProgressBar(tab2)
    ################  Defining size for each progress bar #####################
    p1.setGeometry(200,80,250,20)
    p2.setGeometry(200,80,250,20)



    ################## Defining functions for these events ############
    button1.clicked.connect(button1_clicked)
    button2.clicked.connect(button2_clicked)
    b1.clicked.connect(b1_clicked)
    b2.clicked.connect(b2_clicked)

    tabs.show()
    sys.exit(app.exec_())

###############  Action performed when each function is called ##########
def button1_clicked():
    humidity, temperature1 = Adafruit_DHT.read_retry(22, 4)
    print(" Refresh Temperature Button is pressed")
    try:
       w = QtGui.QWidget()
       if temperature1 == 25:
         ##############  Setting value for progress bar 1 as temperature #############################
            p1.setValue(temperature1)
            QMessageBox.information(w, "Message",  "Room temperature")
            w.show()
            p1.show()
       elif str(temperature1) ==  None:
            ######## Raising Exception to handle when temp is none #####
            raise Exception
       elif temperature1 < 22:
            ######  Displaying Warning Box for Low Temperatures and setting an alarm #########
            p1.setValue(temperature1)
            QMessageBox.warning(w, "Message", "Alarm for low temperature is activated") 
            w.show()
            p1.show()
       else:
            p1.setValue(temperature1)
            QMessageBox.information(w, "Message", "Normal temperature")
            w.show()
            p1.show()
     ######## Setting Date Time and printing it ################
       t3.setText(str(datetime.datetime.now()))

    except Exception as e:
        ####### Exception Handling ##################
        print(" Error in reading temperature and pressure")
        w1 = QtGui.QWidget()
        p1.setValue(0)
        QMessageBox.information(w1, "Message", "ERROR in Fetching Data")
        w1.show()
        ######### Display Date Time #############
        t3.setText(str(datetime.datetime.now()))
########Defining action event when quit button is pressed #######
def button2_clicked():
    print("Quit button is pressed")
    sys.exit(1)

######## Defining action event when refresh humidity button is pressed ########
def b1_clicked():
    humidity1, temperature = Adafruit_DHT.read_retry(22, 4)
    print(" Refresh Humidity Button is pressed")
    try:
        ##### Creating Window ########
         w = QtGui.QWidget()
         if  humidity1 == 35:
             ###### Setting progress bar for  Humidity  #######
             p2.setValue(humidity1)
             QMessageBox.information(w, "Message",  "Room Humidity")
             p2.show()
         elif str(humidity1) == None:
             raise Exception
         elif humidity1 > 35:
             p2.setValue(humidity1)
             ####### Displaying warning box for high humidity ######
             QMessageBox.warning(w, "Message", "Alarm for high humidity is activated")
             p2.show()
         else:
             p2.setValue(humidity1)
             QMessageBox.information(w, "Message", "Normal Humidity")
             p2.show()
         w.show()
        ###### Displaying Date Time ######
         t4.setText(str(datetime.datetime.now()))
    except Exception as e:
        print(" Error in reading Humidity")
        w1 = QtGui.QWidget()
        p2.setValue(0)
        QMessageBox.information(w1, "Message", "ERROR in Fetching Data")
        w1.show()
        t4.setText(str(datetime.datetime.now()))

######### Defining action2 when button2 is clicked ##################
def b2_clicked():
    print("Quit button is pressed")
    sys.exit(1)

###Defining main program ####
def main():

    Tab()

### Executing main ###
if __name__ == '__main__':
    main()
