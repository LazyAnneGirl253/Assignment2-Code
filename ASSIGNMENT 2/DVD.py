from Item import Item

class DVD:
    def __init__(self, code, title, description, category, picture, quantity_in_stock, price, director, certificate, list_of_actors):
        self.item = Item(code, title, description, category, picture, quantity_in_stock, price)
        self.director = director
        self.certificate = certificate
        self.list_of_actors = list_of_actors

    def play_extract(self):
        # play an extract of the DVD
        pass
        
    def download(self):
        # download the DVD
        pass
        
    def preview(self):
        # preview the DVD
        pass
