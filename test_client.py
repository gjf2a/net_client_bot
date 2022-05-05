# Design inspired by: https://www.journaldev.com/15906/python-socket-programming-server-client

import sys, socket

if len(sys.argv) == 1:
    print("Usage: python test_client.py ip_addr message...")
else:
    ip = sys.argv[1]
    message = ' '.join(sys.argv[2:]) + '\n'
    print("IP address:", ip)
    with socket.socket() as sock:
        print("Socket created; attempting connection")
        sock.connect((ip, 8888))
        print("Socket connected; sending message")
        sock.send(message.encode())
        print("Message sent")
        data = sock.recv(1024).decode()
        print("Message received from server:", data)
