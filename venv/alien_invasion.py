
import sys
import pygame
from settings import Settings
def run_game():
	
 # Инициализирует игру и создает объект экрана.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
 # Запуск основного цикла игры.
	while True:
		screen.fill(ai_settings.bg_color)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.display.flip()
run_game()