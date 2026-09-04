class SmartThermostat:
    MIN_TEMP = 10.0
    MAX_TEMP = 35.0

    def __init__(self, appliance_name: str, target_temp = 22.0):
        self.__appliance_name  = appliance_name

        if self.MIN_TEMP <= target_temp <= self.MAX_TEMP:
            self.__target_temp = target_temp
        else:
            self.__target_temp = 22.0

    
    @property
    def appliance_name(self):
        return self.__appliance_name

    @property
    def target_temp(self):
        return self.__target_temp


    @target_temp.setter
    def target_temp(self, temp):
        if not isinstance(temp, float):
            raise ValueError("Temperature must be a float")

        if not self.MIN_TEMP <= temp <= self.MAX_TEMP:
            raise ValueError(
            "Temperature must be between 10.0 and 35.0 degrees."
        )

        self.__target_temp = temp

    


thermostat = SmartThermostat("Living Room AC", 24.0)

print(thermostat.appliance_name)
print(thermostat.target_temp)

thermostat.target_temp = 28.0

print(thermostat.target_temp)

