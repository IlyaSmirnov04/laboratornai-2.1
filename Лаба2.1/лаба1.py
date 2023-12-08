# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class People:
    """
    Документация на класс
    Класс описывает модель человека
    """
    def __init__(self, rost: float, ves: float) -> float:

        """Проверка аргументов на допустимость значений"""

        if not isinstance(rost, float):
            raise TypeError("рост человека должен быть вещественным числом")
        if rost <= 0:
            raise ValueError("рост человека должен быть положительным числом")

        """Инициализация экземпляра класса"""
        self.rost = rost

        if not isinstance(ves, float):
            raise TypeError("вес человека должен быть вещественным числом")
        if ves <= 0:
            raise ValueError("вес человека должен быть положительным числом")
        self.ves = ves

    """Метод увеличение роста человека"""
    def yvelichenie_rosta(self):
        """

        return:

        rost = yvelichenie_rosta()

        """
        ...

    """Метод изменения веса человека"""
    def izmenenie_vesa(self):
        """

         return:

        ves = izmenenie_vesa()

        """
        ...


class Milk:
    """
    Документация на класс
    Класс описывает модель Молока
    """
    def __init__(self, volume: float, drunk: float, bottle: float) -> float:
        """Проверка аргументов на допустимость значений"""

        if not isinstance(bottle, float):
            raise TypeError("объе бутылки должен быть вещественным числом")
        if bottle < 0:
            raise ValueError("объембутылки должен быть положительным числом")
        self.bottle = bottle

        if not isinstance(volume, float):
            raise TypeError("объем молока должен быть вещественным числом")
        if volume < 0 or volume > bottle:
            raise ValueError("объем молока должен быть положительным числом или не больше объема бутылки")
        self.volume = volume

        if not isinstance(drunk, float):
            raise TypeError("объем выпитого молока должен быть вещественным числом")
        if drunk < 0:
            raise ValueError("объем выпитого молока должен быть положительным числом")
        self.drunk = drunk

    """Метод выпитый объем"""
    def drunk_volume(self):
        """

        return:

        volume = drunk_volume()

        """
        ...

    """Метод оставшегося объема"""
    def ostatoc_volume(self):
        """

        return:

        ostatoc = ostatoc_volume()

        """
        ...

class Ambar:
    """
    Документация на класс
    Класс описывает модель Амбара
    """
    def __init__(self, fructs: int, ovochis: int) -> int:
        """Проверка аргументов на допустимость значений"""

        if not isinstance(fructs, int):
            raise TypeError("количество фруктов должно быть целым числом")
        if fructs < 0:
            raise ValueError("количество фруктов должно быть положительным числом")
        self.fructs = fructs

        if not isinstance(ovochis, int):
            raise TypeError("количество овощей должно быть целым числом")
        if ovochis < 0:
            raise ValueError("количество овощей должно быть положительным числом")
        self.ovochis = ovochis

    """ Метод количества фруктов при определенном изменении их числа в амбаре"""
    def count_fructs(self):
        """

        return:

        count_f = count_fructs()

        """
        ...

    """ Метод количества овощей при определенном изменении их числа в амбаре"""
    def count_ovochi(self):
        """

        return:

        count_o = count_ovochi()

        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()