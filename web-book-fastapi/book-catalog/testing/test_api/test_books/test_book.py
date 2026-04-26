from unittest import TestCase

from api.api_v1.books.crud import BooksStorage
from schemas.book import BookCreate, BookUpdate, BookPartialUpdate, Book
from pydantic import ValidationError
from api.api_v1.books import crud


# Лаба 16
# class BookCRUDTestCase(TestCase):
#     def setUp(self):
#         self.storage = BooksStorage()
#         self.book_data = BookCreate(
#             slug="test-16",
#             title="Title",
#             description="Desc",
#             pages=100
#         )
#
#     def tearDown(self):
#         self.storage.delete_by_slug(self.book_data.slug)
#
#     def test_create_book_in_db(self):
#         db_book = self.storage.create(self.book_data)
#         self.assertEqual(db_book.slug, self.book_data.slug)
#
# class BookListTestCase(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.storage = BooksStorage()
#         cls.test_slugs = ["b1", "b2", "b3"]
#         for s in cls.test_slugs:
#             cls.storage.create(BookCreate(slug=s, title=s, description="D", pages=1))
#
#     @classmethod
#     def tearDownClass(cls):
#         for s in cls.test_slugs:
#             cls.storage.delete_by_slug(s)
#
#     def test_get_list(self):
#         books = self.storage.get()
#         self.assertGreaterEqual(len(books), 3)
#
#     def test_get_by_slug(self):
#         for s in self.test_slugs:
#             with self.subTest(slug=s):
#                 db_book = self.storage.get_by_slug(s)
#                 self.assertIsNotNone(db_book)
#                 self.assertEqual(db_book.slug, s)

# class BookCreateTestCase(TestCase):
# # Лаба 15
#     def test_book_slug_too_short(self):
#         with self.assertRaises(ValidationError):
#             BookCreate(slug="12", title="T", description="D", pages=1)
#
#     def test_book_slug_too_short_with_regex(self):
#         with self.assertRaisesRegex(ValidationError, "at least 3 characters"):
#             BookCreate(slug="a", title="T", description="D", pages=1)
#
#     def test_book_slug_too_long(self):
#         with self.assertRaises(ValidationError) as exc_info:
#             BookCreate(slug="a" * 35, title="T", description="D", pages=1)
#         self.assertEqual(exc_info.exception.errors()[0]['type'], 'string_too_long')
    # def test_book_can_be_created_from_create_schema(self) -> None:
    #     book_in = BookCreate(
    #         slug="test-book",
    #         title="The Great Gatsby",
    #         description="A novel by F. Scott Fitzgerald",
    #         pages=180
    #     )
    #     book = Book(**book_in.model_dump())
    #
    #     self.assertEqual(book_in.slug, book.slug)
    #     self.assertEqual(book_in.title, book.title)
    #
    # def test_book_create_accepts_different_slug(self) -> None:
    #     slugs = ["foobar", "bar", "r", "some-slug", "very-long-slug-over-thirty-characters", "new"]
    #
    #     for slug in slugs:
    #         with self.subTest(slug=slug, msg=f"Testing slug: {slug}"):
    #             book_in = BookCreate(
    #                 slug=slug,
    #                 title="Test Title",
    #                 description="Test Desc",
    #                 pages=100
    #             )
    #             self.assertEqual(slug, book_in.slug)





# class BookUpdateTestCase(TestCase):
#     # Самостоятельное задание: Тест полного обновления
#     def test_book_update_from_schema(self):
#         book = Book(slug="old", title="Old", description="Old", pages=10)
#
#         update_data = BookUpdate(slug="new-slug", title="New Title", description="New Desc", pages=20)
#
#         for field, value in update_data.model_dump().items():
#             setattr(book, field, value)
#
#         self.assertEqual(book.slug, "new-slug")
#         self.assertEqual(book.title, "New Title")
#
#     # Самостоятельное задание: Тест частичного обновления (пустой запрос)
#     def test_book_partial_update_remains_unchanged(self):
#         book = Book(slug="fixed", title="Stay", description="Stay", pages=50)
#         partial_update = BookPartialUpdate()
#
#
#         update_dict = partial_update.model_dump(exclude_unset=True)
#
#         for field, value in update_dict.items():
#             setattr(book, field, value)
#
#         self.assertEqual(book.title, "Stay")
#         self.assertEqual(book.pages, 50)