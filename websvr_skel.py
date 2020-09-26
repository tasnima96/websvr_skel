#
# CPSC-471 Assignment 1
# Tasnima Chowdhury
#
# Add various socket calls in various places, as required.
# Just a hint, see the sample TCPServer.py in the book
#
# Disclaimer:  There are no guarantees that the comments or
#              the code in this file are very accurate 
#

#import socket module
from socket import *
import sys                       # In order to terminate th   socket
from socket import *
from socket import *

# Create a TCP server socket
# AF_INET is used for IPv4 protocols
# SOCK_STREAM is used for TCP
serverPort = 1024
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 1024))
serverSocket.listen(1)

print("Web server port ", serverPort)
#Prepare a server socket
#Fill in start
#Fill in end

while True:
    #Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()    #Fill in start #Fill in end

    try:
        message = connectionSocket.recv(1024)  #Fill in start #Fill in end
        print(message)

        filename = message.split()[1]
        print(filename[1])


        f = open(filename[1:])

        outputdata = f.read() #Fill in start #Fill in end
        print(outputdata)

        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('\nHTTP/1.0 200 OK\n\n'.encode())
        #contentType: html
        #<html>
        #<head>
        #<title> Got it </title>
        #</head>
        #<body>
        #File Exists!!
        #</body>
        #</html>""".encode())

        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        pass
        #Send response message for file not found
        #Fill in start
        print("404 Not Found")
        connectionSocket.send('\HTTP/1.1 404 Not Found\n\n'.encode())
        #Fill in end

        #Close client socket
        #Fill in start
        #Fill in end

serverSocket.close()

sys.exit()    #Terminate the program after sending the corresponding data
