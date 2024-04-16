def unic_elements(int_list: list) -> list:
    return list(set(int_list))


def prime_numbers(min_n: int, max_n: int) -> list:
    res = []
    if min_n > max_n:
        min_n, max_n = max_n, min_n
    if max_n < 2:
        return 'Нет таких чисел'
    if min_n < 2:
        min_n = 2
    for i in range(min_n, max_n+1):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            res.append(i)
    return res


class Point:

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = self.type_check(x)
        self.y = self.type_check(y)

    def type_check(self, item: float) -> float:
        if type(item) in [int, float]:
            return item
        else:
            print('Входной параметр должен быть числом')

    def set_xy(self, x: float = 0, y: float = 0) -> None:
        self.x = self.set_x(x)
        self.y = self.set_y(y)

    def set_x(self, x: float) -> None:
        self.x = self.type_check(x)

    def set_y(self, y: float) -> None:
        self.y = self.type_check(y)

    def get_xy(self) -> float:
        return [self.x, self.y]

    def dist(self, point: object) -> float:
        try:
            return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        except Exception:
            return 'Используйте класс Point'


def len_sort(str_list: list[str]) -> list[list[str]]:
    try:
        return [
            sorted(str_list, key=len),
            sorted(str_list, key=len, reverse=True)
        ]
    except Exception:
        return 'Элементы списка должны быть строками'
