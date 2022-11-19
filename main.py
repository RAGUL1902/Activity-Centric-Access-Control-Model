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
os.system('cls')

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    policyHelper = PolicyHelper(constants.POLICY_FILE)


    def states_box(self):
        states = "\n"
        for machine in constants.machines_list:
            states += f"{machine.name} : {machine.state_name}\n"
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text=states  ,
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.after(1000,self.states_box)


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

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Control Panel",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="CTkButton",
                                                command=self.button_event)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="CTkButton",
                                                command=self.button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="CTkButton",
                                                command=self.button_event)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

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

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
                                                from_=0,
                                                to=1,
                                                number_of_steps=3,
                                                command=self.progressbar.set)
        self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
                                                command=self.progressbar.set)
        self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_right,
                                                text="CTkSwitch")
        self.switch_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_right,
                                                text="CTkSwitch")
        self.switch_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["Value 1", "Value 2"])
        self.combobox_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="CTkCheckBox")
        self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="CTkCheckBox")
        self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="CTkEntry")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Exit",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.on_closing)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.optionmenu_1.set("Dark")
        self.button_3.configure(state="disabled", text="Disabled CTkButton")
        self.combobox_1.set("CTkCombobox")
        self.radio_button_1.select()
        self.slider_1.set(0.2)
        self.slider_2.set(0.7)
        self.progressbar.set(0.5)
        self.switch_2.select()
        self.radio_button_3.configure(state=tkinter.DISABLED)
        self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        self.check_box_2.select()

    def button_event(self, event=0):
        print("Button Pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()
        self.quit()

def take_input(machines_list=constants.machines_list):
    policyHelper = PolicyHelper(constants.POLICY_FILE)
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
                PolicyHelper.show_policies(policyHelper)
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

        os.system('cls')


"""
Starting a new thread to take user inputs. Tkinter runs in the Main thread.
"""
thread = Thread(target=take_input)
thread.start()
app = App()
app.render_box()
app.states_box()
app.mainloop()
thread.join()
