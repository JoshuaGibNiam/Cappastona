import json
class Constants:
    def __init__(self):
        self.WINDOW_HEIGHT = 800
        self.WINDOW_WIDTH = 600
        self.WINDOW_CAPTION = "Cappastona"
        self.FPS = 60
        with open('levels.json', 'r') as f:
            self.levels = json.load(f)

    def set_level(self, level: int) -> None:
        self.level = level
        self.ENEMIES = self.levels[f"lvl{self.level}"]["enemies"]