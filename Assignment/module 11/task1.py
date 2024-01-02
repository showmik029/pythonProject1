class Publication:
    def __init__(self,name):
        self.name=name
class Book(Publication):
    def __init__(self,name,author,page_count):
        super().__init__(name)
        self.author=author
        self.page_count=page_count
    def print_information(self):
        print(f"Publication: {self.name} Book Author: {self.author} Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self,name,magazine_author):
        super().__init__(name)
        self.magazine_author = magazine_author
    def print_information(self):
        print(f"Publication: {self.name} Chef Editor: {self.magazine_author}")

p1=Magazine("Donald Duck","Aki Hyyppa")
p1.print_information()
b1=Book("Compartment No 6","Rosa Liksom",192)
b1.print_information()