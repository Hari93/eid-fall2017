//////////////////*********************    README.txt **********************//////////////////////////

##################################  Author : Hari Shreenivash Madras Vanamamalai #####################

/////////////////////////////////// No Copyrights Provided ///////////////////////////////////////////

//////////////// Name of the Project : Measuring Temperature and Humidity Using Raspberry pi 3 ///////

######################################################################################################

*************************************** Installation/Setup Instructions: *****************************

Step1: Type uname -a to find the version of raspberry pi

Step2: Connect the temperature sensor and resistor in breadboard.

Step3: Make connections using wires from breadboard to raspberry pi

Step4: In my case, Vcc wire was connected to GPIO1(Pin 2) and the ground wire was connected to GPIO3(Pin 6) 
       and the output was connected to GPIO4(Pin 7)

Step5: Run the program using  python filename.py [sensor-type] [pin number]

Step6: If you are using a rewmote machine, use xrdp  or else use VNC viewer to access pi from  your laptop 

****************************************  Project Work ************************************************

Primary Requirements:

1. Printing Temperature and Humidity values on screen every time after request

2. Quitting the interface if the quit button is pressed

3. When the temperature sensor is disconnected, it prints out error in fetching data

4. Current Date and time are printed at the time of request

All basic primary requirements are met and everytime we press refresh button, the old value is cleared and new value is fetched from sensor

UI Design:

Created two tabs . One for temperature and the other one for humidity

Each tab has two buttons namely Refresh and Quit

The expected functionalities are the same and I have added color for buttons

*************************************** Project Additions **********************************************

1. Created progress bar for displaying the current temperature and humidity

2. Created  an alarm for high humidity and low temperature

3. The alarm is displayed with a warning message

*******************************************************************************************************
