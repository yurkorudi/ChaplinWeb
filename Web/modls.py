from funcs import *

class Film_obj:
    def __init__(self, name):
        self.name = name
        self.data = get_films(self.name)
        src = get_images(id=self.data['image_id'])['path']
        print("______________________________________ IMG PATH ______________________________________")
        print (src)
        self.data['img_src'] : src         # type: ignore