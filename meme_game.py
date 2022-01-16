import sys

import pygame

from config import Config
from meme import Meme
from food import Food

class MemeGame:
    def __init__(self):
        pygame.init()
        self.config = Config()

        pygame.display.set_caption(self.config.game_title)

        self.screen = pygame.display.set_mode((
            self.config.screen_width,
            self.config.screen_height
        ), pygame.FULLSCREEN)

        self.meme = Meme(self)
        self.food = Food(self)
        self.running = True

    def _listen_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.meme.direction != 'j':
                        self.meme.direction = 'k'
                elif event.key == pygame.K_UP:
                    if self.meme.direction != 'k':
                        self.meme.direction = 'j'
                elif event.key == pygame.K_LEFT:
                    if self.meme.direction != 'l':
                        self.meme.direction = 'h'
                elif event.key == pygame.K_RIGHT:
                    if self.meme.direction != 'h':
                        self.meme.direction = 'l'
                elif event.key == pygame.K_SPACE:
                    self.running = True

    def _update_screen(self):
        self.screen.fill(self.config.screen_bg_color)
        
    def run_game(self):
        while True:
            pygame.time.delay(100)
            self._listen_event()
            self._update_screen()
            if self.running:
                self.meme.blit_meme()
                self.food.blit_food()
                self.meme.move()
                self.meme.eat_food(self.food)
                self._show_score(self.meme.len)
    
            if self.meme.is_hit_the_self() or self.meme.is_hit_the_wall():
                # die
                self.running = False

            if self.running == False:
                self.meme.reset()
                self._show_game_over()
            pygame.display.flip()

    def _show_score(self, score):
        score = score - 3
        text_color = (0, 0, 0)
        font = pygame.font.SysFont('pingfang', 50)
        score_text = font.render(f'你吃了{score}口热乎的', True, text_color)
        self.screen.blit(score_text, (20, 20))

    def _show_game_over(self):
        text_color = (0, 0, 0)
        font = pygame.font.SysFont('pingfang', 50)
        text = font.render('游戏结束，按空格键再来一把', True, text_color)
        text_rect = text.get_rect()
        text_rect.center = self.screen.get_rect().center
        self.screen.blit(text, text_rect)

    def play_sound(self, sound_name):
        sound = pygame.mixer.Sound(f'sound/{sound_name}.mp3')
        pygame.mixer.Sound.play(sound)


if __name__ == '__main__':
    meme_game = MemeGame()
    meme_game.run_game()
