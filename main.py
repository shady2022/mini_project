from pyfiglet import Figlet
from documentary import Documentary
from film import Film
from series import series
from clip import Clip
from Media import Media


def show_menu():
    print('1-add_movie')
    print('2-edit')
    print('3-delet_movie')
    print('4-search_movie')
    print('5-download_moive')
    print('6-save_and_exit')
    
movie = []

def Media_information():
    id = int(input('please enter your id:'))
    n  = input('please enter name of movie:')
    dir = input('please enter the name of director:')
    IMs = float(input('please enter your rate:'))
    url = input(' please neter url :')
    T = int(input('please enter your duration:'))
    c = input('please enter your casts: ')
    g = input('please enter your genre:')
    return id, n, dir, IMs, url, T, c, g

   


def add_movie():
    while True:
        print('1- Add Film ')
        print('2- Add Series ')
        print('3- Add Clip')
        print('4- Add Documentary')
        print('5- exit')

        choice = int(input('Please enter media want to add: '))
        if choice =='1':
            Media_information()
            Media.append(Film)
         
        elif choice == '2':
            Media_information()
            Media.append(series)
            
        elif choice == '3':
            Media_information()
            Media.append(Clip)
            
        elif choice == '4':
            Media_information()
            Media.append(Documentary)
            
        elif choice == '5':
            break
        
def load():
   
    
    try:
        f = open('database.txt', 'r')
        
    except:
        print('error! data base not found')
        
        big_text = f.read
        rows = big_text.split('\n')
             

    for i in range(len(rows)):
        info = rows[i].split(',')
        movie.append ={'id': int(info[0]), 'name':info[1], 'year':int(info[2]), 'director':info[3], 'duration':info[4],'genre':info[5]}
        show_menu()    
        f.close()
        print('movie:', movie)
        print('program is ready to use!!')
            
            
       
        
def show_edit_menu():
    print('1-name')
    print('2-year')
    print('3-director')
    print('4-duration')
    print('5-genre')
    print('6-end & exit')
    
def edit():
    Media_information()
    for i in range(len(movie)):
        if movie [i]['id'] == id:
            while True:
                show_edit_menu()
                option = int(input('please choose from edit menu:'))
                if option == 1:
                    movie[i]['name']=input('please enter new name: ')
                elif option == 2:
                    movie[i]['year']=int(input('please enter nem year: '))
                elif option == 3:
                    movie[i]['director']=input('please enter new director: ')
                elif option == 4:
                    movie[i]['duration']=int(input('please enter new duration: '))
                elif option == 5:
                    movie[i]['genre']=input('please enter new genre: ')
                elif option == 6:
                    break
                else:
                    print('value error')
                    
def delet_movie():
    id = int(input('please enter movie id: '))
    for i in range(len(movie)):
        if movie[i]['id']== id:
            movie.pop(i)
            print('movie removed sucessfully')
            
    
def search_movie():
    user_input = input('please enter id or name: ')
    for i in range(len(movie)):
        if movie[i]['name'] == user_input or str(movie[i]['id'] == user_input):
            print(movie[i])
            
            
def download_movie():
    name = input('Please enter name of madia that want to download: ')
    f=0

    for i in range(len(movie)):
        if name == movie[i].name:
            movie[i].download()
    if f == 0:
        print('This media not exist!!!')   
        
        
        
def save_and_exit():
    f = open('database1.txt', 'w')
    for i in range(len(movie)):
        rows = str(movie[i]['id'])+','+ movie[i]['name']+ ','+ int(movie[i]['year'])+str(movie[i]['director'])+ ','+int(movie[i]['duration']) + ','+str(movie[i]['genre'])+ '\n')
        f.write(rows)
        f.close()
        exit
        
        
load() 
f = Figlet(font= 'standard')
print(f.renderText('movie star'))
print('loading....')

while True:
    show_menu()
    select = int(input('please choose a number:'))
    
    if select == 1:
        add_movie()
    elif select == 2:
        edit()
    elif select ==3:
        delet_movie()
    elif select == 4:
        search_movie()
    elif select == 5:
        download_movie()
    elif select == 6:
        save_and_exit()
        
            
        
    
    
                    
                    
                    
                    
                    
                    
                    
                
                