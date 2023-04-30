
from Game import Game;
from Player import Player;
import socket;
import json as JSON;
import time;
from threading import Thread;

class Server:
  def __init__(self, port):
    self.port = port;
    self.game = Game();


  def start(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", self.port));
    sock.listen();
    print('Server started on port ' + str(self.port) + '\n');
    while True:
        conn, addr = sock.accept();
        data = conn.recv(1024);
        message = JSON.loads(data);
        print("Message:\n");
        print (message);

        if message["type"] == "HELLO":
            print('HELLO "' + message["player"]["name"] + '" from ' + addr[0] + ':' + str(addr[1]));
            # try:
            name = message["player"]["name"];
            self.userJoining(name);
            receiveThread = Thread(target=Server.receiveEvents, args=(self,conn, name,));
            receiveThread.start();
            sendThread = Thread(target=Server.sendEvents, args=(self,conn, name,));
            sendThread.start();
            # except Exception as e:
            #    print(e);
            #    print('ERROR While trying to communicate with client from ' + addr[0] + ':' + str(addr[1]) + ' : ' + JSON.dumps(e, default=vars, indent=4))
            #    conn.close;
            #    break;
        else:
            message = {type: "Error", message: "Invlid message type. Message of type HELLO expected."}
            conn.sendall(message);
            conn.close;
            break;

  def receiveEvents(self, conn, player):
    while True:
        data = conn.recv(1024)
        if not data:
            print("END   Closing....");
            break
        message = JSON.loads(data);
        print("Received %s %s \n", message.type, JSON.dumps(message))
        if message.type == "CLOSE":
           print("CLOSE Closing...")
           break;
    time.sleep(3);
    conn.close();

  def sendEvents(self, conn, player):
    map = JSON.dumps(self.game.map, default=vars, indent=4);
    # map = self.game.map.toJSON();
    conn.sendall(bytes(map, 'utf-8'));
    time.sleep(3);
    conn.close();

  def userJoining(self, name):
    existingPlayerFound = [x for x in self.game.map.players if x.name == name]
    if (existingPlayerFound):
      raise Exception('Player with name "' + name + '" already exists in this game. Cannot add a new user with the same name ()"' + name + '").');
    player = Player(10,10,100, name);
    self.game.map.players.append(player);

if __name__ == "__main__":
    server = Server(3443);
    server.start();
