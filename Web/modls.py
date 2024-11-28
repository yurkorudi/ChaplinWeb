from funcs import *

class Film_obj:
    def __init__(self, name):
        self.name = name
        self.data = get_films(self.name)
        src = get_images(id=self.data['image_id'])
        print("______________________________________ FILM SRC ______________________________________")
        path = src['path']
        print (self.data)
        print (type(self.data))
        print("______________________________________________________________________________________")
        self.data.update({'img_src': path})
        print (self.data)
        print("______________________________________ IMG PATH ______________________________________")
        print (src['path'])


