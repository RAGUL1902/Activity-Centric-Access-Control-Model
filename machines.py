# Machine class - Parent to all Machines
class Machine:

    """
    Description - Parent class to all the machines in the factory.
    Arguments :
        name <string> - name of the machine
        state <bool> - current state of the machine on/off 
        activity <string>- the process the machine does 
    """  

    def __init__(self, name='default_machine', state="OFF", activity='defaut_activity'):
        self.name = name
        self.state_name = state
        self.activity = activity

    def change_state(self,state):
        self.state_name = state
        pass
    
    def show_state(self):

        print('\n' +self.name +' is '+ self.state_name)
    def describe(self):
        return "{self.name} does {self.activity}"


