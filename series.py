from Media import Media
class series(Media):
    def __init__(self, id, n, di, im, u, t, c , p):
        Media.__init__(self, id, n, di, im, u, t, c)
        self.part = p
        

