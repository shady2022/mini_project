from pyfiglet import Figlet
from actor import Actor
from documentary import Documentary
from film import Film
from series import series
from clip import Clip
from Media import Media


class Main():
    def __init__(self):

        try:
            f = open('database.txt', 'r')
        
        except:
            print('error! data base not found')
        
        big_text = f.read
        rows = big_text.split('\n')
    
        self.movie = []
    
        for i in range(len(rows)):
            info = rows[i].split(',')
            self.movie.append ={'id': int(info[0]), 'name':info[1], 'year':int(info[2]), 'director':info[3], 'duration':info[4],'genre':info[5]}
            
            f.close()
            print('movie:', self.movie)
            print('program is ready to use!!')
            self.show_menu()
            
            

    def load(self):
        f = Figlet(font= 'standard')
        print(f.renderText('movie star'))
        print('loading....')
            
            
            
    load()            
            

    def add_movie(self):

        id = int(input('please enter your id:'))
        n = input('please enter name of movie:')
        dir = input('please enter the name of director:')
        IMs = float(input('please enter your rate:'))
        url = input(' please neter url :')
        T = int(input('please enter your duration:'))
        c = input('please enter your casts: ')
        g = input('please enter your genre:')
        return id, n, dir, IMs, url, T, c, g
    
    
    def add_media():
        while True:
        print('1- Add Film ')
        print('2- Add Series ')
        print('3- Add Clip')
        print('4- Add Documentary')
        print('5- exit')

        choice = int(input('Please enter media want to add: '))
        if choice == 1:
            print('Please enter film information: ')
            inf = add_movie()
            ci = input('Cinema to release a movie: ')
            film = Film.Film('Film: ', inf[0], inf[1], inf[2], inf[3], inf[4], inf[5], ci)
            MEDIAS.append(film)

        elif choice == 2:
            print('Please enter series information: ')
            inf = add_moive()
            sec = int(input('section: '))
            seo = int(input('season: '))
            series = Series.Series('Series: ', inf[0], inf[1], inf[2], inf[3], inf[4], inf[5], sec , seo)
            MEDIAS.append(series)

        elif choice == 3:
            print('Please enter clip information: ')
            inf = get_Media_information()
            s = input('shortened from: ')
            clip = Clip.Clip('Clip: ', inf[0], inf[1], inf[2], inf[3], inf[4], inf[5], s)
            MEDIAS.append(clip)

        elif choice == 4:
            print('Please enter documentary information: ')
            inf = get_Media_information()
            t = input('A truth taken from: ')
            documentary = Documentary.Documentary('Documentary: ', inf[0], inf[1], inf[2], inf[3], inf[4], inf[5], t)
            MEDIAS.append(documentary)

        elif choice == 5:
            print('Medias add. ')
            break

        else:
            print('Wrong choice! Try again. ')
           
    
        
        
        
        
def show_menu(self):
        while True:
           print('1-add movie:')
           print('2-edit movie:')
           print('3-delet movie:')
           print('4-search movie:')
           print('5-EXIT:')
       
           

    
    
        

    
        
        
  
            



        
        

    
    

        


        
    
                            

                                