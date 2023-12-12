import random
import os

# This is to outline a TTRPG system mathmatically for proof of concept

# individual traits
# stats
# mind body spirit
# mind = int, wis, perception
# Body = str, dex, con,
# spirit = cha, insight, luck
# abilities

# statuses

# global variables
# units of speed/distance/time (sprinting/swimming/climbing)
# interpersonal actions (grappeling/opposed checks/combat)
# value of resources, money

# Other characters
# NPCs
# creatures
# how gods work


class player():
    def __init__(self):
        self.AP = 10
        self.status = {'grappled': 0, 'stunned': 0, 'dying': 0, 'confused': 0}
        self.mind = {'int': 1, 'wis': 1, 'per': 1}
        self.body = {'str': 1, 'dex': 1, 'con': 1}
        self.spirit = {'cha': 1, 'ins': 1, 'luck': 1}
        self.equiped = {'head': 'hat', 'torso': 'shirt', 'legs': 'pants',
                        'feet': 'shoes', 'left_hand': 'ring', 'right_hand': 'glove'}
        self.inventory = ('rations', 'jungle juice')

        self.runspeed = 30
        self.swimspeed = 15

    def action(self, action, other_player):
        if self.status
