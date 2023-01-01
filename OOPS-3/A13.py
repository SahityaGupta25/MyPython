# Duck Typing 2

class VLC:
    def play(self):
        print("Playing")

class SS_player:
    def play(self):
        print("Starting")

class MXPlayer():
    def stop(self):
        print("Stopping")

def Action(player):
    player.play()
def Action5(music):
    music.stop()

obj1=VLC()
obj2=SS_player()
obj3=MXPlayer()
Action(obj1)
Action(obj2)
Action5(obj3)