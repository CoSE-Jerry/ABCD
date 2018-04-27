import socket
from picamera import PiCamera
from threading import Thread
from time import sleep

host = ''
port = 5560
title = ''
email = ''
file=''
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

def CALL():
    reply = "CONNECTED"
    return reply

def dataTransfer(conn):
    global interval, duration, title, email,terminate
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
            reply = title+"-"+str(interval)+"-"+str(duration)+"-"+email+"-"+str(total)+"-"+str(currentnum)
        elif command == 'CAM':
            title = dataMessage[1]
            interval = int(dataMessage[2])
            duration = int(dataMessage[3])
            #email = dataMessage[4]
            reply = title
            #Create Class
            Camera = CameraProgram()
            #Create Thread
            CameraThread = Thread(target=Camera.run) 
            #Start Thread 
            CameraThread.start()
        elif command == 'QUIT':
            terminate=True;
            
        else:
            reply = 'Unknown Command'
            
        # Send the reply back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent!")
    conn.close()
    
class CameraProgram:  
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        global file_list, file,total,currentnum,terminate
        total = int((duration*60)/interval)
        file = "../_temp/" +title + "_%04d.jpg"
        while(terminate==False):
            for i in range(total):
                currentnum = i
                sleep(0.2)
                current_image = file % i
                with PiCamera() as camera:
                    print("image cap")
                    sleep(0.8)
                    camera.resolution = (3280,2464)
                    camera._set_rotation(180)
                    camera.capture(current_image)
                file_list.append(current_image)
                for x in range(0,interval-1):
                    while(terminate==False):
                        sleep(1)
        if(terminate):
            print("killed")
            terminate=False
            

s = setupServer()

while True:
    while True:
        try:
            conn = setupConnection()
            dataTransfer(conn)
        except socket.error as msg:
            print("disconnect")
        
