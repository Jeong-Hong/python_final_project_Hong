from models.base_book import Book

class PaperBook(Book):
    def __init__(self, name, writer, isbn, pages):
        super().__init__(name,writer,isbn)
        self.pages = pages

    def __str__(self):
        base = super().__str__()
        return f"{base}, pages: {self.pages}"


class EBook(Book):
    def __init__(self,name, writer, isbn, volume):
        super().__init__(name, writer, isbn)
        self.volume = volume

    def __str__(self):
        base = super().__str__()
        return f"{base}, volume: {self.volume}"