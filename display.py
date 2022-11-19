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

        policyHelper = policy_helper.PolicyHelper(constants.POLICY_FILE)


        def check_policy(machine_index):
            machine_name1 = constants.machines_list[int(machine_index)].name
            state = globals()["switch_"+str(machine_name1)].get().upper()
            old_state = "OFF"
            if state =="OFF":
               old_state = "ON"
            allow_toggle = policyHelper.check_policy(machine_name1, old_state,state,constants.machines_list)
            #machine_name = 'mixer_1'
            if allow_toggle and old_state=="OFF":
                self..select()
            elif allow_toggle and old_state=="ON":
                self.machine_name1.deselect()
            elif not allow_toggle and old_state=="OFF":
                self.machine_name1.deselect()
            elif not allow_toggle and old_state=="ON":
                self.machine_name1.select()
        
        def switch_state_0():
            check_policy(0)       
        def switch_state_1():
            allow_toggle = check_policy(1) 
        def switch_state_2():
            allow_toggle = check_policy(2)
        def switch_state_3():
            allow_toggle = check_policy(3)
        def switch_state_4():
            allow_toggle = check_policy(4)
        def switch_state_5():
            allow_toggle = check_policy(5)
        def switch_state_6():
            allow_toggle = check_policy(6)
        def switch_state_7():
            allow_toggle = check_policy(7)
        def switch_state_8():
            allow_toggle = check_policy(8)
        def switch_state_9():
            allow_toggle = check_policy(9)
        def switch_state_10():
            allow_toggle = check_policy(10)
        def switch_state_11():
            allow_toggle = check_policy(11)
        def switch_state_12():
            allow_toggle = check_policy(12)
        def switch_state_13():
            allow_toggle = check_policy(13)
        def switch_state_14():
            allow_toggle = check_policy(14)

        switch_functions = [switch_state_0,switch_state_1, switch_state_2,switch_state_3,switch_state_4,
                            switch_state_5,switch_state_6,switch_state_7,switch_state_8,switch_state_9,switch_state_10,switch_state_11,
                            switch_state_12,switch_state_13,switch_state_14]
        
        for index, machine in enumerate(constants.machines_list):
            machine_name = machine.name
            globals()["switch_"+str(machine_name)]= customtkinter.StringVar(value=machine.state_name.lower())
            self.machine_name = customtkinter.CTkSwitch(master=self.frame_left, text=machine.name,command=switch_functions[index],
                                                  variable = globals()["switch_"+str(machine_name)], onvalue="on", offvalue="off")
            self.machine_name.grid(row=index+2, column=0, pady=10, padx=20,sticky="we")
       
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

        policies = self.policyHelper.show_policies()
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text=policies,
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

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
                                                command=self.exit_window)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        # self.optionmenu_1.set("Dark")
        # self.button_3.configure(state="disabled", text="Disabled CTkButton")
        self.combobox_1.set("CTkCombobox")
        self.radio_button_1.select()
        self.slider_1.set(0.2)
        self.slider_2.set(0.7)
        self.progressbar.set(0.5)
        # self.switch_2.select()
        self.radio_button_3.configure(state=tkinter.DISABLED)
        self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        self.check_box_2.select()

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