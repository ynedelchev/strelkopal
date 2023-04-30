
from Object import Object;

class Bush(Object):
  def __init__(self, x,y, width, height):
    super().__init__(x, y);
    self.width = width;
    self.height = height;
