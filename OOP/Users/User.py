from Interfaces.Authenticatable import Authenticatable


class User(Authenticatable):
  def __init__(self, name, email, password, role):
    self.name = name
    self.email = email
    self.password = password
    self.roll = role

  def login(self):
    print(f"User '{self.name}' logged in.")

  def logout(self):
    print(f"User '{self.name}' logged out.")
