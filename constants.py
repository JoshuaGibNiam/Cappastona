import json
class Constants:
    def __init__(self):
        self.WINDOW_HEIGHT = 1600
        self.WINDOW_WIDTH = 1200
        self.WINDOW_CAPTION = "Cappastona"
        self.FPS = 120
        with open('jsonfiles/levels.json', 'r') as f:
            self.levels = json.load(f)

    def set_level(self, level: int) -> None:
        self.LEVEL = level
        self.SPRITES = self.levels[f"lvl{self.LEVEL}"]
        self.ENEMIES_COUNT = len(self.SPRITES["enemies"])
        self.PLAYER = self.SPRITES["player"]
        self.ENEMIES = self.SPRITES["enemies"]
        self.WALLS = self.SPRITES["walls"]
        self.PORTAL = self.SPRITES["portal"]
