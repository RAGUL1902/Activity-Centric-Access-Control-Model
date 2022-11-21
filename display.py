from math import ceil
import tkinter
import tkinter.messagebox
import customtkinter
import constants
import policy_helper
import inspect
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    policyHelper = policy_helper.PolicyHelper(constants.POLICY_FILE)

    def __init__(self):
        super().__init__()

        self.title("Chemical Factory - Activity Centric Access Control")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        policyHelper = policy_helper.PolicyHelper(constants.POLICY_FILE)

        switches = {}

        def check_policy(machine_index):
            machine_name1 = constants.machines_list[int(machine_index)].name
            state = globals()["switch_"+str(machine_name1)].get().upper()
            old_state = "OFF"
            if state =="OFF":
               old_state = "ON"
            allow_toggle = policyHelper.check_policy(machine_name1, old_state,state)
            if allow_toggle and old_state=="OFF":
                switches[machine_name1].select()
                tex.delete("0.0",tkinter.END)
            elif allow_toggle and old_state=="ON":
                switches[machine_name1].deselect()
                tex.delete("0.0",tkinter.END)
            elif not allow_toggle and old_state=="OFF":
                switches[machine_name1].deselect()
                tex.insert("0.0","Change made violates the policy defined, the state will remain as it is.")
            elif not allow_toggle and old_state=="ON":
                switches[machine_name1].select()
                tex.insert("0.0","Change made violates the policy defined, the state will remain as it is.")

        
        def switch_state_0():
            check_policy(0)
        def switch_state_1():
             check_policy(1) 
        def switch_state_2():
             check_policy(2)
        def switch_state_3():
             check_policy(3)
        def switch_state_4():
             check_policy(4)
        def switch_state_5():
             check_policy(5)
        def switch_state_6():
             check_policy(6)
        def switch_state_7():
             check_policy(7)
        def switch_state_8():
             check_policy(8)
        def switch_state_9():
             check_policy(9)
        def switch_state_10():
             check_policy(10)
        def switch_state_11():
             check_policy(11)
        def switch_state_12():
             check_policy(12)
        def switch_state_13():
             check_policy(13)
        def switch_state_14():
             check_policy(14)

        switch_functions = [switch_state_0,switch_state_1, switch_state_2,switch_state_3,switch_state_4,
                            switch_state_5,switch_state_6,switch_state_7,switch_state_8,switch_state_9,switch_state_10,switch_state_11,
                            switch_state_12,switch_state_13,switch_state_14]
        
        for index, machine in enumerate(constants.machines_list):
            machine_name = machine.name
            globals()["switch_"+str(machine_name)]= customtkinter.StringVar(value=machine.state_name.lower())
            switch = customtkinter.CTkSwitch(master=self.frame_left, text=machine.name,command=switch_functions[index],
                                                  variable = globals()["switch_"+str(machine_name)], onvalue="on", offvalue="off")
 
            switch.grid(row=index%5, column=int(ceil((index+1)/5)), pady=20, padx=40,sticky="we")

            switches[machine_name] = switch

        tex = tkinter.Text(master=self.frame_left,height = 5,
              width = 30,
              bg = "light grey")
        tex.grid(row=8, column=1,columnspan=2, pady=20, padx=20, sticky="we")
        
        tex.insert(tkinter.END, "")  # insert at line 0 character 0

    def exit_window(self, event=0):
        self.destroy()

    def button_event(self, event=0):
        print("Button Pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

app = App()
app.mainloop()