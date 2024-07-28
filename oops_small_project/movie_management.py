class Movie:
    def __init__(self,title,year,genere,revenue,language):
        self.title=title
        self.year=year
        self.genere=genere
        self.revenue=revenue
        self.language=language

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.genere} , Revenue :${self.revenue}'
    
class MovieManagementSystem:
    def __init__(self):
        self.movies=[]

    def addMovie(self):
        title=input('Enter title of movie :')
        year=input('Enter the year of movie :')
        genere=input('Enter the genere of movie :')
        revenue=input('Enter the revenue of movie :')

        movie=Movie(title,year,genere,revenue)

        self.movies.append(movie)
        print(f"Movie '{movie.title}' added successfully")

    def displayMovie(self):
        if not self.movies:
            print('No movie available')
        else:
            for i,movie in enumerate(self.movies,start=1):
                print(i,movie)

    def searchMovie(self):
        title=input('Enter the title of movie :')

        for movie in self.movies:
            if movie.title == title:
                print(movie)
                return
        print('Movie not found')

    def removeMovie(self):
        title=input('Enter the title of movie :')

        for movie in self.movies:
            if movie.title == title:
                self.movies.remove(movie)
                print('Movie removed successfully')
                return
        print('Movie not found')


    def run(self):
        while True:

            print('\n Movie Management System')
            print('1.Add Movie')
            print('2.List Movie')
            print('3.Search Movie')
            print('4.Remove Movie')
            print('5.Exit')

            choice=input('Enter your choice :')

            if choice == '1':
                self.addMovie()
            elif choice == '2':
                self.displayMovie()
            elif choice == '3':
                self.searchMovie()
            elif choice == '4':
                self.removeMovie()
            elif choice == '5':
                print('Exiting')
                break

            else:
                print('Invalid choice')

if __name__=='__main__':
    system=MovieManagementSystem()
    system.run()