import socket
import threading

HOST ='127.0.0.1'  # If running online entire own (private) ip address 
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
clients = []
activeUsers = []

def waitForConnection(clientConnection):
    while True:
        if clientConnection.recv(1024).decode("utf-8") == "Approved":
            break

#Connect users
def connectUsers(user1, user2):   #No encoding done here (The message should be encoded and passed in the fn)
    user1["connection"] = activeUsers.index(user2);
    user2["connection"] = activeUsers.index(user1);
    user1["available"] = user2["available"] = False
    clients[activeUsers.index(user1)].send(f"Connected with {user2['username']}!".encode('utf-8'))
    clients[activeUsers.index(user2)].send(f"Connected with {user1['username']}!".encode('utf-8'))

#Sending message
def sendMessage(message,user):
    receiver = user["connection"];
    recieverConnection = clients[receiver];
    clients[activeUsers.index(user)].send(message.encode('utf-8'));
    recieverConnection.send(message.encode('utf-8'));
    
#Handle fn
def handle(clientConn, user):
    while True:
        try:
            message = clientConn.recv(1024).decode()
            print(f"{activeUsers[activeUsers.index(user)]['username']} has sent a message ")
            sendMessage(message,user) # The message will be sent to everyone 
        
        except:
            clients.remove(clientConn)
            clientConn.close()
            activeUsers.remove(user)  
            break
            
#Receive fn
def receive():
    #Also can use signals acc to priority
    while True:
        clientConnection , clientAddr = server.accept()
        print(f"Connected with {str(clientAddr)} ") #Typecasting incase the address is not a string
        
        username = clientConnection.recv(1024).decode('utf-8') #1024 bits
        
        user = {"username":username, "available": True, "connection": None}
        activeUsers.append(user)
        clients.append(clientConnection)

        print(f"{user['username']} has connected ") #Server message 
        clientConnection.send("Connecting....".encode('utf-8')) 

        found = 0;
        for u in activeUsers:
            if((u["username"] != user["username"]) and u["available"]):
                connectUsers(user, u)
                if clientConnection.recv(1024).decode("utf-8") == "Approved":
                    found = 1;
        
        if(found==0):
            thread = threading.Thread(target= waitForConnection,args=(clientConnection,))
            thread.start()
            found = 1

        if(found == 1):
            thread = threading.Thread(target= handle,args=(clientConnection,user)) # We use a comma cause we want the arg to be treated as a tuple
            thread.start()
        

print("Server has started running")
receive()
