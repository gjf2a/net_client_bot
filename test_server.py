from server import MessageHandler

mh = MessageHandler()
mh.start()

input("Type enter to quit")
print("Quitting...")
mh.done = True