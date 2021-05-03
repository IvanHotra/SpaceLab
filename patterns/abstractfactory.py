app,film,music = 'app','film','music'
dataBase = {app : [], music : [], film : []}
class AppStore:
    def __init__(self,dataBase = dataBase):
        self.dataBase = dataBase
    def createApp(self,app):
        self.app = app
        self.dataBase['app'].append(app)
    def createFilm(self,film):
        self.film = film
        self.dataBase['film'].append(film)
    def createMusic(self,music):
        self.dataBase['music'].append(music)

class App(AppStore):
    def __init__(self):
        AppStore.__init__(self)
    def createApp(self):
        AppStore.createApp()

class Film(AppStore):
    def __init__(self):
        AppStore.__init__(self)
    def createFilm(self):
        AppStore.createFilm()
    def __str__(self):
        print(dataBase)

class Music(AppStore):
    def __str__(self):
        print(dataBase['music'])


music = Music()
music.createMusic('wwe')
music.createMusic('reoad')
print(music)