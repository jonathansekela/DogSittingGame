#!/usr/bin/env python

#@todo: get mysql db connection going
import mysql.connector as conn
import pygame as pg
import random
import spritesfunctions as sf
import button
import dog
pg.init()

#region setup
SCREEN_WIDTH = 928
SCREEN_HEIGHT = 793
BACKGROUND = pg.image.load('.\\Backgrounds\\Free Pixel Art Forest\\Preview\\Background.png')

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('what da dog doin?')
random.seed()

game_running = True
menu_running = True
#endregion

#region game menu

#load button images
start_img = pg.image.load('.\\Menu Buttons\\Large Buttons\\Large Buttons\\Play Button.png').convert_alpha()
stop_img = pg.image.load('.\\Menu Buttons\\Large Buttons\\Large Buttons\\Quit Button.png').convert_alpha()

#create button instances
start_button = button.Button(200, 100, start_img, .8)
quit_button = button.Button(200, 400, stop_img, .8)

#menu loop
while menu_running:
	screen.fill((202, 228, 241))

	if start_button.draw(screen):
		menu_running = False
	if quit_button.draw(screen):
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
goodboi_dest = (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 160)
goodboi = dog.Dog(dog.Directions.LEFT.value, dog.Actions.STAND_IDLE.value, goodboi_dest)

last_update = pg.time.get_ticks()
action_change_time = goodboi.get_animation_cooldown() * random.randint(1, 10) * 5

while game_running:
	#update background
	screen.blit(BACKGROUND, (0, 0))
	
	#change goodboi action at random intervals between .5 and 5 seconds
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
					print("good boy!")
				else:
					print("incorrect time for reward")
	
	pg.display.update()
#endregion

pg.quit()