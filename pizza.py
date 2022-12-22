from typing import List, Dict


class Pizza:
    AVLBL_SIZES = ['L', 'XL']
    DEFAULT_SIZE = 'L'

    def __init__(self, name: str, recipe: List[str], size: str) -> None:
        self.size = size
        self.name = name
        self.recipe = recipe

    def __eq__(self, obj: 'Pizza') -> bool:
        if isinstance(obj, Pizza):
            return all([
                self.name == obj.name,
                self.recipe == obj.recipe,
                self.size == obj.size,
            ])
        return False

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value: str) -> None:
        if value in self.AVLBL_SIZES:
            self._size = value
        else:
            print(f'Incorrect Pizza size. Set default: {self.DEFAULT_SIZE}')
            self._size = self.DEFAULT_SIZE

    def dict(self) -> Dict[str, List[str]]:
        """
        Возвращает словарь из названия и рецепта
        """
        return {self.name: self.recipe}


if __name__ == '__main__':
    m = Pizza('Margherita', [
        'tomato sauce', 'mozzarella', 'tomatoes'], 'XL')
    p = Pizza('Pepperoni', [
        'tomato sauce', 'mozzarella', 'pepperoni'], 'XL')
    h = Pizza('Hawaiian', [
        'tomato sauce', 'mozzarella', 'chicken', 'pineapples'], 'L')
    print(m.size)
    print(m.dict().popitem())
    print(m == p)
