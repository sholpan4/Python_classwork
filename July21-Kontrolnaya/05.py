''' Класс Point имеет свойства: x, y.
Класс Figure содержит массив точек (объектов класса Point) и методы:
        add(point) -- добавляет новую вершину к фигуре,
        perimeter() -- возвращает периметр фигуры.
    Реализовать эти классы.
'''
class Point:
    pass


class Figure:
    pass




def test_Point():
    p = Point(10,20)
    assert p.x == 10 and p.y == 20

    p = Point()
    assert p.x == 0 and p.y == 0


def test_Figure():
    triangle = Figure()
    assert triangle.perimeter() == 0

    triangle.add(Point(5,5))
    assert triangle.perimeter() == 0

    triangle.add(Point(8,5))
    assert triangle.perimeter() == 6

    triangle.add(Point(8,8))
    assert triangle.perimeter() == 6 + (9+9)**0.5

    triangle.add()
    assert triangle.perimeter() == 6 + (9+9)**0.5


test_Point()
test_Figure()