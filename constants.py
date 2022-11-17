from machines import Machine

POLICY_FILE = 'policies.txt'
#creating objects
crusher_and_grinder_1 = Machine('Crusher_and_grinder_1',0,"breakdown_chemicals")
agitator_1 = Machine('agitator_1',1,"agitate")
suction_1 = Machine('suction_1',0,'remove_gas')
suction_2 = Machine('suction_2',0,'remove_gas')
pump_1 = Machine("pump_1",0,'pump_chemicals')
pump_2 = Machine("pump_2",0,'pump_chemicals')
mixer_1 = Machine("mixer_1",0,"mix")
mixer_2 = Machine("mixer_2",0,"mix")
mixer_3 = Machine("mixer_3",0,"mix")
high_shear_mixer_1 = Machine("high_shear_mixer_1",0,'mix_with_high_shear')
conveyer_1 = Machine("conveyer_1",0,'move_chemicals')
compressor_1 = Machine("compressor_1",0,"compress")
tank_1 = Machine("tank_1",0,'store')
packing_machine_1 = Machine('packing_machine_1',0,"pack")
air_conditioner_1 = Machine("air_conditioner_1",0,'air_conditioning')

machines_list = [crusher_and_grinder_1,agitator_1,suction_1,suction_2,pump_1,pump_2,mixer_1,mixer_2,mixer_3,
                        high_shear_mixer_1,conveyer_1,compressor_1,tank_1,packing_machine_1,air_conditioner_1]
