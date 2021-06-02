import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = '127.0.0.1' # For online enter public ip address here 
PORT = 9090  #Open the port on the server site for online

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((host,port)) #Connect instead of bind 
        
        # GUI part 
        msg = tkinter.Tk()
        msg.withdraw()
        
        self.nickname = simpledialog.askstring("Nickname"," Please choose a nickname ", parent = msg )
        self.gui_done = False # Like a lock that prevents unneccesary starts
        self.running = True
        
        gui_thread = threading.Thread(target=self.gui_loop)  # Gui loop is a fn i,e builds the gui 
        receive_thread = threading.Thread(target=self.receive) # Deals with the server connection
        
        gui_thread.start()
        receive_thread.start()
        
    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgray") #Background

        self.chat_label = tkinter.Label(self.win, text="Chat:",bg="lightgray") #Texts
        self.chat_label.config(font=("Arial",12)) #Fonts
        self.chat_label.pack(padx=20, pady=5) #For decoration provides no functionality
        
        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20,pady =5)
        self.text_area.config(state ='disabled')
        
        self.msg_label = tkinter.Label(self.win, text="Message:",bg="lightgray") #Texts
        self.msg_label.config(font=("Arial",12)) #Fonts
        self.msg_label.pack(padx=20, pady=5) #For decoration provides no functionality
        
        self.input_area = tkinter.Text(self.win,height = 3)
        self.input_area.pack(padx=20,pady=5)
        
        self.send_button = tkinter.Button(self.win, text= "Send", command = self.write)
        self.send_button.config(font=("Arial",12))
        self.send_button.pack(padx=20, pady=5)
        
        self.gui_done = True 
        self.win.protocol("WM_DELETE_WINDOW",self.stop)  #To terminate the whole program
        self.win.mainloop()
        
    def write(self):        
        message = f"{self.nickname}: {self.input_area.get('1.0','end')}"  #Can be done on either server or client
        # 1.0 to end means get the whole text
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0','end')
        
    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive (self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if message == "NICK":
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state= 'normal')
                        self.text_area.insert('end',message) #Inserts the message at the end 
                        self.text_area.yview('end')
                        self.text_area.config(state= 'disabled')
            except ConnectionAbortedError:
                break
            except:
                print("Error !!")
                self.sock.close()
                break                
        
client = Client(HOST,PORT)
