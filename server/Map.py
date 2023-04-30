
from Bush import Bush;
from Zone import Zone;
import json

from server.Wall import Wall;

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
    bush1 = Bush(0,0, 40, 10);
    self.bushes.append(bush1);
    bush2 = Bush(90,0,40,10)
    self.bushes.append(bush2);
    bush3 = Bush(0,10, 20, 10);
    self.bushes.append(bush3);
    bush4 = Bush(120,10,10,10)
    self.bushes.append(bush4);
    bush5 = Bush(0,20, 30, 10);
    self.bushes.append(bush5);
    bush6 = Bush(0,20,30,10)
    self.bushes.append(bush6);
    bush7 = Bush(0,30, 10, 10);
    self.bushes.append(bush7);
    bush8 = Bush(220,10, 10, 10)
    self.bushes.append(bush8);

  def createWalls(self):
    bush1 = Wall(30,30, 40, 10);
    self.bushes.append(bush1);
    bush2 = Wall(120,130,400,10)
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
