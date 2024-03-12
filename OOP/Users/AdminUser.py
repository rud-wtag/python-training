from User import User


class AdminUser(User):
  def __init__(self, name, email, password, role="Admin"):
    super().__init__(name, email, password)
    self.role = role

  def login(self):
    print(f"Admin '{self.name}' logged in.")
