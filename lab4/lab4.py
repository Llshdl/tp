from abc import ABC, abstractmethod


# Стратегия (Strategy)
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass


class BubbleSort(SortingStrategy):
    def sort(self, data: list) -> list:
        for i in range(len(data)):
            for j in range(0, len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class QuickSort(SortingStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        pivot = data[0]
        less = [x for x in data[1:] if x <= pivot]
        greater = [x for x in data[1:] if x > pivot]
        return self.sort(less) + [pivot] + self.sort(greater)


class SortContext:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort(self, data: list) -> list:
        return self._strategy.sort(data)


# Цепочка обязанностей (Chain of Responsibility)
class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass


class PositiveHandler(Handler):
    def handle_request(self, request):
        if request > 0:
            return f"PositiveHandler: {request} is positive."
        elif self._successor:
            return self._successor.handle_request(request)


class NegativeHandler(Handler):
    def handle_request(self, request):
        if request < 0:
            return f"NegativeHandler: {request} is negative."
        elif self._successor:
            return self._successor.handle_request(request)


class ZeroHandler(Handler):
    def handle_request(self, request):
        if request == 0:
            return f"ZeroHandler: {request} is zero."
        elif self._successor:
            return self._successor.handle_request(request)


# Итератор (Iterator)
class CustomIterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._collection):
            result = self._collection[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


class CustomCollection:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return CustomIterator(self._items)


# Пример использования всех паттернов
if __name__ == "__main__":
    # Стратегия
    data = [5, 2, 9, 1, 5, 6]
    print("Стратегия:")
    context = SortContext(BubbleSort())
    print("Bubble Sort:", context.sort(data.copy()))

    context.set_strategy(QuickSort())
    print("Quick Sort:", context.sort(data.copy()))

    print("\nЦепочка обязанностей:")
    # Цепочка обязанностей
    handler = PositiveHandler(NegativeHandler(ZeroHandler()))
    print(handler.handle_request(10))
    print(handler.handle_request(-5))
    print(handler.handle_request(0))

    print("\nИтератор:")
    # Итератор
    collection = CustomCollection()
    collection.add_item("Item 1")
    collection.add_item("Item 2")
    collection.add_item("Item 3")

    for item in collection:
        print(item)