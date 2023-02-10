import unittest
from exercice_2 import *

class TestBook(unittest.TestCase):
    
    def setUp(self):
        self.book = Book("Le crime de l'Orient Express", "Agatha Christie")
        self.second_book = Book("Un petit boulot", "Iain Levison")

    def test_book_init(self):
        #Verify a book cannot be create with less or more than 2 params
        self.assertRaises(TypeError, Book, "Le Crime de l'Orient Express")
        self.assertRaises(TypeError, Book)
        self.assertRaises(TypeError, Book, "Le crime de l'Orient Express", "Agatha Christie", "Troisieme argument en trop")

    def test_check_out(self):
        #Verify that a book can be check out
        self.book.check_out()
        self.assertTrue(self.book.is_checked_out)

        #Verify that we can't check out a book with one param in more
        self.assertRaises(TypeError, self.second_book.check_out, "Parametre en trop")

    def test_check_in(self):
        #Verify that a book check in function after been check out modify book state value
        self.book.check_out()
        self.assertTrue(self.book.is_checked_out)
        self.book.check_in()
        self.assertFalse(self.book.is_checked_out)

        self.assertRaises(TypeError, self.second_book.check_in, "Parametre en trop")


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.first_book = Book("Le crime de l'Orient Express", "Agatha Christie")
        self.library.add_book(self.first_book)

        self.second_book = Book("Un petit boulot", "Iain Levisson")
        self.library.add_book(self.second_book)

    def test_library_init(self):
        #Verify that you cannot create a library giving a parameter
        self.assertRaises(TypeError, Library, "Parametre en trop")

        #Verify that we can add mutliple books into one array
        for i in range(0,500):
            self.third_book = Book("One piece", "Eichiro Oda")
            self.library.add_book(self.third_book)
        self.assertEqual(len(self.library.books), 502)

    def test_add_book(self):
        
        #Verify that books are well added to library
        self.assertIn(self.first_book, self.library.books)
        self.assertIn(self.second_book, self.library.books)

        #Verify that all books initialized has been well added to library list of books
        self.assertEqual(len(self.library.books), 2)

    def test_check_out_book(self):
        #Verify the book can be check out by title from library
        self.library.check_out_book("Le crime de l'Orient Express")
        self.assertTrue(self.first_book.is_checked_out)

        #Verify the book cannot be check out by author name from library
        self.library.check_out_book("Iain Levison")
        self.assertFalse(self.second_book.is_checked_out)

    def test_check_in_book(self):
        #Verify the book can be check in after a check out using the title from the library
        self.library.check_out_book("Le crime de l'Orient Express")
        self.assertTrue(self.first_book.is_checked_out)
        self.library.check_in_book("Le crime de l'Orient Express")
        self.assertFalse(self.first_book.is_checked_out)

        #Verify the book cannot be check in by author name from the library
        self.library.check_out_book("Un petit boulot")
        self.assertTrue(self.second_book.is_checked_out)
        self.library.check_in_book("Iain Levison")
        self.assertTrue(self.second_book.is_checked_out)


class TestClient(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.first_book = Book("Le crime de l'Orient Express", "Agatha Christie")
        self.library.add_book(self.first_book)

        self.second_book = Book("Un petit boulot", "Iain Levison")
        self.library.add_book(self.second_book)

        self.client = Client("John Doe")

    def test_client_init(self):
        #Verify error case on creating clients with too much or less arguments
        self.assertRaises(TypeError, Client, "Pierre Dubois", "Michel Dubois")
        self.assertRaises(TypeError, Client)

        #Verify that other variable type can be used to create user without making bug
        other_client = Client(1)
        self.assertEqual(other_client.name, 1)

    def test_check_out_book(self):
        #Verify if the client has well added a book into his check out book list
        self.client.check_out_book(self.library, "Le crime de l'Orient Express")
        self.assertIn(self.first_book, self.client.checked_out_books)

        #Verify that no book has been added to the client check out book list by the book author name
        self.client.check_out_book(self.library, "Iain Levison")
        self.assertNotIn(self.second_book, self.client.checked_out_books)

    def test_check_in_book(self):

        #Verify that a client can check in a book that as been check out
        self.client.check_out_book(self.library, "Le crime de l'Orient Express")
        self.assertIn(self.first_book, self.client.checked_out_books)
        self.client.check_in_book(self.library, "Le crime de l'Orient Express")
        self.assertNotIn(self.second_book, self.client.checked_out_books)

        #Verify that a client cannot check in a book that he do not have without check in another one
        self.client.check_out_book(self.library, "Le crime de l'Orient Express")
        self.client.check_in_book(self.library, "Un petit boulot")
        self.assertIn(self.first_book, self.client.checked_out_books)

if __name__ == '__main__':
    unittest.main()