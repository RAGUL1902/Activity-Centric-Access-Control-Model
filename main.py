import os
import time
from machines import Machine
import constants
from constants import machines_list
from policy_helper import PolicyHelper

# TODO help function
os.system('cls')

policyHelper = PolicyHelper(constants.POLICY_FILE)
print("\n\n ---------------------- COMMANDS-------------------")
print('\n show_policies() - show policies')
print('\n show_activity() - show current activity status')
print('\n help() - to print all command')
print("\n\n --------------------------------------------------")

time.sleep(2)
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
                state = 'OFF'
                if machine_iterator.state_name == "ON":
                    state = 'ON'
                print("\n" + machine_iterator.name + "     " + state)
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
                    if(val == 'ON'):
                        new_state = "ON"
                        old_state = "OFF"
                    if(itr.state_name == new_state):
                        print('\n->'+machine_name +
                              ' is already in ' + val + ' state')

                    else:
                        policyHelper.check_policy(
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
