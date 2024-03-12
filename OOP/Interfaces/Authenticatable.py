from abc import ABC, abstractmethod


class Authenticatable(ABC):
  """A abstract class for authenticatable users"""

  @abstractmethod
  def login(self):
    pass

  @abstractmethod
  def logout(self):
    pass
