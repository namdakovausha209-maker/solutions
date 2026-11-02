class Account:
    def __init__(self, number: str, owner: str, balance: float = 0):
        if balance < 0:
            raise ValueError("Начальный остаток не может быть отрицательным")
        
        self._number = number
        self._owner = owner
        self._balance = balance

    @property
    def number(self) -> str:
        """Номер счёта (доступен только для чтения)."""
        return self._number

    @property
    def owner(self) -> str:
        """Владелец счёта (доступен только для чтения)."""
        return self._owner

    @property
    def balance(self) -> float:
        """Текущий остаток (доступен только для чтения)."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """Положить деньги на счёт."""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Снять деньги со счёта."""
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount

    def __repr__(self) -> str:
        return f"Account({self._number!r}, {self._owner!r}, {self._balance})"


# Проверка работы из условия задачи:
if __name__ == "__main__":
    acc = Account("40817", "Иван", 1000)
    acc.deposit(500)
    print(acc.balance)          # 1500
    acc.withdraw(200)
    print(acc.balance)          # 1300
    
    try:
        acc.withdraw(5000)   # Ошибка: недостаточно средств
    except ValueError as e:
        print(f"ValueError: {e}")
        
    print(acc.balance)          # 1300 - операция ничего не испортила
    print(acc)                  # Account('40817', 'Иван', 1300)
