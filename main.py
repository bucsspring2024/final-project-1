import pygame
from src.Controller import Controller

def main():
    pygame.init()
    pygame.display.set_mode()
    game = Controller()
    game.mainloop()

if __name__ == '__main__':
    main()
