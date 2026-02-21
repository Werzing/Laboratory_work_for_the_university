

class Triangle:
    def __init__(self, name, x1, y1, x2, y2, x3, y3):
        self.name = name
        # Проверкаф, что координаты — числа
        try:
            self.vertices = [(float(x1), float(y1)),
                             (float(x2), float(y2)),
                             (float(x3), float(y3))]
        except ValueError:
            raise TypeError("Координаты должны быть числами")

    def move(self, dx, dy):
        try:
            dx = float(dx)
            dy = float(dy)
        except ValueError:
            raise TypeError("Смещение должно быть числом")
        new_vertices = []
        for x, y in self.vertices:
            new_vertices.append((x + dx, y + dy))
        self.vertices = new_vertices

    def area(self):
        x1, y1 = self.vertices[0]
        x2, y2 = self.vertices[1]
        x3, y3 = self.vertices[2]

        a = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        b = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
        c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5

        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c))**0.5
        return s

    def __str__(self):
        return f"Triangle {self.name}: {self.vertices}"


class Pentagon:
    def __init__(self, name, points):
        self.name = name
        if len(points) != 5:
            raise ValueError("Должно быть 5 вершин")
        self.vertices = []
        for pt in points:
            try:
                x, y = float(pt[0]), float(pt[1])
                self.vertices.append((x, y))
            except (ValueError, TypeError):
                raise TypeError("Каждая вершина должна быть парой чисел")

    def move(self, dx, dy):
        try:
            dx = float(dx)
            dy = float(dy)
        except ValueError:
            raise TypeError("Смещение должно быть числом")
        new_vertices = []
        for x, y in self.vertices:
            new_vertices.append((x + dx, y + dy))
        self.vertices = new_vertices

    def area(self):
        x0, y0 = self.vertices[0]
        s = 0
        for i in range(1, 4):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[i + 1]
            s += abs((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)) / 2
        return s

    def __str__(self):
        return f"Pentagon {self.name}: {self.vertices}"


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
    print("=== Задание 2: обработка ошибок ===")

    # 1. Ошибка: треугольник с буквами вместо чисел
    try:
        t = Triangle("T", "a", 0, 2, 0, 0, 2)
    except Exception as e:
        print(f"Ошибка при создании треугольника: {e}")

    # 2. Ошибка: пятиугольнику передано 4 точки
    try:
        p = Pentagon("P", [(0,0), (1,0), (2,1), (0,1)])
    except Exception as e:
        print(f"Ошибка при создании пятиугольника: {e}")

    # 3. Нормальное создание и перемещение с неверными данными
    t = Triangle("T1", 0, 0, 2, 0, 0, 2)
    p = Pentagon("P1", [(0,0), (1,0), (2,1), (1,2), (0,1)])

    try:
        t.move("пять", 5)
    except Exception as e:
        print(f"Ошибка при перемещении: {e}")

    # 4. Всё хорошо
    print("\nРабота без ошибок:")
    t.move(1, 1)
    p.move(1, 1)
    print(t)
    print(p)
    print(f"Сравнение: {compare(t, p)}")