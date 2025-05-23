class Player:
    def __init__(self, position=(0, 0, 0)):
        self.position = position

    def move(self, delta):
        self.position = (
            self.position[0] + delta[0],
            self.position[1] + delta[1],
            self.position[2] + delta[2]
        )