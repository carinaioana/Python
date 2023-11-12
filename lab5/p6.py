class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print(f"{self.title} by {self.author} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} by {self.author} has been returned.")
        else:
            print(f"{self.title} by {self.author} is not checked out.")

    def display_info(self):
        status = "checked out" if self.checked_out else "available"
        print(f"{self.title} by {self.author} - Status: {status}")


class Book(LibraryItem):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre


class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        super().__init__(title, director)
        self.duration = duration


class Magazine(LibraryItem):
    def __init__(self, title, publisher, issue_number):
        super().__init__(title, publisher)
        self.issue_number = issue_number


def main():
    book = Book("The Catcher in the Rye", "J.D. Salinger", "Fiction")
    dvd = DVD("Inception", "Christopher Nolan", "2 hours 28 minutes")
    magazine = Magazine("National Geographic", "National Geographic Society", "November 2023")

    book.display_info()
    dvd.display_info()
    magazine.display_info()

    book.check_out()
    dvd.check_out()
    magazine.check_out()

    book.return_item()
    dvd.return_item()
    magazine.return_item()

    book.display_info()
    dvd.display_info()
    magazine.display_info()


if __name__ == "__main__":
    main()
