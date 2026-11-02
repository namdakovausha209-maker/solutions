class Book:
    def __init__(self, title: str, author: str, isbn: str, year: int, pages: int):
        if pages <= 0:
            raise ValueError("Число страниц должно быть положительным")
        
        self._title = title
        self._author = author
        self._isbn = isbn
        self._year = year
        self._pages = pages
        
        self._is_available = True
        self._last_read_pages = 0

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def year(self) -> int:
        return self._year

    @property
    def pages(self) -> int:
        return self._pages

    @property
    def is_available(self) -> bool:
        return self._is_available

    @property
    def last_read_pages(self) -> int:
        return self._last_read_pages

    def borrow(self) -> None:
        if not self._is_available:
            raise ValueError("Книга уже выдана")
        self._is_available = False

    def give_back(self, pages_read: int) -> None:
        if self._is_available:
            raise ValueError("Книга уже находится на полке")
        if not (0 <= pages_read <= self._pages):
            raise ValueError(f"Количество прочитанных страниц должно быть от 0 до {self._pages}")
        
        self._last_read_pages = pages_read
        self._is_available = True

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self._isbn == other._isbn

    def __lt__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self._year < other._year

    def __repr__(self) -> str:
        return f"Book({self._title!r}, {self._author!r}, {self._isbn!r}, {self._year}, {self._pages})"


class Reader:
    def __init__(self, name: str):
        self.name = name
        self.books = []         # Список книг на руках
        self.pages_read = 0     # Общее число прочитанных страниц за всё время


class Library:
    def __init__(self):
        self._books = []        # Фонд библиотеки

    def add_book(self, book: Book) -> None:
        """Добавить книгу в фонд."""
        self._books.append(book)

    def find_by_isbn(self, isbn: str) -> Book | None:
        """Книга с этим ISBN или None."""
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None

    def find_by_author(self, author: str) -> list[Book]:
        """Список книг автора в порядке добавления."""
        return [book for book in self._books if book.author == author]

    def lend(self, isbn: str, reader: Reader) -> None:
        """Выдать книгу читателю."""
        book = self.find_by_isbn(isbn)
        if book is None:
            raise KeyError(f"Книги с ISBN {isbn} нет в фонде")
        
        # Метод .borrow() сам выбросит ValueError, если книга уже выдана
        book.borrow()
        reader.books.append(book)

    def take_back(self, isbn: str, reader: Reader, pages_read: int) -> None:
        """Принять книгу обратно."""
        # Ищем книгу в списке книг конкретного читателя
        target_book = None
        for book in reader.books:
            if book.isbn == isbn:
                target_book = book
                break
        
        if target_book is None:
            raise ValueError("У читателя нет этой книги")
        
        # Метод .give_back() проверяет корректность диапазона страниц.
        # Если pages_read невалидно, он выбросит ValueError, а состояние книги не изменится.
        target_book.give_back(pages_read)
        
        # Если проверка прошла успешно, обновляем данные читателя и убираем книгу
        reader.books.remove(target_book)
        reader.pages_read += pages_read

    def available(self) -> list[Book]:
        """Список книг на полке в порядке добавления."""
        return [book for book in self._books if book.is_available]

    def unfinished(self) -> list[Book]:
        """Книги, которые последний читатель бросил недочитанными."""
        return [book for book in self._books if 0 < book.last_read_pages < book.pages]

    def __len__(self) -> int:
        """Сколько всего книг в фонде."""
        return len(self._books)


# Проверка работы из условия задачи:
if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("1984", "Оруэлл", "123", 1949, 328))
    lib.add_book(Book("Скотный двор", "Оруэлл", "124", 1945, 112))
    alice = Reader("Алиса")

    lib.lend("123", alice)
    print(alice.books)                           # [Book('1984', 'Оруэлл', '123', 1949, 328)]
    print(lib.find_by_isbn("123").is_available)  # False
    print(len(lib.available()))                  # 1
    
    try:
        lib.lend("123", Reader("Боб"))           # ValueError
    except ValueError as e:
        print(f"ValueError: {e}")
        
    try:
        lib.take_back("123", alice, 500)         # ValueError: столько страниц в книге нет
    except ValueError as e:
        print(f"ValueError: {e}")
        
    print(alice.books)                           # Книга осталась: [Book('1984', 'Оруэлл', '123', 1949, 328)]
    lib.take_back("123", alice, 100)
    print(alice.books)                           # []
    print(alice.pages_read)                      # 100
    print(lib.unfinished())                      # [Book('1984', 'Оруэлл', '123', 1949, 328)]

    lib.lend("124", alice)
    lib.take_back("124", alice, 112)             # дочитала до конца
    print(alice.pages_read)                      # 212
    print(len(lib.unfinished()))                 # 1
