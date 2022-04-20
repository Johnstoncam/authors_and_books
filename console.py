
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Cecin")
author_repository.save(author1)
author2 = Author("Johnston")
author_repository.save(author2)

book_1 = Book("How not to fuck up CodeClan", author1)
book_repository.save(book_1)
book_2 = Book("How to fuck up CodeClan", author2)
book_repository.save(book_2)
book_3 = Book("How my name thounds", author1)
book_repository.save(book_3)


# book_repository.delete(3)

