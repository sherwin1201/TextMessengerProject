import socket 
import threading

HOST ='127.0.0.1'  # If running online entire own (private) ip address 
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
clients = []
nicknames =[]

#Broadcast fn
def broadcast(message):   #No encoding done here (The message should be encoded and passed in the fn)
    for n in clients:
        n.send(message)

#Handle fn
def handle(clientConn):
    while True:
        try:
            message = clientConn.recv(1024)
            print(f"{nicknames[clients.index(clientConn)]} has sent a message ")
            broadcast(message) # The message will be sent to everyone 
        
        except:
            index = clients.index(clientConn)
            clients.remove(clientConn)
            clientConn.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)  
            break
            
#Receive fn
def receive():
    #Also can use signals acc to priority
    while True:
        clientConnection , clientAddr = server.accept()
        print(f"Connected with {str(clientAddr)} ") #Typecasting incase the address is not a string
        
        clientConnection.send("NICK".encode('utf-8')) #Used for communication btn the server and the client
        nickname = clientConnection.recv(1024).decode('utf-8') #1024 bits
        
        nicknames.append(nickname)
        clients.append(clientConnection)

        print(f"{nickname} has connected ") #Server message 
        broadcast(f"{nickname} has joined the server \n ".encode("utf-8")) #Broadcasting message
        clientConnection.send("You have connected to the server".encode('utf-8')) #Client message
        
        thread = threading.Thread(target= handle,args=(clientConnection,)) # We use a comma cause we want the arg to be treated as a tuple
        thread.start()
        

print("Server has started running")
receive()
