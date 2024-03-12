from Car import Car


class ElectricCar(Car):
  """A simple attempt to represent an electric car."""

  def __init__(self, made_by, model, year):
    """Initialize attributes of the parent class."""
    super().__init__(made_by, model, year)
    self.eco_friendly = True

  def is_eco_friendly(self):
    """Check if the car is eco-friendly."""
    if self.eco_friendly:
      return f"{self.model} is eco friendly"
    else:
      return f"{self.model} is not eco friendly"

  def fill_gas_tank(self):
    return "Electric car doesn't have any gas fuel tank"


electric_car = ElectricCar("Tesla", "M404", "2024")

print(electric_car.fill_gas_tank())
