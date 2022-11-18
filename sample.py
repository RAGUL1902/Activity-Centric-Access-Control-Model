# # from tkinter import *
# # from tkinter import messagebox
from constants import machines_list
import tkinter as tk
from tkinter import END, ttk


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
       
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = ttk.Label(self, text="This is a smart ecosystem based on working of a factory. The working of machines is implemented using Activity-Centric Access Control Model.")
		# putting the grid in its place by using
		# grid
		label.grid(row = 3, column = 4, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="States",
		command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 0, column = 1, padx = 10, pady = 10)

		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Policies",
		command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 0, column = 2, padx = 10, pady = 10)

		


# second window frame page1
class Page1(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		for index, machine_iterator in enumerate(machines_list):
			ttk.Label(text=machine_iterator.name).grid(row=index+1)
			ttk.Label(text="----->").grid(row=index+1,column=1)
			ttk.Label(text=machine_iterator.state_name).grid(row=index+1,column=2)

		button1 = ttk.Button(self, text ="Home Page",
            command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place
		# by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Policies",
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 1, column = 2, padx = 10, pady = 10)




# third window frame page2
class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Policies", font = LARGEFONT)
		label.grid(row = 3, column = 4, padx = 10, pady = 10)
		policy = Text(master, height=100, width=100)
		policy.pack()
		policy.grid(column=3)
		filename='policies.txt'
		with open(filename, 'r') as f:
			policy.insert(END, f.read())

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="States",
							command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 0, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Home",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 0, column = 2, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.mainloop()

