from policy_helper import PolicyHelper


policy_helper = PolicyHelper("policies.txt")
policy_helper.add_policy('a1', 'b1', 'c1', ['d1', 'e1', 'f1'], [], ['g1', 'h1', 'i1'])
policy_helper.add_policy('a2', 'b2', 'c2', ['d2', 'e2', 'f2'], [], ['g2', 'h2', 'i2'])
policy_helper.show_policies()
policy_helper.delete_policy(1)
policy_helper.show_policies()