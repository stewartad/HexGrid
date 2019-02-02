import pygame
from cevent import CEvent
from map import Map


from const import *


class App(CEvent):
    def __init__(self):
        super(App, self).__init__()
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.background = None
        self.hexgrid = Map(MAP_X, MAP_Y, HEXES_ACROSS * (HEX_RECT_W - HEX_H) + HEX_H, HEXES_DOWN * HEX_RECT_H + HEX_R)

        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((WIN_W, WIN_H), pygame.HWSURFACE)
        self._running = True
        self.background = pygame.Surface((WIN_W, WIN_H))
        self.background.fill(BG_BLUE)
        # self._image_surf = pygame.image.load("logo32x32.png").convert()

        self.hexgrid.draw_map(HEXES_ACROSS, HEXES_DOWN)


    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(self.background, (0, 0))

        self._display_surf.blit(self.hexgrid.image, self.hexgrid.rect)
        pygame.display.flip()

    def on_exit(self):
        self._running = False

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                # self.on_event(event)
                if event.type == pygame.QUIT:
                    self._running = False
            self.on_loop()
            self.on_render()
            self.clock.tick(60)
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()