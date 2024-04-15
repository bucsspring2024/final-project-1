import pygame

class Player:
    """
    Represents the player object
    """

    def __init__(self, x, y, img_file):
        """
        Initializes the player object
        args:
            - x : int - starting x coordinate
            - y : int - starting y coordinate
            - img_file : str - path to img file
        """

    def move_right(self):
        """
        Moves the player to the right by one unit
        args: None
        return: None
        """

    def move_left(self):
        """
        Moves the player to the left by one unit
        args: None
        return: None
        """

    def shoot(self):
        """
        Creates a bullet object
        args: None
        return: Bullet
        """


class Bullet:
    """
    Represents the bullet object
    """

    def __init__(self, x, y, img_file):
        """
        Initializes the bullet object
        args:
            - x : int - starting x coordinate
            - y : int - starting y coordinate
            - img_file : str - path to img file
        """

    def move(self):
        """
        Moves the bullet upwards
        args: None
        return: None
        """


class Controller:
    """
    Controller class to handle game logic
    """

    def __init__(self):
        """
        Initializes objects and resources required to run the program
        """
        pygame.init()

    def mainloop(self):
        """
        Main game loop
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()


def main():
    controller = Controller()
    controller.mainloop()
if __name__ == '__main__':
    main()

