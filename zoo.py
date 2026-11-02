from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    @abstractmethod
    def sound(self) -> str:
        """Возвращает звук, издаваемый животным."""
        pass

    @abstractmethod
    def food_per_day(self) -> float:
        """Возвращает массу корма (в кг), необходимую животному в день."""
        pass

    def describe(self) -> str:
        """Возвращает описание животного в формате 'Имя: Звук'."""
        return f"{self.name}: {self.sound()}"


class Lion(Animal):
    def sound(self) -> str:
        return "Р-р-р"

    def food_per_day(self) -> float:
        # 5% от веса льва
        return self.weight * 0.05


class Parrot(Animal):
    def sound(self) -> str:
        return "Привет!"

    def food_per_day(self) -> float:
        # 10% от веса попугая
        return self.weight * 0.10


class Zoo:
    def __init__(self):
        self._animals = []

    def add(self, animal: Animal) -> None:
        """Добавить животное в зоопарк."""
        # Проверка, что переданный объект является экземпляром класса Animal или его наследником
        if not isinstance(animal, Animal):
            raise TypeError("В зоопарк можно добавлять только объекты типа Animal")
        self._animals.append(animal)

    def sounds(self) -> list[str]:
        """Возвращает список описаний всех животных в порядке добавления."""
        return [animal.describe() for animal in self._animals]

    def total_food(self) -> float:
        """Возвращает общее количество корма для всех животных зоопарка в день."""
        return sum(animal.food_per_day() for animal in self._animals)

    def __len__(self) -> int:
        """Возвращает общее количество животных в зоопарке."""
        return len(self._animals)


# Проверка работы из условия задачи:
if __name__ == "__main__":
    zoo = Zoo()
    zoo.add(Lion("Симба", 190))
    zoo.add(Parrot("Кеша", 0.5))
    
    print(len(zoo))               # Ожидается: 2
    print(zoo.sounds())           # Ожидается: ['Симба: Р-р-р', 'Кеша: Привет!']
    print(zoo.total_food())       # Ожидается: 9.55 (190*0.05 = 9.5; 0.5*0.1 = 0.05; 9.5 + 0.05 = 9.55)
    
    try:
        Animal("Нечто", 10)       # TypeError: создание экземпляра абстрактного класса запрещено
    except TypeError as e:
        print(f"TypeError при создании Animal: {e}")
        
    try:
        zoo.add("слон")           # TypeError: строка не является наследником Animal
    except TypeError as e:
        print(f"TypeError при добавлении строки: {e}")
