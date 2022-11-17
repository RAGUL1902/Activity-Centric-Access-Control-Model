import policy

# TODO: Add validation for policy formats


class PolicyHelper:
    """Provides helper functions needed to interact with the Policies"""

    policy_file = ""
    policy_list = []

    def __init__(self, policy_file):
        self.policy_file = policy_file

    def add_policy(self, object_name, state_name, activity_name, pre_condition, current_condition, post_condition):
        policy_number = len(self.policy_list) + 1
        print(f"Adding new policy: {policy_number}...")
        new_policy = policy.Policy(policy_number, object_name, state_name,
                                   activity_name, pre_condition, current_condition, post_condition)
        self.policy_list.append(new_policy)
        self.update_policies_file()

    def delete_policy(self, policy_number):
        print(f"Deleting policy number: {policy_number}...")
        new_policy_list = []
        counter = 1
        for i in self.policy_list:
            if i.policy_number != policy_number:
                i.policy_number = counter
                counter += 1
                new_policy_list.append(i)
        self.policy_list = new_policy_list
        self.update_policies_file()

    def show_policies(self):
        """Displays all the policies"""
        print("\n============================= POLICIES ============================")
        f = open(self.policy_file)
        print(f.read())

    def update_policies_file(self):
        open(self.policy_file, 'w').close()
        f = open(self.policy_file, 'a+')
        for i in self.policy_list:
            policy_string = f"{i.policy_number}) < ({i.object_name}, {i.state_name}, {i.activity_name}), ({str(i.pre_condition)[1:-1]}), ({str(i.current_condition)[1:-1]}), ({str(i.post_condition)[1:-1]})) > \n"
            f.write(policy_string)
        f.close()


    def check_policy(self, machine_name, old_state, machines_list):
        
        for i in self.policy_list:
            if i.name == machine_name & i.state == old_state :
                
                pass
        pass

    