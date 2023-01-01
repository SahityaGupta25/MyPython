# Duck Typing

class VLC:
    def play(self):
        print("Playing")

def Action(player):
    player.play()

obj1=VLC()
Action(obj1)
