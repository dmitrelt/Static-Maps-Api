import os
import sys

import pygame as pg
import requests

pg.init()
screen = pg.display.set_mode((600, 450))


class Map:
    def __init__(self):
        super().__init__()
        self.t_lon = "39.55166106940937"
        self.t_lat = "52.604717305615324"
        self.z = 5

    def get(self):
        map_server = f"http://static-maps.yandex.ru/1.x/"
        map_params = {
            "ll": ",".join([self.t_lon, self.t_lat]),
            "z": self.z,
            "l": "map"
        }
        response = requests.get(map_server, params=map_params)

        if not response:
            print("Ошибка выполнения запроса")
            sys.exit(1)
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        screen.blit(pg.image.load(self.map_file), (0, 0))
        self.set()

    def set(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_PAGEUP] and self.z <= 20:
            self.z += 1
        if keys[pg.K_PAGEDOWN] and self.z > 0:
            self.z -= 1



map = Map()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    map.get()
    pg.display.update()
os.remove(map.map_file)
pg.quit()
sys.exit()
