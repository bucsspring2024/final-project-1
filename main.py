import pygame
import sys
import random

class Player(pygame.sprite.Sprite):
    """
    Represents the player object
    """

    def __init__(self):
        """
        Initializes the player object
        """
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 580
        self.speed = 5

    def update(self):
        """
        Updates the player's position
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800


class Bullet(pygame.sprite.Sprite):
    """
    Represents the bullet object
    """

    def __init__(self, x, y):
        """
        Initializes the bullet object
        """
        super().__init__()
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        """
        Moves the bullet upwards
        """
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    """
    Represents the enemy object
    """

    def __init__(self):
        """
        Initializes the enemy object
        """
        super().__init__()
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800 - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)

    def update(self):
        """
        Updates the enemy's position
        """
        self.rect.y += self.speedy
        if self.rect.top > 600:
            self.rect.x = random.randrange(0, 800 - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 5)


class Game:
    """
    Controller class to handle game logic
    """

    def __init__(self):
        """
        Initializes objects and resources required to run the program
        """
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False

    def new_enemy(self):
        """
        Creates a new enemy and adds it to the sprites group
        """
        enemy = Enemy()
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def handle_events(self):
        """
        Handles pygame events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shoot_bullet()

    def shoot_bullet(self):
        """
        Creates a bullet object and adds it to the bullets group
        """
        bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

    def update(self):
        """
        Updates game state
        """
        self.all_sprites.update()

        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        for hit in hits:
            self.score += 10
            self.new_enemy()

        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            self.game_over = True

    def draw(self):
        """
        Draws game objects on the screen
        """
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(self.score), 18, (255, 255, 255), 10, 10)
        if self.game_over:
            self.draw_text("Game Over", 48, (255, 0, 0), 250, 250)
            pygame.display.flip()
            pygame.time.delay(2000)
            self.__init__()  
        pygame.display.flip()

    def draw_text(self, text, size, color, x, y):
        """
        Helper function to draw text on the screen
        """
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def mainloop(self):
        """
        Main game loop
        """
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  


def main():
    game = Game()
    game.new_enemy()  
    game.mainloop()

if __name__ == '__main__':
    main()

