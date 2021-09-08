import pytube

class Media:
    def __init__(self, id, n, dir, IMs, url, t, c, g):
        self.id = id
        self.name = n
        self.director = dir
        self.IMDB_score = IMs
        self.url = url
        self.duration = t
        self.casts= c
        self.genre = g
        
    def show(self):
        print('id':int({self.id}), 'n':{self.name}, 'dir':{self.director}, 'Is':int({self.IMDB_score}), 'url':{self.url}, 't':int({self.duration}), 'c':{self.casts}, 'g':{self.genre})  )
        
        
    def showInfo(self):
        for i in range(self.movie):
            i.show()
            
        self.menu()
        
    def download(self):
        link = self.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path = './' , filename = 'test.mp4')
        
    