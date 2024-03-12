from Interfaces.Authenticatable import Authenticatable


class User(Authenticatable):
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def login(self):
    print(f"User '{self.name}' logged in.")

  def logout(self):
    print(f"User '{self.name}' logged out.")
