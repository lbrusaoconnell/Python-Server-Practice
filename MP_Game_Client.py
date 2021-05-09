import socket
import threading
import time
import turtle

HEADER = 64
PORT = 3309
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#SERVER =  '47.149.222.226'
SERVER =  '192.168.1.56'
ADDR = (SERVER, PORT)

#screen size
screen_width = 800
screen_length = 800

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))




def generate_field():
	#makes the window
	wn = turtle.Screen()
	wn.setup(width=screen_width, height=screen_length)

def show(x,y):
	player_x = x
	player_y = y
	print(player_x)
	print(player_y)
	player.goto(x,y)
	coordinates = str(x)+str(y)
	send(coordinates)


def generate_player():
	global player
	player = turtle.Turtle()
	player.showturtle()
	player.shape("circle")
	player.goto(0,0)
	#turtle.onscreenclick()
	turtle.onscreenclick(show)










def start():
	turtle.listen()
	generate_field()
	generate_player()
	turtle.mainloop()






start()