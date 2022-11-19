import policy
import constants

# TODO: Add validation for policy formats
# TODO: read policy file and load polices into list


class PolicyHelper:
    """Provides helper functions needed to interact with the Policies"""

    policy_file = ""
    policy_list = []

    def __init__(self, policy_file):
        self.policy_file = policy_file
        self.load_policies()

    def load_policies(self):
        with open(self.policy_file) as f:
            lines = f.readlines()

        for i in lines:
            new_policy = policy.Policy()
            i = i.strip('\n').split(' ')
            for idx in range(len(i)):
                i[idx] = i[idx].strip("(),")
            new_policy.policy_number = int(i[0])
            new_policy.object_name = i[2]
            new_policy.state_name = i[3]
            new_policy.activity_name = i[4]
            new_policy.pre_condition = list([i[5], i[6], i[7]])
            new_policy.current_condition = list([i[8], i[9], i[10]])
            new_policy.post_condition = list([i[11], i[12], i[13]])
            self.policy_list.append(new_policy)

    def add_policy(self, object_name, state_name, activity_name, pre_condition, current_condition, post_condition):
        policy_number = len(self.policy_list) + 1
        print(f"Adding new policy: {policy_number}...")
        new_policy = policy.Policy(policy_number, object_name, state_name,
                                   activity_name, pre_condition, current_condition, post_condition)
        self.policy_list.append(new_policy)
        self.update_policies_file()

    def delete_policy(self, policy_number):

        # TODO check policy exist before deleting
        print(f"Deleting policy number: {policy_number}...")
        new_policy_list = []
        counter = 1
        for i in self.policy_list:
            if i.policy_number != int(policy_number):
                i.policy_number = counter
                counter += 1
                new_policy_list.append(i)
        self.policy_list = new_policy_list
        self.update_policies_file()

    def check_policy(self, machine, old_state, new_state):
        for i in self.policy_list:
            if (i.object_name == machine and i.state_name == new_state):
                pre_condition = i.pre_condition
                current_condition = i.current_condition
                post_condition = i.post_condition

                pre = False
                curr = False
                post = False

                if pre_condition[0] == '-':
                    pre = True
                if current_condition[0] == '-':
                    curr = True
                if post_condition[0] == '-':
                    post = True
                for j in constants.machines_list:
                    if (j.name == pre_condition[0] and j.state_name == pre_condition[1]):
                        pre = True
                    if (j.name == current_condition[0] and j.state_name == current_condition[1]):
                        curr = True
                    if (j.name == post_condition[0] and j.state_name == post_condition[1]):
                        post = True
                if (pre == True and curr == True and post == True):

                    for k in constants.machines_list:
                        if (k.name == machine and k.state_name == old_state):
                            k.change_state(new_state)
                            print('\n->MACHINE STATE CHANGED to ' +
                                  new_state + '\n')
                            return 1

                else:
                    print("\n POLICY DOESN'T ALLOW THIS CHANGE")
                    return 0

    def get_policies(self):
        """Displays all the policies"""
        print("\n============================= POLICIES ============================")
        f = open(self.policy_file)
        policies = f.read()
        return policies

    def update_policies_file(self):
        open(self.policy_file, 'w').close()
        f = open(self.policy_file, 'a+')
        for i in self.policy_list:
            pre_condition = "(),"
            current_condition = "(),"
            post_condition = "()"
            object_info = f"({i.object_name}, {i.state_name}, {i.activity_name}),"

            if len(i.pre_condition) > 0:
                pre_condition = f"({i.pre_condition[0]}, {i.pre_condition[1]}, {i.pre_condition[2]}),"
            if len(i.current_condition) > 0:
                current_condition = f"({i.current_condition[0]}, {i.current_condition[1]}, {i.current_condition[2]}),"
            if len(i.post_condition) > 0:
                post_condition = f"({i.post_condition[0]}, {i.post_condition[1]}, {i.post_condition[2]})"

            policy_string = f"{i.policy_number}) < {object_info} {pre_condition} {current_condition} {post_condition} > \n"
            f.write(policy_string)
        f.close()
