# always seem to need this
import sys
import os
import time
import subprocess
 
# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *

# This is our window from QtCreator
import ABCD_UI

#import custom functions
import Camera

#camera libraries
from picamera import PiCamera
from time import sleep

#email libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#global variables
file_list = []
link =""
email=""
interval = 0
duration = 0
total = 0
current = 0
current_image = None
file = None
name = None
on_flag = False
half_flag = None

class Image(QThread):

    done = QtCore.pyqtSignal()
    capture = QtCore.pyqtSignal()
    half = QtCore.pyqtSignal()
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        global current, current_image, file_list, total
        for i in range(total):
            current = i
            sleep(0.2)
            current_image = file % i
            with PiCamera() as camera:
                sleep(0.8)
                camera.resolution = (2464,2464)
                camera._set_rotation(180)
                camera.capture(current_image)
            file_list.append(current_image)
            self.capture.emit()
            if(current == int(total/2)):
                self.half.emit()
            sleep(interval-1)
        self.done.emit()
    def stop(self):
        self.running = False

class Dropbox(QThread):
    upload_complete = QtCore.pyqtSignal()
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        global file_list, name, link

        os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh mkdir /" + name)
        link = str(subprocess.check_output("/home/pi/Dropbox-Uploader/dropbox_uploader.sh share /" + name, shell=True))
        link = link.replace("b' > ", "")
        link = link.split("\\")[0]
        while True:
            if (len(file_list) > 0):
                os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + file_list[0] + " /"+name)
                os.system("rm " + file_list[0])
                del file_list[0]
            if(current == total - 1 and len(file_list) == 0):
                self.upload_complete.emit()

class Email(QThread):
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        sys.path.insert(0,'../../HP')
        import Email
        global link, current, total, half_flag, name
        fromaddr = "notification_noreply@flashlapseinnovations.com"
        toaddr = email
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "FLASHLAPSE NOTIFICATION"

        if (half_flag == None):
            sleep(5)
            print(link)
            body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" has been initiated, check it out here.\n" + link + "\n\nTeam Flashlapse"
            msg.attach(MIMEText(body, 'plain'))
        elif(half_flag == False):
            body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is 50% complete, check it out here.\n" + link + "\n\nTeam Flashlapse"
            msg.attach(MIMEText(body, 'plain'))
            half_flag = True
        else:
            body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is complete, check it out here.\n" + link + "\n\nTeam Flashlapse"
            msg.attach(MIMEText(body, 'plain'))
            half_flag = None

        server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(Email.user, Email.password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
           


# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, ABCD_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def IST_Edit(self):
        global name
        name = self.IST_Editor.text()
        
    def IST_Change(self):
        global interval, duration, total, email, name
        self.ICI_spinBox.setEnabled(True)
        temp = self.IST_Editor.text()
        
        if(len(temp)==0):
            self.Start_Imaging.setEnabled(False)
            name=""
            
        if(interval!= 0):
            total = int((duration*60)/interval)
            if(total>0 and len(email) > 0 and len(temp) > 0):
                self.Start_Imaging.setEnabled(True)
            else:
                self.Start_Imaging.setEnabled(False)
        
        
    def ICI_Change(self):
        global interval, duration, total, email, name
        interval = self.ICI_spinBox.value()
        self.ISD_spinBox.setEnabled(True)
        if(interval == 0):
            self.ISD_spinBox.setEnabled(False)
            self.Start_Imaging.setEnabled(False)
        else:
            total = int((duration*60)/interval)
            if(total>0 and len(email) > 0 and len(name) > 0):
                self.Start_Imaging.setEnabled(True)
            else:
                self.Start_Imaging.setEnabled(False)
                
    def ISD_Change(self):
        global interval, duration, total, email, name
        duration = self.ISD_spinBox.value()
        if(duration == 0):
            self.Start_Imaging.setEnabled(False)
        if(interval!= 0):
            total = int((duration*60)/interval)
            if(total>0 and len(email) > 0 and len(name) > 0):
                self.Start_Imaging.setEnabled(True)
            else:
                self.Start_Imaging.setEnabled(False)
        
    def Start_Snapshot(self):
        self.Snap_Thread = Camera.Snap()
        self.Snap_Thread.started.connect(lambda: self.Processing_Snapshot())
        self.Snap_Thread.finished.connect(lambda: self.Processing_Complete())
        self.Snap_Thread.start()
        
    def Processing_Snapshot(self):
        self.Snapshot.setEnabled(False)
        self.Snapshot.setText("Processing...")
        
    def Processing_Complete(self):
        user_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
        self.Image_Frame.setPixmap(QtGui.QPixmap(user_img))
        self.Snapshot.setEnabled(True)
        self.Snapshot.setText("Snapshot")
        
    def Start_Live_Feed(self):
        self.Live_Thread = Camera.Live()
        self.Live_Thread.started.connect(lambda: self.Processing_Live())
        self.Live_Thread.finished.connect(lambda: self.Live_Complete())
        self.Live_Thread.start()
        
    def Processing_Live(self):
        self.Snapshot.setEnabled(False)
        self.Live_Feed.setEnabled(False)
        self.Start_Imaging.setEnabled(False)
        self.Live_Feed.setText("Processing...")
        
    def Live_Complete(self):
        self.Snapshot.setEnabled(True)
        self.Live_Feed.setEnabled(True)
        self.Start_Imaging.setEnabled(True)
        self.Live_Feed.setText("Start Live Feed (30s)")

    def Half_Notif(self):
        global half_flag
        half_flag = False
        self.Email_Thread = Email()
        self.Email_Thread.start()
        
        
    def Begin_Imaging(self):
        global jpg, name, duration, interval, total, file, on_flag, file_list
        
        if (on_flag == False): 
            self.Image_Thread = Image()
            self.Dropbox_Thread = Dropbox()
            self.Email_Thread = Email()
            total = int((duration*60)/interval)
            self.Progress_Bar.setMaximum(total)
            
            if (self.JPG.isChecked()):
                file = "../_temp/" +name + "_%04d.jpg"
            else:
                file = "../_temp/" +name + "_%04d.png"
            self.Image_Thread.started.connect(lambda: self.Start_Image())
            self.Image_Thread.finished.connect(lambda: self.Done())
            self.Image_Thread.capture.connect(lambda: self.Progress())
            self.Image_Thread.half.connect(lambda: self.Half_Notif())

            self.Image_Thread.start()
            self.Dropbox_Thread.start()
            self.Email_Thread.start()
            on_flag = True
        
        else:
            half_flag = None
            self.Image_Thread.terminate()
            self.IST_Editor.setEnabled(True)
            self.ICI_spinBox.setEnabled(True)
            self.ISD_spinBox.setEnabled(True)
            self.Live_Feed.setEnabled(True)
            self.Snapshot.setEnabled(True)
            self.JPG.setEnabled(True)
            self.PNG.setEnabled(True)
            self.Dropbox_Email.setEnabled(True)
            self.Dropbox_Confirm.setEnabled(True)
            self.Frequency_Off.setEnabled(True)
            self.Frequency_Low.setEnabled(True)
            self.Frequency_Average.setEnabled(True)
            self.Frequency_High.setEnabled(True)
            self.Image_Frame.setPixmap(QtGui.QPixmap("../_image/background1.png"))
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("../_image/Start-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Start_Imaging.setIcon(icon3)
            self.Start_Imaging.setText("Start Image Sequence")
            self.Progress_Bar.setValue(0)
            del file_list[:]
            self.Image_Thread.terminate()
            self.Dropbox_Thread.terminate()
            on_flag = False

    def Done(self):
        self.Email_Thread = Email()
        self.Email_Thread.start()
        self.Start_Imaging.setText("Start Another Sequence")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../_image/Start-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start_Imaging.setIcon(icon3)
        
    def Progress(self):
        global current, current_image
        self.Progress_Bar.setValue(current+1)
        self.Image_Frame.setPixmap(QtGui.QPixmap(current_image))

    def Email_Change(self):
        global email
        match =None
        import re
        temp_email = self.Dropbox_Email.text()
        if (len(temp_email)==0):
            self.Start_Imaging.setEnabled(False)
            email=""
        if (len(temp_email)) > 7:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', temp_email)
        if (match != None):
            self.Dropbox_Confirm.setEnabled(True)
        else:
            self.Start_Imaging.setEnabled(False)
            self.Dropbox_Confirm.setEnabled(False)
<<<<<<< HEAD
            
=======
            self.Cloud_Sync.setEnabled(False)

>>>>>>> a03a3b981271bab7d6ce6829f83f039df4670aca

    def Email_Entered(self):
        global email, total
        email = self.Dropbox_Email.text()
        if(total>0 and len(email) > 0):
            self.Start_Imaging.setEnabled(True)
        else:
            self.Start_Imaging.setEnabled(False)
        
            
    def Start_Image(self):
                
        self.IST_Editor.setEnabled(False)
        self.ICI_spinBox.setEnabled(False)
        self.ISD_spinBox.setEnabled(False)
        self.Live_Feed.setEnabled(False)
        self.Snapshot.setEnabled(False)
        self.JPG.setEnabled(False)
        self.PNG.setEnabled(False)
        self.Dropbox_Email.setEnabled(False)
        self.Dropbox_Confirm.setEnabled(False)
        self.CyVerse_Email.setEnabled(False)
        self.CyVerse_Confirm.setEnabled(False)
        self.Frequency_Off.setEnabled(False)
        self.Frequency_Low.setEnabled(False)
        self.Frequency_Average.setEnabled(False)
        self.Frequency_High.setEnabled(False)
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../_image/Stop-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start_Imaging.setIcon(icon2)
        self.Start_Imaging.setText("Stop Image Sequence")

    def Check_Network(self):
        import socket
        REMOTE_SERVER = "www.google.com"
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
        except:
            pass
            sys.exit()
        
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.Check_Network()
        self.IST_Editor.editingFinished.connect(lambda: self.IST_Edit())
        self.IST_Editor.textChanged.connect(lambda: self.IST_Change())
        self.ICI_spinBox.valueChanged.connect(lambda: self.ICI_Change())
        self.ISD_spinBox.valueChanged.connect(lambda: self.ISD_Change())
        self.Snapshot.clicked.connect(lambda: self.Start_Snapshot())
        self.Live_Feed.clicked.connect(lambda: self.Start_Live_Feed())
        self.Start_Imaging.clicked.connect(lambda: self.Begin_Imaging())
        self.Dropbox_Email.textChanged.connect(lambda: self.Email_Change())
        self.Dropbox_Confirm.clicked.connect(lambda: self.Email_Entered())

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
