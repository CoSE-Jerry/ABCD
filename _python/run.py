import sys
import socket
import os

# This gets the Qt stuff
import PyQt5
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *

PORT = 5560

UpperStat = [0] * 10
LowerStat = [0] * 10
UpperConn = [1] * 10
LowerConn = [1] * 10

UpperRunning = [0] * 10
LowerRunning = [0] * 10

interval=0
duration=0
loadinterval=0
loadduration=0
loadtotal=0
current=0
running=False
title=""
loadtitle=""
email="temp"
loademail=""


# This is our window from QtCreator
import ABCD_UI


class ConnectionUpdate(QThread):
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        global loadtitle, loadinterval, loadduration,loademail,current,loadtotal
        found=False
        for x in range(0, 9):
            if(LowerStat[x]==1 and found ==False):
                HOST="192.168.1.10"+str(x)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((HOST,PORT))
                    s.send(str.encode("CURR"))
                    reply = s.recv(1024)
                    reply = reply.decode('utf-8')
                    dataMessage = reply.split('-', 5)
                    print(reply)
                    
                    loadtitle = dataMessage[0]
                    loadinterval = dataMessage[1]
                    loadduration = dataMessage[2]
                    email = dataMessage[3]
                    current = int(dataMessage[4])
                    print(current)
                    loadtotal = int(dataMessage[5])
                    print(loadtotal)
                    if(len(loadtotal)>0):
                        found=True
                    s.close()
                except:
                    print("nopey")
                    
            if(UpperStat[x]==1 and found ==False):
                HOST="192.168.1.20"+str(x)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((HOST,PORT))
                    s.send(str.encode("CURR"))
                    reply = s.recv(1024)
                    reply = reply.decode('utf-8')
                    dataMessage = reply.split('-', 5)
                    print(reply)
                    
                    loadtitle = dataMessage[0]
                    loadinterval = dataMessage[1]
                    loadduration = dataMessage[2]
                    email = dataMessage[3]
                    current = int(dataMessage[4])
                    print(current)
                    loadtotal = int(dataMessage[5])
                    print(loadtotal)
                    if(len(loadtotal)>0):
                        found=True
                    s.close()
                except:
                    print("nopey")
            

class StartImaging(QThread):
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):

        for x in range(0, 9):
            if(LowerRunning[x]==1):
                HOST="192.168.1.10"+str(x)
                print(HOST)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((HOST,PORT))
                    cmd = "CAM-"+title+"-"+str(interval)+"-"+str(duration)+"-"+email
                    s.send(str.encode(cmd))
                    reply = s.recv(1024)
                    print (reply.decode('utf-8'))
                    s.close()
                except:
                    print("nope")
                    
            if(UpperRunning[x]==1):
                HOST="192.168.1.20"+str(x)
                print(HOST)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((HOST,PORT))
                    cmd = "CAM-"+title+"-"+str(interval)+"-"+str(duration)+"-"+email
                    s.send(str.encode(cmd))
                    reply = s.recv(1024)
                    print (reply.decode('utf-8'))
                    s.close()
                except:
                    print("nope")

class Livefeed(QThread):
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):

        for x in range(0, 9):
            if(LowerRunning[x]==1):
                HOST="192.168.1.10"+str(x)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((HOST,PORT))
                    cmd = "LIVE"
                    s.send(str.encode(cmd))
                    s.close()
                except:
                    print("nope")
                    
            if(UpperRunning[x]==1):
                HOST="192.168.1.20"+str(x)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((HOST,PORT))
                    cmd = "LIVE"
                    s.send(str.encode(cmd))
                    s.close()
                except:
                    print("nope")
        sleep(60)

            


class QuitImaging(QThread):
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):

        for x in range(0, 9):
            if(LowerRunning[x]==1):
                HOST="192.168.1.10"+str(x)
                print(HOST)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((HOST,PORT))
                    cmd = "QUIT"
                    s.send(str.encode(cmd))
                    s.close()
                except:
                    print("nope")
                    
            if(UpperRunning[x]==1):
                HOST="192.168.1.20"+str(x)
                print(HOST)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((HOST,PORT))
                    cmd = "QUIT"
                    s.send(str.encode(cmd))
                    s.close()
                except:
                    print("nope")

class PingConnection(QThread):
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        global LowerConn,Upperconn,UpperRunning,LowerRunning
        for x in range(0, 9):
            if(LowerStat[x]==1):
                HOST="192.168.1.10"+str(x)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((HOST,PORT))
                    s.close()
                    LowerRunning[x]=1
                    print("connection successful" + HOST)
                except:
                    LowerConn[x]=0
                    print("connection failed" + HOST)
        for x in range(0, 9):
            if(UpperStat[x]==1):
                HOST="192.168.1.20"+str(x)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((HOST,PORT))
                    s.close()
                    UpperRunning[x]=1
                    print("connection successful" + HOST)
                except:
                    UpperConn[x]=0
                    print("connection failed" + HOST)
        
class PingLower(QThread):
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        global LowerStat, LowerReady
        LowerStat = [0] * 10
        for x in range(0, 9):
            hostname = "192.168.1.10" + str(x)
            response = os.system("fping -c1 -t50 " + hostname)
            if response == 0:
                LowerStat[x]=1

class PingUpper(QThread):
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        global UpperStat, UpperReady
        UpperStat = [0] * 10
        for x in range(0, 9):
            hostname = "192.168.1.20" + str(x)
            response = os.system("fping -c1 -t50 " + hostname)
            if response == 0:
                UpperStat[x]=1

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, ABCD_UI.Ui_Demo):
# access variables inside of the UI's file
    def IST_Edit(self):
        global title
        title = self.IST_Editor.text()
        print(title)
        
    def IST_Change(self):
        
        self.ICI_spinBox.setEnabled(True)
        if(len(self.IST_Editor.text())==0):
            self.ICI_spinBox.setEnabled(False)
            self.ISD_spinBox.setEnabled(False)
            self.Start_Imaging.setEnabled(False)

    def ICI_Change(self):
        global interval, total
        interval = self.ICI_spinBox.value()
        self.ISD_spinBox.setEnabled(True)
        if(interval == 0):
            self.ISD_spinBox.setEnabled(False)
        if(interval!= 0):
            total = int(duration/interval)
            if(total>0 and len(email)!=0):
                self.Start_Imaging.setEnabled(True)
            else:
                self.Start_Imaging.setEnabled(False)
                
    def ISD_Change(self):
        global duration, total
        duration = self.ISD_spinBox.value()
        if(interval!= 0):
            total = int(duration/interval)
            if(total>0 and len(email)!=0):
                self.Start_Imaging.setEnabled(True)
            else:
                self.Start_Imaging.setEnabled(False)

    def Update(self):
        self.Update_Status.setText("Updating Status...")
        self.Update_Status.setEnabled(False)
        self.Terminate_Imaging.setEnabled(False)
        self.LowerStat_Thread = PingLower()
        self.LowerStat_Thread.start()
        self.UpperStat_Thread = PingUpper()
        self.UpperStat_Thread.start()

        self.LowerStat_Thread.finished.connect(lambda: self.UpdateLower())
        self.UpperStat_Thread.finished.connect(lambda: self.UpdateUpper())
        

    def ConnectUpdate(self):
        try:
            self.Connection_Thread = ConnectionUpdate()
            self.Connection_Thread.start()
            self.Connection_Thread.finished.connect(lambda: self.ConnectionTest())
        except:
            print("nope")
            
    def ConnectionTest(self):
        self.Ping_Connection_Thread = PingConnection()
        self.Ping_Connection_Thread.start()
        self.Ping_Connection_Thread.finished.connect(lambda: self.ConnectionUIUpdate())
     
    def UpdateLower(self):
        for x in range(0, 9):
            if(LowerStat[x]==1):
                cmd1 = "self.Unit_%d_Label.setEnabled(True)"%x
                cmd2 = "self.Unit_%d_Label.setPixmap(QtGui.QPixmap(\"../_images/Green_button.png\"))"%x
                exec(cmd1)
                exec(cmd2)
            else:
                cmd1 = "self.Unit_%d_Label.setEnabled(True)"%x
                cmd2 = "self.Unit_%d_Label.setPixmap(QtGui.QPixmap(\"../_images/stop-red.png\"))"%x
                exec(cmd1)
                exec(cmd2)
            

    def UpdateUpper(self):
        for x in range(0, 9):
            xmod=x+10
            if(UpperStat[x]==1):
                cmd1 = "self.Unit_%d_Label.setEnabled(True)"%xmod
                cmd2 = "self.Unit_%d_Label.setPixmap(QtGui.QPixmap(\"../_images/Green_button.png\"))"%xmod
                exec(cmd1)
                exec(cmd2)
            else:
                cmd1 = "self.Unit_%d_Label.setEnabled(True)"%xmod
                cmd2 = "self.Unit_%d_Label.setPixmap(QtGui.QPixmap(\"../_images/stop-red.png\"))"%xmod
                exec(cmd1)
                exec(cmd2)
        self.Update_Status.setText("Update Status")
        self.Update_Status.setEnabled(True)
        if(running==False):
            self.IST_Editor.setEnabled(True)
        self.ConnectUpdate()

        if(running):
            self.Start_Imaging.setEnabled(False)
            self.Terminate_Imaging.setEnabled(True)
        else:
            self.Start_Imaging.setEnabled(True)
            self.Terminate_Imaging.setEnabled(False)

    def ConnectionUIUpdate(self):
        global UpperConn,LowerConn
        for x in range(0, 9):
            if(LowerConn[x]==0):
                cmd = "self.Unit_%d_Label.setEnabled(False)"%x
                exec(cmd)
        for x in range(0, 9):
            xmod=x+10
            if(UpperConn[x]==0):
                cmd = "self.Unit_%d_Label.setEnabled(False)"%xmod
                exec(cmd)
        if(running):
            self.Start_Live.setEnabled(False)
        else:
            self.Start_Live.setEnabled(True)
        UpperConn = [1] * 10
        LowerConn = [1] * 10
        self.IST_Editor.setText(loadtitle)
        self.ICI_spinBox.setValue(int(loadinterval))
        self.ISD_spinBox.setValue(int(loadduration))

        self.Image_Bar.setMaximum(current+1)
        self.Image_Bar.setValue(loadtotal)

        if(current==loadtotal):
            running=False
            self.StatusBar.setText("System Status: Idle...")
        elif(current-1==loadtotal):
            running=False
            self.StatusBar.setText("System Status: Imaging Complete")
        else:
            running=True
            self.StatusBar.setText("System Status: Imaging... %d/%d"%(loadtotal,current))
        if(running):
            self.Start_Imaging.setEnabled(False)
            self.Terminate_Imaging.setEnabled(True)
            self.IST_Editor.setEnabled(False)
            self.ICI_spinBox.setEnabled(False)
            self.ISD_spinBox.setEnabled(False)
        else:
            self.Start_Imaging.setEnabled(True)
            self.Terminate_Imaging.setEnabled(False)
            self.IST_Editor.setEnabled(True)
            
            
    def Begin_Imaging(self):
        self.Imaging_Thread = StartImaging()
        self.Imaging_Thread.start()
        self.StatusBar.setText("System Status: Initializing Sequence...")
        sleep(1)
        self.Update()

    def Stop_Imaging(self):
        self.Stop_Imaging_Thread = QuitImaging()
        self.Stop_Imaging_Thread.start()
        running=False
        self.StatusBar.setText("System Status: Idle...")
        sleep(1)
        self.Update()

    def Start_Livefed(self):
        self.Start_Live_Thread = Livefeed()
        self.Start_Live_Thread.start()
        self.Start_Live.setEnabled(False)
        self.Start_Live_Thread.finished.connect(lambda: self.Live_Done())

    def Live_Done(self):
        self.Start_Live.setEnabled(True)
        
        
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.Update()
        self.Update_Status.clicked.connect(lambda: self.Update())
        self.IST_Editor.editingFinished.connect(lambda: self.IST_Edit())
        self.IST_Editor.textChanged.connect(lambda: self.IST_Change())
        self.ICI_spinBox.valueChanged.connect(lambda: self.ICI_Change())
        self.ISD_spinBox.valueChanged.connect(lambda: self.ISD_Change())
        self.Start_Imaging.clicked.connect(lambda: self.Begin_Imaging())
        self.Terminate_Imaging.clicked.connect(lambda: self.Stop_Imaging())
        self.Start_Live.clicked.connect(lambda: self.Start_Livefed())
        
        

# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()

    # without this, the script exits immediately.
    sys.exit(app.exec_())




# python bit to figure how who started This
if __name__ == "__main__":
    main()
