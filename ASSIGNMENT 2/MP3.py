from Item import Item

class MP3:
    def __init__(self, code, title, description, category, picture, quantity_in_stock, price, duration, artist):
        self.item = Item(code, title, description, category, picture, quantity_in_stock, price, duration, artist)
        self.code = code
        self.title = title
        self.description = description
        self.category = category
        self.picture = picture
        self.quantity_in_stock = quantity_in_stock
        self.price = price
        self.duration = duration
        self.artist = artist
        
        
    def playExtract(self):
        # play an extract of the MP3
        pass
        
    def download(self):
        # download the MP3
        pass
