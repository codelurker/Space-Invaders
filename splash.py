import pygame
import load_resources
from pygame.locals import *

class start_button(pygame.sprite.Sprite):
	def __init__(self):
	    pygame.sprite.Sprite.__init__(self)
	    self.x = 400
	    self.y = 450
	    self.font = pygame.font.Font(None, 32)
	    self.text = "START"
	    self.color = 255, 255, 255
	    self.image = self.font.render(self.text, False, (self.color))
	    self.rect = self.image.get_rect()
	    self.rect.center= self.x, self.y
	def update(self):
	    self.image = self.font.render(self.text, False, (self.color))

class quit_button(pygame.sprite.Sprite):
	def __init__(self):
	    pygame.sprite.Sprite.__init__(self)
	    self.x = 400
	    self.y = 550	    
	    self.font = pygame.font.Font(None, 32)
	    self.text = "QUIT"
	    self.color = 255, 255, 255
	    self.image = self.font.render(self.text, False, (self.color))
	    self.rect = self.image.get_rect()
	    self.rect.center= self.x, self.y
	def update(self):
	    self.image = self.font.render(self.text, False, (self.color))

class highscore_button(pygame.sprite.Sprite):
	def __init__(self):
	    pygame.sprite.Sprite.__init__(self)
	    self.x = 400
	    self.y = 500
	    self.font = pygame.font.Font(None, 32)
	    self.text = "HIGH SCORES"
	    self.color = 255, 255, 255
	    self.image = self.font.render(self.text, False, (self.color))
	    self.rect = self.image.get_rect()
	    self.rect.center= self.x, self.y
	def update(self):
	    self.image = self.font.render(self.text, False, (self.color))
def show_splash(screen):
    s = start_button()
    q = quit_button()
    h = highscore_button()
    sprites= pygame.sprite.RenderUpdates(s, q, h)
    clock = pygame.time.Clock()
    splash = True
    bg_image= pygame.image.load("graphics/splash/background.png").convert()
    screen.blit(bg_image, (0, 0))
    pygame.display.flip()
    title = load_resources.load_image("graphics/splash/title.png", -1)
    points = load_resources.load_image("graphics/splash/points.png", -1)
    screen.blit(title, (250, 50))
    screen.blit(points, (290, 250))
    pygame.display.flip()
    play = True
    file = "code/highscores.txt"
    while splash:
	for event in pygame.event.get():
	    if event.type == QUIT:
		splash = False
		play = False
	    if event.type == pygame.KEYDOWN:		
		if event.key== K_q:
		    splash = False
		    play = False
		elif event.key== K_ESCAPE:
		    splash = False
		    play = False
	    if event.type == MOUSEBUTTONDOWN:
		x, y = event.pos
		distance_s= ((x - s.x)**2 + (y - s.y)**2)** 0.5
		if distance_s < 25:
		    splash = False
		distance_q= ((x - q.x)**2 + (y - q.y)**2)** 0.5
		if distance_q < 20:
		    splash = False
		    play = False
		distance_h= ((x - h.x)**2 + (y - h.y)**2)** 0.5
		if distance_h < 25:
		    pass
	    if event.type == MOUSEMOTION:
		x, y = event.pos
		distance_s= ((x - s.x)**2 + (y - s.y)**2)** 0.5
		if distance_s < 25:
		    s.color= 0, 255, 0
		else:
		    s.color= 255, 255, 255
		distance_q= ((x - q.x)**2 + (y - q.y)**2)** 0.5
		if distance_q < 20:
		    q.color= 0, 255, 0
		else:
		    q.color= 255, 255, 255
		distance_h= ((x - h.x)**2 + (y - h.y)**2)** 0.5
		if distance_h < 25:
		    h.color= 0, 255, 0
		else:
		    h.color= 255, 255, 255
	sprites.clear(screen, bg_image) 
	sprites.update()
	rectlist = sprites.draw(screen)
	pygame.display.update(rectlist) 
	clock.tick(15)
    return play
