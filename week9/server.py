from socket import *
import sys # In order to terminate the program

# Inisialisasi socket server
serverSocket = socket(AF_INET, SOCK_STREAM)

# Menyiapkan server socket
serverPort = 6789
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:]) 
        outputdata = f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        
        connectionSocket.close()

serverSocket.close()
sys.exit()

# #Prepare a sever socket
# #Fill in start
# #Fill in end
# while True:
#     #Establish the connection
#     print('Ready to serve...')
#     connectionSocket, addr = #Fill in start #Fill in end
#     try:
#         message = #Fill in start #Fill in end
#         filename = message.split()[1]
#         f = open(filename[1:])
#         outputdata = #Fill in start #Fill in end
#         #Send one HTTP header line into socket
#         #Fill in start
#         #Fill in end
#         #Send the content of the requested file to the client
#         for i in range(0, len(outputdata)):
#             connectionSocket.send(outputdata[i].encode())
#         connectionSocket.send("\r\n".encode())
#         connectionSocket.close()
#     except IOError:
#     #Send response message forfile not found
#     #Fill in start
#     #Fill in end
#     #Close client socket
#     #Fill in start
#     #Fill in end
# serverSocket.close()
# sys.exit()  #Terminate the program after sending the corresponding
# data