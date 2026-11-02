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
        """Свойство только для чтения: доступность книги."""
        return self._is_available

    @property
    def last_read_pages(self) -> int:
        """Свойство только для чтения: количество страниц, прочитанных последним читателем."""
        return self._last_read_pages

    def borrow(self) -> None:
        """Выдать книгу."""
        if not self._is_available:
            raise ValueError("Книга уже выдана")
        self._is_available = False

    def give_back(self, pages_read: int) -> None:
        """Вернуть книгу и обновить количество прочитанных страниц."""
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


# Проверка работы из условия задачи:
if __name__ == "__main__":
    b = Book("1984", "Оруэлл", "123", 1949, 328)
    print(b.is_available)          # True
    print(b.last_read_pages)       # 0
    b.borrow()
    print(b.is_available)          # False
    
    try:
        b.borrow()                 # ValueError: книга уже выдана
    except ValueError as e:
        print(f"ValueError: {e}")
        
    try:
        b.is_available = True      # AttributeError
    except AttributeError as e:
        print(f"AttributeError: {e}")
        
    try:
        b.give_back(400)           # ValueError: в книге всего 328 страниц
    except ValueError as e:
        print(f"ValueError: {e}")
        
    print(b.is_available)          # False - книга так и осталась у читателя
    b.give_back(120)
    print(b.last_read_pages)       # 120
    print(b == Book("1984", "Оруэлл", "123", 1949, 328))   # True

    old = Book("Мы", "Замятин", "456", 1924, 224)
    print(sorted([b, old]))        # [Book('Мы', 'Замятин', '456', 1924, 224), Book('1984', 'Оруэлл', '123', 1949, 328)]
