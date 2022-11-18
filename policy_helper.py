import policy

# TODO: Add validation for policy formats


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
            new_policy.source_name = i[3]
            new_policy.activity_name = i[4]
            new_policy.pre_condition = list([i[5], i[6], i[7]])
            new_policy.current_condition = list([i[8], i[9], i[10]])
            new_policy.post_condition = list([i[11], i[12], i[13]])
            self.policy_list.append(new_policy)

    def add_policy(self, object_name, source_name, activity_name, pre_condition, current_condition, post_condition):
        policy_number = len(self.policy_list) + 1
        print(f"Adding new policy: {policy_number}...")
        new_policy = policy.Policy(policy_number, object_name, source_name,
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

    def check_policy(self, machine, user, state):

        pass

    def show_policies(self):
        """Displays all the policies"""
        print("\n============================= POLICIES ============================")
        f = open(self.policy_file)
        print(f.read())

    def update_policies_file(self):
        open(self.policy_file, 'w').close()
        f = open(self.policy_file, 'a+')
        for i in self.policy_list:
            pre_condition = "(),"
            current_condition = "(),"
            post_condition = "()"
            object_info = f"({i.object_name}, {i.source_name}, {i.activity_name}),"

            if len(i.pre_condition) > 0:
                pre_condition = f"({i.pre_condition[0]}, {i.pre_condition[1]}, {i.pre_condition[2]}),"
            if len(i.current_condition) > 0:
                current_condition = f"({i.current_condition[0]}, {i.current_condition[1]}, {i.current_condition[2]}),"
            if len(i.post_condition) > 0:
                post_condition = f"({i.post_condition[0]}, {i.post_condition[1]}, {i.post_condition[2]})"

            policy_string = f"{i.policy_number}) < {object_info} {pre_condition} {current_condition} {post_condition} > \n"
            f.write(policy_string)
        f.close()
