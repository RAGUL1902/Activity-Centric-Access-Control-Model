
#Crusher and Grinder
class CrusherAndGrinder:

    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.activity = "Crusher and Grinder breaks down the raw material"
    
    def _change_state(self, val):
        self.state = val


    def _show_state(self) :
        return f"{self.name} {self.state}" 

    def _describe(self):
        return self.activity

#Agitator
class Agitator:
    
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.activity = "Agitator stirs the chemicals from crusher and grinder"

    def _change_state(self, val):
        self.state = val


    def _show_state(self) :
        return f"{self.name} {self.state}" 
    
    def _describe(self):
        return self.activity
        
    
# Mixer
class Mixer:
    
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.activity = "Mixer mixes the chemicals from agitator with water and other chemicals from the pump"

    def _change_state(self, val):
        self.state = val


    def _show_state(self) :
        return f"{self.name} {self.state}" 
    
    def _describe(self):
        return self.activity
        

# High Shear Mixer
class HighShearMixer:
    
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.activity = "High Shear Mixer mixes the chemicals from agitator with water and other chemicals from the pump"

    def _change_state(self, val):
        self.state = val


    def _show_state(self) :
        return f"{self.name} {self.state}" 
    
    def _describe(self):
        return self.activity


# Pump
class Pump:
    
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.activity = "Pump pushes chemicals into mixer and high shear mixer"

    def _change_state(self, val):
        self.state = val


    def _show_state(self) :
        return f"{self.name} {self.state}" 
    
    def _describe(self):
        return self.activity
        


# Conveyer
class Conveyer:
    
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.activity = "Conveyer belt carries the chemicals from mixer to the compressors"

    def _change_state(self, val):
        self.state = val


    def _show_state(self) :
        return f"{self.name} {self.state}" 
    
    def _describe(self):
        return self.activity
        


# Compressor
class Compressor:
    
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.activity = "Compressor keeps the chemicals at high pressure"

    def _change_state(self, val):
        self.state = val


    def _show_state(self) :
        return f"{self.name} {self.state}" 
    
    def _describe(self):
        return self.activity
        

# Storage tank
class StorageTank:
    
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.activity = "Storage tanks stores the chemicals at appropriate temparature and pressure"

    def _change_state(self, val):
        self.state = val


    def _show_state(self) :
        return f"{self.name} {self.state}" 
    
    def _describe(self):
        return self.activity
        

# Packaging Machine
class PackagingMachine:
    
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.activity = "Packaging machine packs chemcicals into small plastic containers"

    def _change_state(self, val):
        self.state = val


    def _show_state(self) :
        return f"{self.name} {self.state}" 
    
    def _describe(self):
        return self.activity
        

# Air Conditioner
class AirConditioner:
    
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.activity = "Air conditioner keeps the chemicals in plastic containers in appropriate conditions before shipping"

    def _change_state(self, val):
        self.state = val


    def _show_state(self) :
        return f"{self.name} {self.state}" 
    
    def _describe(self):
        return self.activity
        
