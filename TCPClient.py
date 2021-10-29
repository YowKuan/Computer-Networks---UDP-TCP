from socket import * 
serverName = 'localhost'
serverPort = 8899
#Initiate TCP connection
clientSocket = socket(AF_INET, SOCK_STREAM)
#Make connection to the server
clientSocket.connect((serverName, serverPort))

while True:
    question = clientSocket.recv(1024)
    question = question.decode()
    if question == 'Green Pass!' or question == 'Red Pass!':
        break
    answer = input(question + '\nResponse:')
    #No specification on serverName and Server port because the server has already provided dedicated connetionSocket to receive message.
    clientSocket.send(answer.encode())
print(question)

clientSocket.close()