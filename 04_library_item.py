"""
You are tasked with developing a system to manage different types of media in a library.
The library contains various types of items such as books, magazines, and DVDs.
Each type of media shares some common attributes but also has specific attributes and behaviors unique to its type.
You will need multiple classes to accomplish this, with some classes inheriting from a parent class.
See example:

book = Book("The Great Gatsby", "1925", "B001", "F. Scott Fitzgerald", 218)
magazine = Magazine("National Geographic", "2021", "M001", 12, "December")
dvd = DVD("Inception", "2010", "D001", 148, "Christopher Nolan")

print(book.get_info())         # Prints book information
print(magazine.get_info())     # Prints magazine information
print(dvd.get_info())          # Prints DVD information


Once your classes are complete, copy and paste the above example below them in order to test their functionality.
"""

"""
Write a class that meets these requirements.

Name:       LibraryItem

Required state:
   * title, the title of the item
   * publication date, the date the item was published
   * identifier, a unique identifier for the item

Behavior:
   * get_info()     # Returns information about the item

"""
class LibraryItem:
   def __init__(self, title, pub_date, uniqueID):
      self.title = title
      self.pub_date = pub_date
      self.uniqueID = uniqueID

   def get_info(self):
      return f"Title: {self.title}, Publication Date: {self.pub_date}, Unique ID: {self.uniqueID}"
"""
Write a class that meets these requirements.

Name:       Book (inherits from LibraryItem)

Required state:
   * author, the author of the book
   * pages, the number of pages in the book

Behavior:
   * get_info()     # Returns information about the book, including the author and number of pages

Example:
   book = Book("The Great Gatsby", "1925", "B001", "F. Scott Fitzgerald", 218)

   print(book.get_info())    # Prints book information

"""
class Book(LibraryItem):
   def __init__(self, title, pub_date, uniqueID, author, pages):
      self.author = author
      self.pages = pages
      super().__init__(title, pub_date, uniqueID)

   def get_info(self):

      return super().get_info() + f", Author: {self.author}, Pages: {self.pages}."

"""
Write a class that meets these requirements.

Name:       Magazine (inherits from LibraryItem)

Required state:
   * issue number, the issue number of the magazine
   * month, the month the magazine was published

Behavior:
   * get_info()     # Returns information about the magazine, including the issue number and month

Example:
   magazine = Magazine("National Geographic", "2021", "M001", 12, "December")

   print(magazine.get_info())    # Prints magazine information

"""
class Magazine(LibraryItem):
   def __init__(self, title, pub_date, uniqueID, issue, month):
      self.issue = issue
      self.month = month
      super().__init__(title, pub_date, uniqueID)

   def get_info(self):

      return super().get_info() + f", Issue #: {self.issue}, Month Published: {self.month}."

"""
Write a class that meets these requirements.

Name:       DVD (inherits from LibraryItem)

Required state:
   * duration, the duration of the DVD in minutes
   * director, the director of the DVD

Behavior:
   * get_info()     # Returns information about the DVD, including the duration and director

Example:
   dvd = DVD("Inception", "2010", "D001", 148, "Christopher Nolan")

   print(dvd.get_info())    # Prints DVD information

"""
class DVD(LibraryItem):
   def __init__(self, title, pub_date, uniqueID, duration, director):
      self.duration = duration
      self.director = director
      super().__init__(title, pub_date, uniqueID)

   def get_info(self):

      return super().get_info() + f", Duration(minutes): {self.duration}, Director: {self.director}."


book = Book("The Great Gatsby", "1925", "B001", "F. Scott Fitzgerald", 218)
magazine = Magazine("National Geographic", "2021", "M001", 12, "December")
dvd = DVD("Inception", "2010", "D001", 148, "Christopher Nolan")

print(book.get_info())         # Prints book information
print(magazine.get_info())     # Prints magazine information
print(dvd.get_info())          # Prints DVD information