import socket
import threading
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
import re
import AESEncryption
import AESDecryption;

HOST = '127.0.0.1' # For online enter public ip address here 
PORT = 9090  #Open the port on the server site for online

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT)) #Connect instead of bind 

def write():        
        message = f"{nickname}: {input_area.get('1.0','end')}"  #Can be done on either server or client
        # 1.0 to end means get the whole text
        encryptedMessage = AESEncryption.encrypt(message);
        sock.send(encryptedMessage.encode('utf-8'))
        input_area.delete('1.0','end')

def stop():
        if tkinter.messagebox.askokcancel("Notice", "Are you sure you want to close the window?"):
            running = False
            win.destroy()
            sock.close()
            exit(0)

def receive ():
        sock.send(nickname.encode('utf-8'))
        print(sock.recv(1024).decode('utf-8'))
        while running:
            try:
                message = sock.recv(1024).decode('utf-8')
                while True:
                    if(gui_done):
                        break;                
                if re.search("Connected with.*$",message):
                    sock.send("Approved".encode('utf-8'))
                    text_area.config(state= 'normal')
                    text_area.insert('end',message+"\n") #Inserts the message at the end 
                    text_area.yview('end')
                    text_area.config(state= 'disabled')
                    input_area.config(state="normal")
                    #send_button.config(state = 'normal')
                elif re.search(".* has left the chat$",message):
                    sock.send("Available".encode('utf-8'))
                    text_area.config(state= 'normal')
                    text_area.insert('end',message+"\n") #Inserts the message at the end 
                    text_area.yview('end')
                    text_area.config(state= 'disabled')
                    input_area.config(state="disabled")
                else:
                    decryptedMessage = AESDecryption.decrypt(message);
                    text_area.config(state= 'normal')
                    text_area.insert('end',decryptedMessage) #Inserts the message at the end 
                    text_area.yview('end')
                    text_area.config(state= 'disabled')
                    #send_button.config(state = 'normal')
                        
            except ConnectionAbortedError:
                break
            except:
                print("Error !!")
                sock.close()
                break  

# GUI part 
msg = tkinter.Tk()
msg.withdraw()
        
nickname = simpledialog.askstring("Nickname"," Please choose a nickname ", parent = msg )
        
gui_done = False
running = True

win = tkinter.Tk()
win.configure(bg="lightgray") #Background

chat_label = tkinter.Label(win, text="Chat:",bg="lightgray") #Texts
chat_label.config(font=("Arial",12)) #Fonts
chat_label.pack(padx=20, pady=5) #For decoration provides no functionality
        
text_area = tkinter.scrolledtext.ScrolledText(win)
text_area.pack(padx=20,pady =5)
text_area.config(state ='disabled')
        
msg_label = tkinter.Label(win, text="Message:",bg="lightgray") #Texts
msg_label.config(font=("Arial",12)) #Fonts
msg_label.pack(padx=20, pady=5) #For decoration provides no functionality
        
input_area = tkinter.Text(win,height = 3)
input_area.config(state="disabled")
input_area.pack(padx=20,pady=5)
        
send_button = tkinter.Button(win, text= "Send", command = write)
send_button.config(font=("Arial",12))
send_button.pack(padx=20, pady=5)
        
gui_done = True             

receive_thread = threading.Thread(target=receive)
receive_thread.start()

win.protocol("WM_DELETE_WINDOW",stop)  #To terminate the whole program
win.mainloop() 
