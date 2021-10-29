from socket import *
serverName = 'localhost'
serverPort = 8888
#we are not specifying the port number of the client socket when we create it
clientSocket = socket(AF_INET, SOCK_DGRAM)
#Initial "hello message to server"
message = "Hi, the client want to establish the connection!"

while True:
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    question = ''

    #Continueously receive message from server until client got either "Green Pass!" or "Red Pass!"
    while True:
        question, server_addr = clientSocket.recvfrom(2048)
        question = question.decode()
        if question == 'Green Pass!' or question == 'Red Pass!':
            break
        answer = input(question + '\nResponse:')
        if answer == '':
            answer = '.'
        #Because we're using UDP, so everytime we send a message, we need to specify serverName and serverPort
        clientSocket.sendto(answer.encode(), (serverName, serverPort))
    #print out the result
    print(question)

    #Close UDP connection and terminate the while loop
    clientSocket.close()
    break




