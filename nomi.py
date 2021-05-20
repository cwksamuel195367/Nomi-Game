import random

class Nomi():

  def __init__(self, name, type, hp, att_speed, att, energy, defense, mood, moveSet):
    self.name = name
    self.type = type
    self.hp = hp
    self.att_speed = att_speed
    self.att = att
    self.energy = energy
    self.defense = defense
    self.mood = mood
    self.moveSet = moveSet

class Move():
  def __init__(self, name, power, consumption, priority, moody, mood):
    self.name = name
    self.power = power
    self.consumption = consumption
    self.priority = priority
    self.moody = moody
    if (self.moody == mood):
      self.bonus = 1.2
    else:
      self.bonus = 1.0

class Tail_Slap(Move):
  def __init__(self, mood):
    Move.__init__(self, "Tail Slap", 20, 10, 0, "Angry", mood)

class Punch(Move):
  def __init__(self, mood):
    Move.__init__(self, "Punch", 15, 10, 0, "irritated", mood)

class Stern_Glare(Move):
  def __init__(self, mood):
    Move.__init__(self, "Stern Glare", 1, 5, 0, "Calm", mood)

class Golf(Move):
  def __init__(self, mood):
    Move.__init__(self, "Golf", 0, 10, 0, "Vacation", mood)

class Wide_Chomp(Move):
  def __init__(self, mood):
    Move.__init__(self, "Wide Chomp", 13, 8, 0, "Thirst", mood)

class Spike_Slash(Move):
  def __init__(self, mood):
    Move.__init__(self, "Spike_Tail_Slash", 25, 25, 0, "Angry", mood)

class Sniper_Vomit(Move):
  def __init__(self, mood):
    Move.__init__(self, "Sniper Vomit", 15, 12, 0, "Irritated", mood)

class Raging_Jolt(Move):
  def __init__(self, mood):
    Move.__init__(self, "Raging Jolt", 18, 15, 0, "irritated", mood)

class Chomp(Move):
  def __init__(self, mood):
    Move.__init__(self, "Chomp", 15, 12, 0, "angry", mood)

class Lightning_Tornado(Move):
  def __init__(self, mood):
    Move.__init__(self, "Lightning Tornado", 25, 20, 0, "Supercharged", mood)

def calculateDamage(self, move, attack):
  bonus = move.bonus

  randMod = random.uniform(0.80, 1.20)
  crit = random.randint(1, 100)
  if crit <= 5:
    bonus += 1.0

  atkMod = bonus * randMod
  defense = self.defense

  damage = (defense)(attack + (move.power * atkMod)) - (1.5 * defense)
  self.health = self.health - damage

  if self.health < 0:
    self.health = 0