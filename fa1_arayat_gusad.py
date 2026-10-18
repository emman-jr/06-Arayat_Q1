class Library_Material:
    def __init__(self, __title, __author):
        self.__title = __title
        self.__author = __author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, __title):
        self.__title = __title

    def set_author(self, __author):
        self.__author = __author

class Book(Library_Material):
    def __init__(self, __title, __author, __number_of_pages):
        super().__init__(__title, __author)
        self.__number_of_pages = __number_of_pages
        #makes number of pages 1 if user inputs non-positive integer
        if __number_of_pages <= 0:
            self.__number_of_pages = 1
            print("Number of pages must be a positive integer.")

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.__number_of_pages}")

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, __number_of_pages):
        if __number_of_pages <= 0:
            print("Number of pages must be a positive integer.")
        else:
            self.__number_of_pages = __number_of_pages

class Magazine(Library_Material):
    def __init__(self, __title, __author, __issue_number):
        super().__init__(__title, __author)
        self.__issue_number = __issue_number
        #makes issue number 1 if user inputs non-positive integer
        if __issue_number <= 0:
            self.__issue_number = 1
            print("Issue number must be a positive integer.")

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.__issue_number}")

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, __issue_number):
        if __issue_number <= 0:
            __issue_number = 1
            print("Issue number must be a positive integer.")
        else:
            self.__issue_number = __issue_number

pub1 = Library_Material("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 =   Magazine("National Geographic", "Various Authors", 202)

print("Library Material Information:")
pub1.display_info()
print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())
print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())