import random


class Player:
    health = 10
    max_health = 10
    default_damage = 10
    position = [0, 0]

    def was_hitted(self, hid):
        self.health -= hid

    def get_clear_position(self, map):
        map_height = len(map.split("\n"))
        map_width = len(map.split("\n")[0])
        while True:
            coords = [random.randint(0, map_width -1), random.randint(0, map_height - 1)]
            if map.split("\n")[coords[1]][coords[0]] == "*":
                return coords

    def wait(self):
        if not self.health == self.max_health:
            self.health += 1
        print("player`s health:", self.health)