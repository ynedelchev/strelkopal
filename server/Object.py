class Object:
  nextId = 0;
  def __init__(self, x, y):
    self.x = x;
    self.y= y;
    self.id = Object.nextId;
    Object.nextId = Object.nextId +1;

