"""Случайное блуждание"""
"""Случайным блужданием (random walk) называется путь, который не имеет четкого направления, но определяется серией полностью случайных решений."""

import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    """Класс для генерирования случайных блужданий"""

    def __init__(self, num_points=80000):
        """Инициализирут атрибуты блуждания."""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания."""
        # Шаги генерируются до достижения нужной длины.
        while len(self.x_values) < self.num_points:
            # Определение направления и длины перемещения.
            x_direction = choice([1, -1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Отклонение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих значений x и y.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


# Удаление осей
plt.axis('off')
# Назначение размера области просмотра.
#plt.figure(dpi=128, figsize=(10, 6))
plt.get_current_fig_manager().window.state('zoomed')
# Построение случайного блуждания и нанесение точек на диаграмму.
rw = RandomWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap='magma', s=0.5)

# Выделение первой и последней точек
plt.scatter(0, 0, c='black', edgecolors='white', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='white', edgecolors='black', s=100)

plt.show()
