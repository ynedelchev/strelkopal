


from Object import Object;
from random import seed;
from random import random;

class Player(Object):
  def __init__(self, x, y, color, name):
    super().__init__(x, y);
    self.color = color;
    self.name = name;
    self.direction = random();
    self.health = 100.0;
