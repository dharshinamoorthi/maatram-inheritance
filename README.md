# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Article:
    def _init_(self, title, page_count):
        # initialize protected attributes
        self._title = title
        self._page_count = page_count
        
    # define protected method
    def _show(self):
        # access protected attributes inside class 
        print("Article Title: ", self._title)
        print("Page Count: ", self._page_count)
        
class Author(Article):
    def _init_(self, name, title, page_count):
        Article._init_(self, title, page_count)
        self.name = name
    def display(self):
        print("Author Name: ", self.name)
        # access Article's protected method
        self._show()
        print("------------------ \n")
        
        
author = Author("dharshins", "Python", 3000)
author.display()
# access protected data
print(author._title)
