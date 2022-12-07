import socket
import threading
from queue import Queue

HOST = socket.gethostbyname("localhost")
print(f"HOST = {HOST}")
PORT = 42000
BACKLOG = 4

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Below line makes address reusable.
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind a socket to a specific host and port - initialize it.
server.bind((HOST, PORT))

# Start the socket! Means to let the socket start listening.
server.listen(BACKLOG)

print("looking for connection")
messageSeperator = "\n"


def handleClient(client, serverChannel, cID, clientele):
    client.setblocking(1)  # Make this socket block - don't do anything until we get a message!
    msg = ""
    while True:
        try:
            msg += client.recv(10).decode("UTF-8")
            command = msg.split(messageSeperator)
            while (len(command) > 1):
                readyMsg = command[0]
                msg = messageSeperator.join(command[1:])  # only take off the first message.
                serverChannel.put(str(cID) + "_" + readyMsg)  # client ID + seperator + the message.
                command = msg.split(messageSeperator)
        except:
            clientele.pop(cID)
            return


def serverThread(clientele, serverChannel):
    while True:
        msg = serverChannel.get(True, None)  # <- block until an item is available.
        print("msg recv: ", msg)
        senderID, msg = int(msg.split("_")[0]), "_".join(msg.split("_")[1:])
        if (msg):
            for cID in clientele:
                if cID != senderID:
                    sendMsg = "playerMoved " + str(senderID) + " " + msg + messageSeperator
                    clientele[cID].send(sendMsg.encode())
        serverChannel.task_done()  # <- good practice if you need to 'join' later, but you can ignore for now! Techincally not needed.


clientele = dict()  # Use dictionaries to store information! OTHER STRUCTURES NOT NECCESARILY SAFE!
# ^ this dictionary stores the sockets of all players by CID as (CID: socket)

currID = 0

# General communication channel - like a shared walkie talkie line!
serverChannel = Queue(100)

# Start a main server 'thread'.
threading.Thread(target=serverThread, args=(clientele, serverChannel)).start()

while True:
    # Wait for a client to join the server.
    client, address = server.accept()
    print(currID)

    # Client joined! We want to tell everyone about this new player.
    for cID in clientele:
        # Print the current new client and the client we are looking through!
        print(repr(cID), repr(currID))

        # Tell current looping client about the new player.
        clientele[cID].send(f"newPlayer {currID} 100 100{messageSeperator}".encode())

        # Tell new player about this client.
        client.send(f"newPlayer {cID} 100 100{messageSeperator}".encode())

    # Set up our new client in our dictionary of clientele.
    clientele[currID] = client
    print("connection recieved")

    # Spawn a new 'thread' to now always serve this player new player!
    threading.Thread(target=handleClient, args=
    (client, serverChannel, currID, clientele)).start()
    currID += 1