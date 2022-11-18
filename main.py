import os
import time
from machines import Machine
import constants
from constants import machines_list
from policy_helper import PolicyHelper

# TODO help function
os.system('cls')


POLICY_FILE = 'policies.txt'
# creating objects
# crusher_and_grinder_1 = Machine(
#     'crusher_and_grinder_1', "OFF", "breakdown_chemicals")
# agitator_1 = Machine('agitator_1', "OFF", "agitate")
# suction_1 = Machine('suction_1', "OFF", 'remove_gas')
# suction_2 = Machine('suction_2', "OFF", 'remove_gas')
# pump_1 = Machine("pump_1", "OFF", 'pump_chemicals')
# pump_2 = Machine("pump_2", "OFF", 'pump_chemicals')
# mixer_1 = Machine("mixer_1", "OFF", "mix")
# mixer_2 = Machine("mixer_2", "OFF", "mix")
# mixer_3 = Machine("mixer_3", "OFF", "mix")
# high_shear_mixer_1 = Machine(
#     "high_shear_mixer_1", "OFF", 'mix_with_high_shear')
# conveyer_1 = Machine("conveyer_1", "OFF", 'move_chemicals')
# compressor_1 = Machine("compressor_1", "OFF", "compress")
# tank_1 = Machine("tank_1", "OFF", 'store')
# packing_machine_1 = Machine('packing_machine_1', "OFF", "pack")
# air_conditioner_1 = Machine("air_conditioner_1", "OFF", 'air_conditioning')

# machines_list = [crusher_and_grinder_1, agitator_1, suction_1, suction_2, pump_1, pump_2, mixer_1, mixer_2, mixer_3,
#                  high_shear_mixer_1, conveyer_1, compressor_1, tank_1, packing_machine_1, air_conditioner_1]

from tkinter import *
from tkinter import messagebox
from importlib import reload
# from constants import machines_list
master = Tk()

master.title("Activity Centric Access Control Model")
def show_state():
   for index, machine_iterator in enumerate(machines_list):
      Label(master,text=machine_iterator.name).grid(row=index+1)
      Label(master,text="----->").grid(row=index+1,column=1)
      Label(master,text=machine_iterator.state_name).grid(row=index+1,column=2)
#       machine_iterator.show_state()
#    print("=========================================================================\n")
#    master.after(1000, show_state)

def show_policy():
    policy = Text(master, height=100, width=100)
    #policy.pack()
    policy.grid(column=5)
    filename='policies.txt'
    with open(POLICY_FILE, 'r') as f:
      policy.insert(END, f.read())
    # master.after(1000, show_policy)

# reload(constants)
show_state()
show_policy()
mainloop()

# ==========================================================================================================================================

policyHelper = PolicyHelper(POLICY_FILE)
print("\n\n ---------------------- COMMANDS-------------------")
print('\n show_policies() - show policies')
print('\n show_activity() - show current activity status')
print('\n help() - to print all command')
print("\n\n --------------------------------------------------")

# time.sleep(2)
while 1:

    show_state()
    show_policy()

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
            l1 = input('\n-> Enter concurrent condition machine activity :')

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

            policy_no = input("\n-> Enter policy number you want to delete :")
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

        # time.sleep(5)
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
            print("\n-------------------  CHANGE MACHINE STATE ---------------------")
            machine_name = input("\n->Enter machine name:")
            val = input("\n->Enter new state (ON/OFF) :")

            machine_exist = False
            for itr in machines_list:
                if itr.name == machine_name:
                    machine_exist = True
                    old_state = "OFF"
                    new_state = "ON"
                    if (val == 'ON'):
                        new_state = "ON"
                        old_state = "OFF"
                    if (itr.state_name == new_state):
                        print('\n->'+machine_name +
                              ' is already in ' + val + ' state')

                    else:
                        machines_list = policyHelper.check_policy(
                            machine_name, old_state, new_state, machines_list)
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
    #policyHelper = PolicyHelper(constants.POLICY_FILE)
    time.sleep(5)

    os.system('cls')


# =======================================================================================================

