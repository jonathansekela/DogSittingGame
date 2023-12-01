#!/usr/bin/env python

#@todo: get mysql db connection going
import mysql.connector as conn
import pygame as pg
from pygame import mixer
import random
import button
import dog
import sqlconn

#mixer allows us to load sounds
pg.mixer.pre_init(44100, -16, 2, 512)#I have no idea what these mean, Coding with Russ set these arguments like this
mixer.init()
pg.init()

#region general setup
SCREEN_WIDTH = 928
SCREEN_HEIGHT = 793
BACKGROUND = pg.image.load('./Backgrounds/Free Pixel Art Forest/Preview/Background.png')

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Sit, Boy!')
random.seed()

game_running = True
menu_running = True
#endregion

#region sqlconn setup
sqlConnector = sqlconn.SqlConn("localhost", "root", "Thug4Lyfe")
#endregion

#region game menu

#load button images
start_img = pg.image.load('./Menu Buttons/Large Buttons/Large Buttons/Play Button.png').convert_alpha()
stop_img = pg.image.load('./Menu Buttons/Large Buttons/Large Buttons/Quit Button.png').convert_alpha()

#create button instances
start_button = button.Button(200, 100, start_img, .8)
quit_button = button.Button(200, 400, stop_img, .8)

#load menu music
pg.mixer.music.load('Music/Abstraction - Ludum Dare 28 Loops/Ludum Dare 28 - Track 1.wav')
pg.mixer.music.set_volume(.5)#50% original volume
pg.mixer.music.play(-1, 0.0, 5000)

#load menu sounds
confirm_fx = pg.mixer.Sound('sfx/menu/confirm tones/confirm_style_2_001.wav')
back_fx = pg.mixer.Sound('sfx/menu/back tones/back_style_2_001.wav')
error_fx = pg.mixer.Sound('sfx/menu/error tones/error_style_2_001.wav')
cursor_fx = pg.mixer.Sound('sfx/menu/cursor_style_2.wav')

#menu loop
while menu_running:
	screen.fill((202, 228, 241))

	#@todo: cursor_fx currently plays 6 seconds repeating as long as colliding with button. Cut the sfx down and make it only play once per mouseover.
	# if start_button.rect.collidepoint(pg.mouse.get_pos()) or quit_button.rect.collidepoint(pg.mouse.get_pos()):
	# 	cursor_fx.play()
	if start_button.draw(screen):
		confirm_fx.play()
		menu_running = False
	if quit_button.draw(screen):
		back_fx.play()
		menu_running = False
		game_running = False

	#event handler
	for event in pg.event.get():
		#quit game
		if event.type == pg.QUIT:
			menu_running = False
			game_running = False

	pg.display.update()
#endregion

#region game loop

#load game music
pg.mixer.music.load('Music/Abstraction - Ludum Dare 28 Loops/Ludum Dare 28 - Track 8.wav')
pg.mixer.music.set_volume(.5)#50% original volume
pg.mixer.music.play(-1, 0.0, 5000)

#load game sounds
reward_fx = pg.mixer.Sound('sfx/game/MI_SFX 43.wav')

goodboi_dest = (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 160)
goodboi = dog.Dog(dog.Directions.LEFT.value, dog.Actions.STAND_IDLE.value, goodboi_dest)

last_update = pg.time.get_ticks()
action_change_time = goodboi.get_animation_cooldown() * random.randint(1, 10) * 5

while game_running:
	#update background
	screen.blit(BACKGROUND, (0, 0))
	
	#change goodboi action at random intervals between .5 and 5 seconds
	#@todo: make update pause when goodboi.is_sitting(), keep track of time between sit and reward
	current_time = pg.time.get_ticks()
	if current_time - last_update >= action_change_time:
		goodboi.change_action_random()
		last_update = current_time
		action_change_time = goodboi.get_animation_cooldown() * random.randint(1, 10) * 5

	#update animation
	goodboi.update_animation(screen)

	#event handler
	for event in pg.event.get():

		if event.type == pg.QUIT:
			game_running = False
		if event.type == pg.KEYDOWN:
			#change dog direction
			if event.key == pg.K_LEFT:
				goodboi.turn_left()
			elif event.key == pg.K_RIGHT:
				goodboi.turn_right()
			#change dog action
			elif event.key == pg.K_SPACE or event.key == pg.K_0:
				goodboi.lick()
			elif event.key == pg.K_1:
				goodboi.walk()
			elif event.key == pg.K_2:
				goodboi.run()
			elif event.key == pg.K_3:
				goodboi.sit()
				goodboi.sit_idle()
			elif event.key == pg.K_4:
				goodboi.stand()
				goodboi.stand_idle()
			#user action handlers
			elif event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
				if goodboi.is_sitting():
					reward_fx.play()
					print("good boy!")
				else:
					error_fx.play()
					print(dog.Actions(goodboi.get_action()).name, ": incorrect time for reward")
			#test db conn
			elif event.key == pg.K_i:
				#@todo: the insert works!
				print("inserting into test_deez...")
				sqlConnector.insert("", "")
			elif event.key == pg.K_s:
				print("selecting from test_deez..")
	
	pg.display.update()
#endregion

pg.quit()