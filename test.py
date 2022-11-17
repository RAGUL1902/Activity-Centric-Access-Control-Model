from policy_helper import PolicyHelper
import constants

policyHelper = PolicyHelper(constants.POLICY_FILE)


#print(policyHelper.policy_list[0])

l = policyHelper.policy_list

i = l[0]

print(i.object_name)