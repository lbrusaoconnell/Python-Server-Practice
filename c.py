import socket
import threading
import time
import turtle

HEADER = 64
PORT = 2021
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#SERVER =  '47.149.222.226'
SERVER =  '192.168.1.56'
ADDR = (SERVER, PORT)

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


def generate_board():

	#screen size
	screen_width = 800
	screen_length = 800
	#side length of each square
	square_size = 80
	#how many squares there are per lane
	lane_length = 8
	#how many lanes there are (since we want the board to be a square, the amount of lanes is equal to the amount of squares per lane)
	lanes = lane_length

	#makes the window
	wn = turtle.Screen()
	wn.bgcolor("lightgreen")
	wn.setup(width=screen_width, height=screen_length)
	wn.tracer(0)

	#creates the turtle
	pen = turtle.Turtle()
	pen.penup()
	pen.goto(-((square_size * lane_length)/2),((square_size * lane_length)/2))
	pen.pendown()

	#makes the turtle go foward "square_length" units and then turn 90 degrees 4 times to make a square
	def box():
		for i in range(4):
			pen.forward(square_size)
			pen.right(90)

	#creates the board with all the squares
	def board():

		#sets the x and y coordinates to half the size of the board
		#Which is found by multiplying the size of each square by how many squares there are per column and dividing it by 2
		x = -((square_size * lane_length)/2)
		y = (square_size * (lane_length / 2))
		count = 0

		#makes a horizontal column then lower the y value of the turtle so that it can create another column directly underneath the first
		for k in range(lanes):

			#makes a box "lane_length" amounts of times, and moves them over one box size each time so that they're created lined up next to each other
			for j in range(lane_length):

				#changes the count from even to odd or odd to even every time a box is created
				count += 1

				#makes different squares black or white
				pen.begin_fill()

				if (int(count) % 2) == 0:
					pen.fillcolor("black")
				else:
					pen.fillcolor("white")

				box()
				pen.end_fill()

				#moves the turtle to the right one box length
				x += square_size
				pen.penup()
				pen.goto(x,y)
				pen.pendown()

			#adds one so that the pen filling pattern alternates
			count += 1

			#brings the turtle back to the far left side of the board and lowers it one column
			x = -((square_size * lane_length)/2)
			y -= square_size
			pen.penup()
			pen.goto(x,y)
			pen.pendown()


	#creates the turtle
	quadrants = turtle.Turtle()
	quadrants.hideturtle()
	quadrants.penup()

	#writes A-H and 1-8 on horizontal axis and the vertical axis respectively
	def x_axis_letters():
		y = -372
		x = -292
		counter = 0
		letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
		for a in range(8):
			quadrants.goto(x, y)
			quadrants.write(letters[counter], font=("Arial", 30, "normal"))
			x += 80
			counter += 1

	def y_axis_numbers():
		x2 = -355
		y2 = 257
		counter2 = 0
		numbers = ["8", "7", "6", "5", "4", "3", "2", "1"]
		for b in range(8):
			quadrants.goto(x2, y2)
			quadrants.write(numbers[counter2], font=("Arial", 30, "normal"))
			y2 -= 80
			counter2 += 1

	#executes the function, board
	board()
	x_axis_letters()
	y_axis_numbers()

	#gets the mouse coordinates on click
	def get_mouse_click_coor(x, y):
		global square_coord
		chessX = " "
		chessY = " "
		mouse_x = x
		mouse_y = y
		#print(mouse_x, mouse_y)
		if (mouse_x in range(-320, -240)):
			chessX = "A"
		if (mouse_x in range(-240, -160)):
			chessX = "B"
		if (mouse_x in range(-160, -80)):
			chessX = "C"
		if (mouse_x in range(-80, 0)):
			chessX = "D"
		if (mouse_x in range(0, 80)):
			chessX = "E"
		if (mouse_x in range(80, 160)):
			chessX = "F"
		if (mouse_x in range(160, 240)):
			chessX = "G"
		if (mouse_x in range(240, 320)):
			chessX = "H"

		if (mouse_y in range(-320, -240)):
			chessY = "1"
		if (mouse_y in range(-240, -160)):
			chessY = "2"
		if (mouse_y in range(-160, -80)):
			chessY = "3"
		if (mouse_y in range(-80, 0)):
			chessY = "4"
		if (mouse_y in range(0, 80)):
			chessY = "5"
		if (mouse_y in range(80, 160)):
			chessY = "6"
		if (mouse_y in range(160, 240)):
			chessY = "7"
		if (mouse_y in range(240, 320)):
			chessY = "8"

		if not (" " in chessX + chessY):
			square_coord = chessX + chessY
			send(square_coord)


	turtle.onscreenclick(get_mouse_click_coor) 

	turtle.mainloop()

generate_board()