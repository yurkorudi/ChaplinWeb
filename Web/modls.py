from werkzeug.datastructures import ImmutableMultiDict


class JSN: 
    def __init__(self, json, filepath, type):
        self.filepath = filepath
        self.type = type 
        self.dirty_data = None
        print ("####################################################LALALAND##############################################################")
        with open (self.filepath, 'r') as self.file:
            self.dirty_data = json.load(self.file)
            self.data = json.dumps(self.dirty_data, indent=4)
            print ("####################################################LALALAND##############################################################")
            self.cities = list(self.dirty_data['location'].keys())
            print (self.cities)



    def city (self, cityname):
        self.cityname = cityname
        if self.cityname in self.cities:
            self.CITY = self.cityname
        else:
            return
        print (self.CITY)
        self.films = list(self.dirty_data['location'][self.CITY]['films'].keys())
        print (self.films)
        return self.films
    

    def film (self, filmname):
        self.filmname = filmname
        if self.filmname in self.films:
            self.FILM = self.filmname
        else:
            return
        self.filmdict = self.dirty_data['location'][self.CITY]['films'][self.FILM]

        print (self.filmdict)


