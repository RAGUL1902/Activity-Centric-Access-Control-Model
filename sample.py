from tkinter import *
from tkinter import messagebox
from importlib import reload
# from constants import machines_list
import constants
master = Tk()

master.title("Activity Centric Access Control Model")
def show_state():
   for index, machine_iterator in enumerate(constants.machines_list):
                Label(master,text=machine_iterator.name).grid(row=index+1)
                Label(master,text="----->").grid(row=index+1,column=1)
                Label(master,text=machine_iterator.state_name).grid(row=index+1,column=2)
   master.after(1000, show_state)

def show_policy():
    policy = Text(master, height=100, width=100)
    #policy.pack()
    policy.grid(column=5)
    filename='policies.txt'
    with open(constants.POLICY_FILE, 'r') as f:
      policy.insert(END, f.read())
    master.after(1000, show_policy)
show_state()
show_policy()
# reload(constants)

mainloop()
