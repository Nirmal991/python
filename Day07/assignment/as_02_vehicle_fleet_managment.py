class Vehcile:
    def __init__(self, make: str, model: str, fuel_capacity: float):
        self.make = make
        self.model = model
        self.fuel_capacity = fuel_capacity

    def calculate_range(self, fuel_efficiency):
        vehicle_range = self.fuel_capacity * fuel_efficiency 
        return vehicle_range

    def get_description(self):
        return f"Vehicle: <{self.make}> <{self.model}>"


class Drivertruck(Vehcile):
    def __init__(self, make: str, model: str, fuel_capacity: float, cargo_load: float):
        super().__init__(make, model, fuel_capacity)
        self.cargo_load = cargo_load

    def calculate_range(self,fuel_efficiency):
        base_range = super().calculate_range(fuel_efficiency)
        adjusted_range = base_range * (1.0 - 0.1 * self.cargo_load)
        return adjusted_range

    def get_descripton(self):
        return f"Truck: {self.make} {self.model} carrying {self.cargo_load} tons"

        