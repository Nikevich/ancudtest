import logging
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

# Отрисовка прямоугольника
def drawRectangle(rectangle_data):
    x = rectangle_data.get('x')
    y = rectangle_data.get('y')
    height = rectangle_data.get('height')
    width = rectangle_data.get('width')
    color = rectangle_data.get('color', 'blue')
    if x is None or y is None or height is None or width is None:
        logging.error(f"Height or width is None in {rectangle_data.get('type')}")
        return

    rectangle = Rectangle((x, y), width, height, edgecolor=color, fill=False)
    plt.gca().add_patch(rectangle)
    logging.info(f"Add rectangle with parametres [{x}, {y}], height = {height}, width = {width}, color = {color}")
    
# Отрисовка фигуры по произвольным точкам
def drawOther(triangle_data):
    points = triangle_data.get('points')
    color = triangle_data.get('color', 'green')
    if points is None:
        logging.error(f"Points are None in {triangle_data.get('type')}")

    triangle = Polygon(points, closed=True, edgecolor=color, fill=False)
    plt.gca().add_patch(triangle)
    logging.info(f"Add figure other type {points}")