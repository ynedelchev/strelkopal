
from Bush import Bush;
from Zone import Zone;
import json;

class Map:

  def __init__(self):
    self.width = 1024;
    self.height = 768;
    self.zoneCenter = -1;
    self.zoneRadius = -1;
    self.bushes = [];
    self.walls =[];
    self.players = [];
    self.zone = None;
    self.createBushes();
    self.createWalls();
    self.createZone();


  def createBushes(self):
    bush1 = Bush(10,10, 40, 10);
    self.bushes.append(bush1);
    bush2 = Bush(100,100,400,10)
    self.bushes.append(bush2);

  def createWalls(self):
    bush1 = Bush(30,30, 40, 10);
    self.bushes.append(bush1);
    bush2 = Bush(120,130,400,10)
    self.bushes.append(bush2);

  def createZone(self, x=None, y=None, radius=None):
    if (x == None):
      x = self.width / 2;
    if (y == None):
      y = self.height /2;
    if (radius == None):
      radius = self.width*2/3;
    self.zone = Zone(x, y, radius)

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,
      sort_keys=True, indent=4)
