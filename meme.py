import pygame

class Meme():
    def __init__(self, meme_game):
        self.screen = meme_game.screen
        self.config = meme_game.config
        self.game = meme_game

        self.head = pygame.image.load(self.config.meme_head_image)
        self.head = pygame.transform.scale(self.head, self.config.meme_head_size)
        self.head_rect = self.head.get_rect()

        self.body_rect = pygame.Rect(
            0,
            0,
            self.config.meme_body_block_size,
            self.config.meme_body_block_size
        )

        self.len = 3
        self.body = [(100, 200), (130, 200), (160, 200)]

        self.head_rect.x = 160 + 15
        self.head_rect.y = 200 - 30

        self.direction = 'k' # jkhl ---> 下上左右

    def blit_meme(self):
        for item in self.body:
            self.body_rect.x = item[0]
            self.body_rect.y = item[1]
            pygame.draw.rect(self.screen, self.config.meme_body_color, self.body_rect)
        self.screen.blit(self.head, self.head_rect)

    def move(self):
        head = self.body[0]
        if self.direction == 'k':
            now_head = (head[0], head[1] + 30)
            self.body.insert(0, now_head)
            self.head_rect.x = now_head[0] - 15
            self.head_rect.y = now_head[1] + 15
        elif self.direction == 'j':
            now_head = (head[0], head[1] - 30)
            self.body.insert(0, now_head)
            self.head_rect.x = now_head[0] - 15
            self.head_rect.y = now_head[1] - 30 - 30
        elif self.direction == 'h':
            now_head = (head[0] - 30, head[1])
            self.body.insert(0, now_head)
            self.head_rect.x = now_head[0] - 30
            self.head_rect.y = now_head[1] -30
        elif self.direction == 'l':
            now_head = (head[0] + 30, head[1])
            self.body.insert(0, now_head)
            self.head_rect.x = now_head[0] + 15
            self.head_rect.y = now_head[1] - 30

        if self.len < len(self.body):
            self.body.pop()

    def eat_food(self, food):
        if self.head_rect.colliderect(food.food_rect):
            self.len += 1
            self.game.play_sound('zhenxiang')
            food.rand_food()

    def is_hit_the_self(self):
        return self.body[0] in self.body[1:]

    def is_hit_the_wall(self):
        if self.screen.get_rect().collidepoint((self.head_rect.x, self.head_rect.y)):
            return False
        else:
            return True

    def reset(self):
        self.len = 3
        self.direction = 'k'
        self.body = [(100, 200), (130, 200), (160, 200)]
