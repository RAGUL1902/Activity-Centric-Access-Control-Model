import os
import time
from machines import Machine
from constants import machines_list

print("\n-------------------  STATE OF MACHINES ---------------------")
for machine_iterator in machines_list:
    machine_state = 'OFF'
    if machine_iterator.state == 1:
        machine_state = 'ON'
    print( "\n" + machine_iterator.name + "     " + machine_state +" "+ str(machine_iterator.state))
print('\n---------------------------------------------------------')

machine_name = input("Enter machine name:")
print(machine_name)

exist = False
for machine_itr in machines_list :
    if machine_itr.name == machine_name:
        exist = True
        break

if exist == False:
    print('Enter correct machine name')

val = input("Enter new state (ON/OFF) :")

new_state = 0
if(val == 'ON'):
    new_state = 1
if(machine_name.state == new_state):
    print(machine_name + ' is already in '+ val + ' state')