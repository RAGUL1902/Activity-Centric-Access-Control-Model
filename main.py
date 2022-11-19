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
    print("\n\n ---------------------- COMMANDS-------------------")
    print('\n show_policies() - show policies')
    print('\n show_activity() - show current activity status')
    print('\n help() - to print all command')
    print("\n\n --------------------------------------------------")

    while 1:

        print("\n Enter :")
        print("\n '1' for Policy Related")
        print("\n '2' for Activity Related")
        print("\n 'help()' to see all commands")
        print("\n 'exit' to close the program")

        command_1 = input("\n->")

        if command_1 == "exit":
            break

        if command_1 == '1':
            print("\n-------------------  POLICY RELATED ---------------------")
            print('\n\n')

            print('\n "1" to add new policy')
            print('\n "2" to delete policy')
            print('\n "3" to show policy')

            command_2 = input("\n->")

            if command_2 == '1':
                print("\n-------------------  ADD POLICY ---------------------")
                a1 = input("\n-> Enter the machine for new policy :")
                b1 = input("\n-> Enter the New State of the machine :")
                c1 = input("\n-> Enter the activity of the machine :")

                print("\n-> ENTER PRECONDITIONS")
                d1 = input('\n-> Enter precondition Machine name :')
                e1 = input('\n-> Enter pre condition Machine state :')
                f1 = input('\n-> Enter pre condition machine activity :')

                print("\n-> ENTER CONCURRENT CONDITIONS")
                j1 = input('\n-> Enter concurrent condition Machine name :')
                k1 = input('\n-> Enter concurrent condition Machine state :')
                l1 = input(
                    '\n-> Enter concurrent condition machine activity :')

                print("\n-> ENTER POSTCONDITIONS")
                g1 = input('\n-> Enter post condition Machine name :')
                h1 = input('\n-> Enter post condition Machine state :')
                i1 = input('\n-> Enter post condition machine activity :')

                PolicyHelper.add_policy(policyHelper, a1, b1, c1, [
                                        d1, e1, f1], [j1, k1, l1], [g1, h1, i1])
                print('\n---------------------------------------------------------')
                pass
            elif command_2 == '2':
                print("\n-------------------  DELETE POLICY ---------------------")

                policy_no = input(
                    "\n-> Enter policy number you want to delete :")
                PolicyHelper.delete_policy(policyHelper, policy_no)
                print('\n---------------------------------------------------------')
                pass
            elif command_2 == '3':
                print("\n-------------------  SHOW POLICY ---------------------")
                PolicyHelper.get_policies(policyHelper)
                print('\n---------------------------------------------------------')
                pass
            else:
                print('INVALID COMMAND')
                print('Enter "help" to see all commands')

        elif command_1 == '2':
            print("\n-------------------  ACTIVITY RELATED ---------------------")
            print('\n\n ')

            print('\n "1" to show all machines')
            print('\n "2" to show current status of all machines')
            print('\n "3" change state of a machine')

            command_2 = input("\n->")

            if command_2 == '1':

                print("\n-------------------  LIST OF MACHINES ---------------------")
                for machine_iterator in machines_list:
                    print("\n" + machine_iterator.name)
                print('\n---------------------------------------------------------')
                pass

            elif command_2 == '2':
                print("\n-------------------  STATE OF MACHINES ---------------------")
                for machine_iterator in machines_list:

                    machine_iterator.show_state()
                print('\n---------------------------------------------------------')
                pass
                pass
            elif command_2 == '3':
                print(
                    "\n-------------------  CHANGE MACHINE STATE ---------------------")
                machine_name = input("\n->Enter machine name:")
                val = input("\n->Enter new state (ON/OFF) :")

                machine_exist = False
                for itr in machines_list:
                    if itr.name == machine_name:
                        machine_exist = True
                        if (itr.state_name == val):
                            print('\n->'+machine_name +
                                  ' is already in ' + val + ' state')

                        else:
                            policyHelper.check_policy(
                                machine_name, itr.state_name, val)
                if machine_exist == False:
                    print('\n Enter Correct Machine Name')

                pass
            else:
                print('INVALID COMMAND')
                print('Enter "help" to see all commands')
            # time.sleep(5)

        else:
            print('INVALID COMMAND')
            print('Enter "help" to see all commands')
            # time.sleep(5)

        print("\n --------------------------next iteration----------------------------")



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
