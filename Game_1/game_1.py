import pygame
import sys
import os
import random 
import time

pygame.init()
window = pygame.display.set_mode((700,800))

explode = False
black = 0,0,0
red = (0,0,255)
font = pygame.font.SysFont(None,35)
n = 0

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("back_.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Player(pygame.sprite.Sprite):
	
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		img = pygame.image.load('__ship.png').convert_alpha()
		img2 = pygame.image.load('ship_.png').convert_alpha()
		img3 = pygame.image.load('ship__.png').convert_alpha()

		self.images = []
		self.images.append(img)
		self.images.append(img2)
		self.images.append(img3)

		self.image = self.images[0]
		self.rect  = self.image.get_rect()
		
		self.rect.x = x
		self.rect.y = y

	def move(self, direction):
		if direction == "right":
			if self.rect.right <= 700:
				self.rect.x += 12
				self.image = self.images[2]

			else:
				self.image = self.images[0]

		elif direction == "left":
			if self.rect.left >= 0:
				self.rect.x -= 12
				self.image = self.images[1]

			else:
				self.image = self.images[0]

		if direction == "center":
			self.image = self.images[0]

class Boss(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		img = pygame.image.load('boss.png').convert_alpha()
		self.images = []
		self.images.append(img)
		self.image = self.images[0]
		self.rect  = self.image.get_rect()

		self.rect.x = x
		self.rect.y = y

	def update(self):
		
		if not self.rect.y >= 0:
			self.rect.y += 1

class Alien(pygame.sprite.Sprite):	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		img = pygame.image.load('alien.png').convert_alpha()
		img1 = pygame.image.load('ship_.png').convert_alpha()

		self.images = []
		self.images.append(img)
		self.images.append(img1)

		self.image = self.images[0]
		self.rect  = self.image.get_rect()

		self.pos_list = [0,50,100,150,200,250,300,350,400,450,500,550,600,650]
		self.rand_pos = random.randint(0,13)

		self.rect.x = self.pos_list[self.rand_pos]
		self.rect.y = 0

	def update(self):

		self.rect.y += 30
		if self.rect.bottom >= 800:
			sys.exit()

class gun(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		
		img = pygame.image.load('shoot.png').convert_alpha()

		self.images = []
		self.images.append(img)

		self.image = self.images[0]
		self.rect  = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		self.rect.y -= 11
		if self.rect.top <= 0:
			self.kill()

class explosion(pygame.sprite.Sprite):
	t = 45
	exp_frame = 0
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		
		self.life = self.t
		self.exp_frame = self.exp_frame
		img1 = pygame.image.load('fire1.png').convert_alpha()
		img2 = pygame.image.load('fire2.png').convert_alpha()
		img3 = pygame.image.load('fire3.png').convert_alpha()
		img4 = pygame.image.load('fire4.png').convert_alpha()
		img5 = pygame.image.load('fire5.png').convert_alpha()
		img6 = pygame.image.load('fire6.png').convert_alpha()
		img7 = pygame.image.load('fire7.png').convert_alpha()
		img8 = pygame.image.load('fire8.png').convert_alpha()
		img9 = pygame.image.load('fire9.png').convert_alpha()
		img10 = pygame.image.load('fire10.png').convert_alpha()
		img11 = pygame.image.load('fire11.png').convert_alpha()
		img12 = pygame.image.load('fire12.png').convert_alpha()
		img13 = pygame.image.load('fire13.png').convert_alpha()
		img14 = pygame.image.load('fire14.png').convert_alpha()
		img15 = pygame.image.load('fire15.png').convert_alpha()
		img16 = pygame.image.load('fire16.png').convert_alpha()

		self.images = []

		self.images.append(img1)
		self.images.append(img2)
		self.images.append(img3)
		self.images.append(img4)
		self.images.append(img5)
		self.images.append(img6)
		self.images.append(img7)
		self.images.append(img8)
		self.images.append(img9)
		self.images.append(img10)	
		self.images.append(img11)
		self.images.append(img12)
		self.images.append(img13)
		self.images.append(img14)
		self.images.append(img15)
		self.images.append(img16)

		self.image = self.images[0]
		self.rect  = self.image.get_rect()

		self.rect.x = x
		self.rect.y = y

	def update(self):
		self.life -= 1
		# Pass through all the explosion frames
		if self.life % 3 == 0:
			self.exp_frame += 1
			self.image = self.images[self.exp_frame]

		if self.life == 0:
			self.exp_frame = 0
			self.kill()

class Bomb(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('bomb.png').convert_alpha()

		self.images = []
		self.images.append(img)

		self.image = self.images[0]
		self.rect  = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		self.rect.y += 5
		if self.rect.bottom >= 810:
			self.kill()

def score(text):
	screen_text = font.render(text, True, red)
	window.blit(screen_text,(30,30))

def main():

	p1 = Player(330, 725)
	a1 = Alien()	
	

	clock = pygame.time.Clock()

	player_list = pygame.sprite.Group()
	alien_list = pygame.sprite.Group()
	shots_list = pygame.sprite.Group()
	fire_list = pygame.sprite.Group()
	bomb_list = pygame.sprite.Group()
	boss_list = pygame.sprite.Group()
	player_list.add(p1)
	alien_list.add(a1)

	move = pygame.USEREVENT + 1
	create = pygame.USEREVENT + 2

	pygame.time.set_timer(move, 300)
	pygame.time.set_timer(create, 1500)

	shot = ""
	fire = 0
	n1 = 0
	ex = 0
	explode = False
	BackGround = Background('back_.jpg', [0,-50])
	bomb_reload = 0
	boss = False

	while True:

		keyp = pygame.key.get_pressed()

		for event in pygame.event.get():
			now = pygame.time.get_ticks()

			if event.type == pygame.QUIT:
				return False

			if event.type == move:
				alien_list.update()

			elif event.type == create:

				if not n1 > 100:
					alien_list.add(Alien())
					alien_list.add(Alien())
					alien_list.add(Alien())
				
				elif boss == False:
					boss = True
					boss_list.add(Boss(260,-240))

			#Gun cooldown						
			elif (now - fire) >= 250:
				 if keyp[pygame.K_SPACE]:
				 	shots_list.add(gun(p1.rect.x + 17, p1.rect.y))
				 	fire = pygame.time.get_ticks()
				 	

		if keyp[pygame.K_RIGHT]:
			p1.move("right")

		elif keyp[pygame.K_LEFT]:
			p1.move("left")

		else:
			
			p1.move("center")
			
		for alien in pygame.sprite.groupcollide(shots_list, alien_list,1,1):
			
			n1 += 1
			alien.kill()
			fire_list.add(explosion(alien.rect.x - 20, alien.rect.y - 45))
			fire_list.update()

		bomb_reload +=1

		if bomb_reload == 10 :
			bomb_rand = random.randint(1,100)

			if bomb_rand >= 80 and bomb_rand <= 100 and len(alien_list) > 0:
				bomb_list.add(Bomb(pygame.sprite.Group.sprites(alien_list)[-1].rect.x,pygame.sprite.Group.sprites(alien_list)[-1].rect.y))
			
			bomb_reload = 0

		for player in pygame.sprite.groupcollide(bomb_list, player_list, 1, 1):
			sys.exit()

		for bossss in pygame.sprite.groupcollide(boss_list, shots_list, 0, 1):
			fire_list.add(explosion(bossss.rect.x + 80, bossss.rect.y + 80))
			fire_list.update()


		pygame.display.update()
		p1.update()
		player_list.update()
		shots_list.update()
		fire_list.update()
		bomb_list.update()
		boss_list.update()
		window.fill(pygame.Color(33,33,33))

		window.blit(BackGround.image, BackGround.rect)
		score(str(n1))
		alien_list.draw(window)
		player_list.draw(window)
		shots_list.draw(window)
		bomb_list.draw(window)
		boss_list.draw(window)
		fire_list.draw(window)

		pygame.display.flip() 
		clock.tick(60)
			
if __name__ == '__main__': 
	main()