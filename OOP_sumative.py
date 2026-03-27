class Smart_device:
    # Defining the base 3 atributers of the system
    def __init__(self, device_id, is_on, base_power_draw):
        self.__device_id = device_id
        self.__is_on = is_on
        self.__base_power_draw = base_power_draw
    
    # Returning device id if a user asks for it
    def get_device_id(self):
        return self.__device_id
    
    #Setting new device id  by owerwriting the old one 
    def set_device_id(self, device_id):
        self.__device_id = device_id
        return device_id
   
    # Returning if the smart object is on whilst also printing it's name before stating if its on or off
    def get_is_on(self):
        if self.__is_on == False:
            return f"{self.get_device_id()} It's turned off"
        else:
            return f"{self.get_device_id()} It's on"
    #The toggle switch. If its off it will turn it on and vice versa
    def Toggle_power(self):
        if self.__is_on == False:
            self.__is_on = True
        else: 
            self.__is_on = False
    
    #Returning powerd draw to the user , if the device is off it's automaticly zero
    def get_base_power_draw(self):
        if self.__is_on == False:
            return 0
        else: 
            return  {self.__base_power_draw}
    
    
    # Setting new power draw for the device
    def set_base_power_draw(self, power_draw):
        self.__base_power_draw = power_draw
        return self.__base_power_draw



#setting the smart devices
Fridge = Smart_device("Fridge", False, 10)
TV = Smart_device("TV", False, 3)
Blast_furnace = Smart_device("Blast furnace", False, 100)
# some basic testing
print(Blast_furnace.get_is_on())
Blast_furnace.Toggle_power()
print(Blast_furnace.get_is_on())
print(Blast_furnace.get_device_id())
Blast_furnace.set_device_id("Markadiusz")
print(Blast_furnace.get_base_power_draw())

Total_power = f"Total power of the system is {Blast_furnace.get_base_power_draw() + TV.get_base_power_draw() + Fridge.get_base_power_draw()}"
print(Total_power)
