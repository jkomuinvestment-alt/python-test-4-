class Library:
    def __init__(self):
        self.books = ["math", "science"]
        
    def borrow(self,books):
        if books in self.books:
           self.books. remove (books)
           return f"you borrow {books}"
        return "not available"
    def return_books(self,book):
       self.books.append(book)
       return f"you returned {book}"