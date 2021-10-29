from socket import *
serverPort = 8888
#Initiate UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
#Bind port number to the server socket
serverSocket.bind(('localhost', serverPort))
print("The Server is ready to receive")

while True:
    answers = [None, None, None]
    questions = ['Have you experienced any COVID-19 symptoms in the past 14 days?',
            'Have you been in close contact with anyone who has tested positive for COVID-19 in the past 14 days?',
            'Have you tested positive for COVID-19 in the past 14 days?']
    #Receive initial connection from the client
    message, clientAddress = serverSocket.recvfrom(2048)

    #Iterate through questions, and repeat the question if responses are invalid.
    for index, question in enumerate(questions):
        while answers[index] != 'No' and answers[index] != 'Yes':
            serverSocket.sendto(question.encode(), clientAddress)
            response, clientAddress = serverSocket.recvfrom(2048)
            answers[index] = response.decode()
    #Return green pass/red pass results to client.
    if "Yes" in answers:
        print("The server gives a red pass to the client")
        serverSocket.sendto("Red Pass!".encode(), clientAddress)
    else:
        print("The server gives a green pass to the client")
        serverSocket.sendto("Green Pass!".encode(), clientAddress)


    


