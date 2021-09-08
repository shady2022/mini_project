from Media import Media


class Actor(Media):
    def __init__(self, c):
        Media().__init__(self, c)
        self.actor = c
        
    def Actor_list(self):
        return self.casts