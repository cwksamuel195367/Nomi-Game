from nomi import Nomi

class DaFish(Nomi):
  def __init__(self, name):
    Nomi.__init__(self, name, "DaFish", 100, 25, 40, 100, 50, "Neutral", ["Tail Slap", "Punch", "Stern Glare", "Golf"])

