from Object import Object;

class Zone(Object):
  def __init__(self, x,y, radius):
    super().__init__(x, y);
    self.radius = radius;
