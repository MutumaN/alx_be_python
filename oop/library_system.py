class Book:
    def __init__(self, title, author):
        """Initialize base Book with title and author."""
        self.title = title
        self.author = author

    def get_info(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file_size."""
        super().__init__(title, author)  # Call parent class constructor
        self.file_size = file_size

    def get_info(self):
        """Return string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page_count."""
        super().__init__(title, author)  # Call parent class constructor
        self.page_count = page_count

    def get_info(self):
        """Return string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)
        print(f"Added: {book.title}")

    def list_books(self):
        """Print details of each book in the library."""
        print("\nLibrary Collection:")
        print("-" * 30)
        for book in self.books:
            print(book.get_info())
        print("-" * 30)