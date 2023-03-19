from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    # Создаем и заполняем нолями "массив" n*m.
    list_ = [[0] * n for i in range(m)]
    # В эти клетки можно попасть только одним маршрутом
    for i in range(n):
        list_[i][0] = 1
    # В эти тоже только одним маршрутом
    for j in range(m):
        list_[0][j] = 1
    # В остальные можно попасть из 3-х соседних
    for i in range(1, n):
        for j in range(1, m):
            list_[i][j] = list_[i][j - 1] + list_[i - 1][j] + list_[i - 1][j - 1]
    return list_
if __name__ == '__main__':
    paths = car_paths(5, 5)
    print(paths)  # 7