from socket import *
serverPort = 8899
#Initiate TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
#serverSocket will be our welcoming socket
serverSocket.bind(('localhost', serverPort))
#maximum number of queued connections
serverSocket.listen(5)
print('The server is ready to receive')
while True:
    #The serverSocket wait for connection, and assign a connectionSocket to client after the connection.
    connectionSocket, addr = serverSocket.accept()

    answers = [None, None, None]
    questions = ['Have you experienced any COVID-19 symptoms in the past 14 days?',
                'Have you been in close contact with anyone who has tested positive for COVID-19 in the past 14 days?',
                'Have you tested positive for COVID-19 in the past 14 days?']
    #Iterate through questions, and repeat the question if responses are invalid.
    for index, question in enumerate(questions):
        while answers[index] != 'No' and answers[index] != 'Yes':
            connectionSocket.send(question.encode())
            response = connectionSocket.recv(1024).decode()
            answers[index] = response

    #Return green pass/red pass results to client.
    if "Yes" in answers:
        print("The server gives a red pass to the client")
        connectionSocket.send("Red Pass!".encode())
    else:
        print("The server gives a green pass to the client")
        connectionSocket.send("Green Pass!".encode())
    #Close connectionSocket.
    connectionSocket.close()
