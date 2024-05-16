# OOPS

'''
class Flowers():
    def __init__(self, type, petals, favoriteFlower):
        self.type = type
        self.petals = petals
        self.favoriteFlower = favoriteFlower
        self.fallenPetals = 0
        
    def setFallenPetals(self, fallenPetals):
        self.fallenPetals = fallenPetals
    def details(self):
        print(f"{self.type} DESCRIPTION\nNo. of Petals: {self.petals}\nFavorite Flower? {self.favoriteFlower}")
    def shakeFlower(self):
        print("Shaking Flower...")
        self.petals -= 2
        self.fallenPetals += 2
    def petalsCount(self):
        print(f"Petals on the flower: {self.petals}\nFallen Petals: {self.fallenPetals}")

myFavoriteFlower = Flowers(type="Violet", petals = 8, favoriteFlower = True)
rose = Flowers(type="Rose", petals = 12, favoriteFlower=False)
# rose.setFallenPetals(fallenPetals=3)
while(rose.petals > 0):
    rose.shakeFlower()
rose.petalsCount()
#'''

class Movies():
    def __init__(self, name, genre, imdb, duration) -> None:
        self.name = name
        self.genre = genre
        self.imdb = imdb
        self.duration = duration
        self.durationUnseen = duration
        self.durationSeen = 0
        self.seen = False
    def watchMovie(self, duration):
        if(self.seen == False):
            print(f"Watching {self.name} for {duration} hours...")
            self.durationUnseen -= duration
            self.durationSeen += duration
            if(self.durationSeen > self.duration):
                self.seen = True
        else:
            print("You have finished watching the movie!")
    def watchStatus(self):
        print(f"Duration of the movie seen: {self.durationSeen}\nDuration of the movie unseen: {self.durationUnseen}")
        
theGodfather = Movies(name="The Godfather", genre="Fiction, Cartel, Action", imdb=9.1, duration=3)
theGodfather.watchMovie(duration=1)
theGodfather.watchStatus()
theGodfather.watchMovie(duration=1.5)
theGodfather.watchStatus()
theGodfather.watchMovie(2)
theGodfather.watchMovie(1)
print(theGodfather.durationSeen)