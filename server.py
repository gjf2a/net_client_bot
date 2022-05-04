import threading, socket, sys

class MessageHandler(threading.Thread):
    def run(self):
        print("Starting thread")
        self.go = True
        self.done = False
        server = socket.socket()
        server.bind(('localhost', 8888))
        server.listen(2)
        while not self.done:
            print("Preparing to accept connection...")
            connection, address = server.accept()
            print("Received connection from", address)
            data = connection.recv(1024).decode()
            self.go = not self.go
            connection.send(data.upper().encode())
        server.close()
