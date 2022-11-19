from importlib import reload
from tkinter import messagebox
from tkinter import *
import os
import constants
from policy_helper import PolicyHelper
from threading import Thread
import tkinter
import tkinter.messagebox
import customtkinter
import sys

# TODO help function
# os.system('cls')

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

policyHelper = PolicyHelper(constants.POLICY_FILE)

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520
    
    policyHelper = policyHelper

    def policy_box(self):
        policies = "\n"
        for policy in self.policyHelper.policy_list:
            policies += f"{policy.get_policy_string()}\n"

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text=policies,
                                                   height=500,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT,
                                                   anchor="w")
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.after(5000,self.policy_box)
    

    def render_box(self):
        self.title("Chemical Factory - Activity Centric Access Control")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)


    def button_event(self, event=0):
        print("Button Pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()
        self.quit()

def take_input(machines_list=constants.machines_list):
    global policyHelper
    print("\n---------------------- COMMANDS-------------------")
    print('\nget_policies')
    print('delete_policy <policy_number>')
    print('add_policy')
    print('help()')
    print("--------------------------------------------------")

    while 1:

        input_command = input('\n->') 

        command = input_command.split()

        if command[0] == "exit":
            break

        elif command[0] == 'get_policies':
            policies = policyHelper.get_policies()
            print(policies)
        
        elif command[0] == 'delete_policy' :
            policyHelper.delete_policy( command[1])
        
        elif command[0] == 'add_policy' :

            print("Enter new policy in the following format :")
            add_policy_string = input("Machine Newstate , Pre_condition state , concurrent_Condition state , post_condition state\n")
            
            words = add_policy_string.split()

            if len(words) != 11 :
                print('Format Error')
            words.remove(',')
            words.remove(',')
            words.remove(',')

            policyHelper.add_policy( words[0], words[1], '-', [
                                        words[2], words[3], '-'], [words[4], words[5], '-'], [words[6], words[7], '-'])
            
        elif command[0] == 'help()':
            help()

        elif command[0] == 'cls' :
            os.system('cls')
        else:
                print('INVALID COMMAND')
                print('Enter "help()" to see all commands')
        


"""
Starting a new thread to take user inputs. Tkinter runs in the Main thread.
"""
thread = Thread(target=take_input)
thread.start()
app = App()
app.render_box()
app.policy_box()
app.mainloop()
thread.join()
