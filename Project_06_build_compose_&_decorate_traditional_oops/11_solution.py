class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

b1 = Book("Think and Grow Rich", "Napolean Hill")
b2 = Book("Atomic Habits", "James Clear")

print("Total books added:", Book.get_total_books())