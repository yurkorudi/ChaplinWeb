from funcs import *

class Film_obj:
    def __init__(self, name):
        self.name = name
        self.busy_seats = []
        self.data = get_films(self.name)
        self.session = get_sessions(film_id=self.data['film_id'])
        self.seats = get_seats(session_id = self.session['session_id'])
        for s in self.seats:
            self.busy_seats.append(s['seat_id'])
        src = get_images(id=self.data['image_id'])

        path = src['path']
        print ("___________________________________________________________________")
        print(self.session['session_datetime'])
        print ("___________________________________________________________________")
        date_time = self.session['session_datetime']

        self.data.update({'img_src': path})
        self.data.update({'date_time': date_time})


        






