from funcs import *

class Film_obj:
    def __init__(self, name):
        self.name = name
        self.busy_seats = {}
        self.film_dates = []
        self.data = get_films(self.name)
        self.session = get_sessions(film_id=self.data['film_id'])

        for g in self.session:
            self.film_dates.append(g['session_datetime'])
            #self.busy_seats[g['session_id']] = g['']#Доробити: film_dates працює добре, потрібно лиш передати 
            #словником відповідну ід сесії дату і зробити busy_seats словником в якому передаються всі 
            # заброньовані місця відповідно до певного ід
            self.seats = get_seats(session_id = g['session_id'])
            id = g['session_id']
            for s in self.seats:
                if id not in self.busy_seats:
                    self.busy_seats[id] = []
                self.busy_seats[id].append(s['seat_id'])
                print ("___________________________________________________________________")
                print(self.busy_seats[id])
                print ("___________________________________________________________________")
        
        src = get_images(id=self.data['image_id'])

        path = src['path']
        
        #date_time = self.session['session_datetime']

        self.data.update({'img_src': path})
        self.data.update({'date_time': self.film_dates})
        self.data.update({'busy_seats': self.busy_seats})


        






