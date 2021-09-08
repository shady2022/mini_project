from Media import Media

class Documentary(Media):
    def __init__(self, id, n, dir, imdb, url, T, c):
        Media().__init__(id, n, dir, imdb, url, T, c)
        
    def show_info(self):
        return Media().showInfo()
        