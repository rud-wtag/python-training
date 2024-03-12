class Car:
  """A simple attempt to represent a car."""

  def __init__(self, made_by, model, year):
    """Initialize attributes to describe a car."""
    self.made_by = made_by
    self.model = model
    self.year = year
    self.odometer_reading = 0
    self.gas_amount = 100

  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()

  def read_odometer(self):
    """Print a statement showing the car's mileage."""
    print(f"This car has {self.odometer_reading} miles on it.")

  def update_odometer(self, mileage):
    """Set the odometer reading to the given value."""
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")

  def increment_odometer(self, miles):
    """Add the given amount to the odometer reading."""
    self.odometer_reading += miles

  def fill_gas_tank(self):
    """Add the given amount to the odometer reading."""
    if self.gas_amount <= 0:
      return "please fill the tank"
    else:
      return f"your remaining fuel is {self.gas_amount}"
