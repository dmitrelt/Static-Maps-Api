import os
import sys

import pygame
import requests

t_lon = input()
t_lat = input()
delta = input()
map_server = f"http://static-maps.yandex.ru/1.x/"
map_params = {
    "ll": ",".join([t_lon, t_lat]),
    "spn": ",".join([delta, delta]),
    "l": "map"
}
response = requests.get(map_server, params=map_params)

if not response:
    print("Ошибка выполнения запроса")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)
