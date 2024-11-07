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
    
    def return_json (self, type):
        if type == 'pretty':
            return self.data
        else:
            return self.dirty_data
    


    # def film (self, filmname):
    #     self.filmname = filmname
    #     if self.filmname in self.films:
    #         self.FILM = self.filmname
    #     else:
    #         return
    #     self.filmdict = self.dirty_data['location'][self.CITY]['films'][self.FILM]

    #     print (self.filmdict)








class Film:
    def __init__(self, filmname, json_file, city):
        self.json_file = json_file
        vidi = self.json_file["location"][city]["films"]
        if filmname in list(self.json_file["location"][city]["films"].keys()):
            self.name = filmname
        self.poster_path = vidi[self.name]["poster"]
        self.image_path = vidi[self.name]["images"]
        self.description = vidi[self.name]["description"]
        self.film_session = []

        sits = self.json_file["location"][city]['SITS']
        for i in sits:
            if len(sits[i]) > 0:
                print("FILM FOUUUNDDD")
                for a in sits[i]:
                    print ("HERE's a >>", a)
                    if self.name in a:
                        self.film_session.append(a)
        print (self.film_session)

        
