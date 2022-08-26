# Design inspired by: https://www.journaldev.com/15906/python-socket-programming-server-client

import threading, socket, sys

TEXT_HEIGHT = 16

class MessageHandler(threading.Thread):
    def __init__(self):
        self.ev3 = None

    def run(self):
        print("Starting thread")
        self.go = False
        self.done = False
        server = socket.socket()
        server.bind(('0.0.0.0', 8888))
        server.listen(2)
        while not self.done:
            self.show("Waiting...", 0)
            connection, (ip, other) = server.accept()
            data = connection.recv(1024).decode()
            self.show(str(ip) + "             ", 1)
            self.show(str(other) + "           ", 2)
            self.show(str(data) + "             ", 3)
            self.go = not self.go
            connection.send(data.upper().encode())
        server.close()

    def show(self, msg, line):
        if self.ev3:
            self.ev3.screen.draw_text(0, line * (3 + TEXT_HEIGHT), msg)
