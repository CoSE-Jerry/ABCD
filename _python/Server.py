import socket
import subprocess
import os
import sys
from picamera import PiCamera
from threading import Thread
from time import sleep

host = ''
port = 5560
title = ''
file=''
reply=''
currentnum = 0
interval = 0
duration = 0
total=0
terminate=False
file_list = []

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    return conn

def dataTransfer(conn):
    global interval, duration, title,terminate,reply,currentnum,total
    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = data.split('-', 5)
        command = dataMessage[0]
        if command == 'CURR':
            reply = title+"-"+str(interval)+"-"+str(duration)+"-"+str(currentnum)+"-"+str(total)
        elif command == 'CAM':
            title = dataMessage[1]
            interval = int(dataMessage[2])
            duration = int(dataMessage[3])
            reply = title
            #Create Class
            Camera = CameraProgram()
            #Create Thread
            CameraThread = Thread(target=Camera.run) 
            #Start Thread 
            CameraThread.start()

            Dropbox = DropboxProgram()
            #Create Thread
            DropboxThread = Thread(target=Dropbox.run) 
            #Start Thread 
            DropboxThread.start()

        elif command == 'LIVE':
            with PiCamera() as camera:
                camera._set_rotation(180)
                camera.resolution = (1920,1080)
                camera.zoom = (0.3, 0.3, 0.3, 0.3)
                camera.start_preview()
                sleep(60)
            
        elif command == 'QUIT':
            currentnum = 0
            total = 0
            terminate=True;

        elif command == 'REBOOT':
            os.system("sudo reboot")
            
        elif command == 'SNAP':
            SnapShot = SnapShotProgram()
            #Create Thread
            SnapShotThread = Thread(target=SnapShot.run) 
            #Start Thread 
            SnapShotThread.start()
            
        else:
            reply = 'Unknown Command'
            
        # Send the reply back to the client
        conn.sendall(str.encode(reply))
    conn.close()
    
class CameraProgram:  
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        global file_list, file,total,currentnum,terminate
        sleep(5)
        get = os.popen('hostname -I').read()
        ip = get.split('.', 4)
        
        total = int(duration/interval)
        file = "/home/pi/ABCD/_temp/" +title +"_"+ip[3].strip()+ "_%04d.jpg"
        for i in range(total):
            currentnum = i
            sleep(0.2)
            current_image = file % i
            with PiCamera() as camera:
                print("Image Captured")
                sleep(0.8)
                camera.resolution = (2464,2464)
                camera._set_rotation(180)
                camera.capture(current_image)
            file_list.append(current_image)
            for x in range(0,interval*60):
                if(terminate):
                    break
                else:
                    sleep(1)
            if(terminate):
                break
        if(terminate):
            terminate=False

class DropboxProgram:  
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        get = os.popen('hostname -I').read()
        ip = get.split('.', 4)
        
        
        global file_list, title
        os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh mkdir /ABCD/" + title)
        os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh mkdir /ABCD/" + title+"/"+ip[3].strip())
        
        while (terminate==False):
            if (len(file_list) > 0):
                os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + file_list[0] + " /ABCD/"+title+"/"+ip[3].strip())
                os.system("rm " + file_list[0])
                del file_list[0]
                
class SnapShotProgram:  
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        get = os.popen('hostname -I').read()
        ip = get.split('.', 4)
        file = "/home/pi/ABCD/_temp/Snap_"+ip[3].strip()+".jpg"

        with PiCamera() as camera:
            sleep(0.8)
            camera.resolution = (2464,2464)
            camera._set_rotation(180)
            camera.capture(file)
        os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh mkdir /ABCD/Snapshot")
        os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + file + " /ABCD/Snapshot/")
                

s = setupServer()

while True:
    while True:
        try:
            conn = setupConnection()
            dataTransfer(conn)
        except socket.error as msg:
            print("disconnect")
        
