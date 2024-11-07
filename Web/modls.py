class JSN: 
    def __init__(self, json, filepath, type):
        self.filepath = filepath
        self.type = type 
        self.dirty_data = None
        print ("####################################################LALALAND##############################################################")
        with open (self.filepath, 'r') as self.file:
            self.dirty_data = json.load(self.file)
            print (self.dirty_data)
            self.data = json.dumps(self.dirty_data, indent=4)
            print (self.data)


