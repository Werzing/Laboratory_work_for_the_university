# Простые классы треугольника и пятиугольника

class Triangle:
    def __init__(self, name, x1, y1, x2, y2, x3, y3):
        """Создаёт треугольник по трём вершинам (x,y)"""
        self.name = name
        self.vertices = [(x1, y1), (x2, y2), (x3, y3)]

    def move(self, dx, dy):
        """Перемещает треугольник на dx, dy"""
        new_vertices = []
        for x, y in self.vertices:
            new_vertices.append((x + dx, y + dy))
        self.vertices = new_vertices

    def area(self):
        """Площадь треугольника по формуле Герона (через длины сторон)"""
        #  длины сторон
        x1, y1 = self.vertices[0]
        x2, y2 = self.vertices[1]
        x3, y3 = self.vertices[2]

        a = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        b = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
        c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5

        # полупериметр
        p = (a + b + c) / 2
        # площадь
        s = (p * (p - a) * (p - b) * (p - c))**0.5
        return s

    def __str__(self):
        return f"Triangle {self.name}: {self.vertices}"


class Pentagon:
    def __init__(self, name, points):
        """
        points - список из 5 кортежей (x, y)
        """
        self.name = name
        if len(points) != 5:
            raise ValueError("Пятиугольник должен иметь 5 вершин")
        self.vertices = points[:]  # копируем список

    def move(self, dx, dy):
        new_vertices = []
        for x, y in self.vertices:
            new_vertices.append((x + dx, y + dy))
        self.vertices = new_vertices

    def area(self):
        """Площадь пятиугольника разбиением на треугольники от первой вершины"""
        # первая вершина как общую
        x0, y0 = self.vertices[0]
        s = 0
        for i in range(1, 4):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[i + 1]
            # площадь треугольника через векторное произведение
            s += abs((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)) / 2
        return s

    def __str__(self):
        return f"Pentagon {self.name}: {self.vertices}"


# Функция сравнения двух фигур по площади
def compare(fig1, fig2):
    s1 = fig1.area()
    s2 = fig2.area()
    if s1 > s2:
        return 1
    elif s1 < s2:
        return -1
    else:
        return 0


if __name__ == "__main__":
    print("=== Задание 1: простые классы ===")
    t = Triangle("T1", 0, 0, 2, 0, 0, 2)
    p = Pentagon("P1", [(0,0), (1,0), (2,1), (1,2), (0,1)])

    print("До перемещения:")
    print(t)
    print(p)
    print(f"Площадь треугольника: {t.area():.2f}")
    print(f"Площадь пятиугольника: {p.area():.2f}")

    cmp = compare(t, p)
    if cmp == 1:
        print("Треугольник больше")
    elif cmp == -1:
        print("Пятиугольник больше")
    else:
        print("Равны")

    print("\nПеремещаем оба на (3, 3):")
    t.move(3, 3)
    p.move(3, 3)
    print(t)
    print(p)
    print(f"Площади не изменились: {t.area():.2f}, {p.area():.2f}")