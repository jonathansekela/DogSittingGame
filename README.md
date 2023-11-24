# Dog Sitting Game Planning Sheet

## Game Dev Plan
- needs backend. python to mysql backend.
	- testdb in mysql server community version localhost server (for now)
- start menu with name of game and play or quit button
- tutorial explaining what the game's about?
- the game:
	- a dog is standing there, hanging out.
	- you tell the dog to sit
	- the dog sits after a random time
	- you press the 'reward' button
		- time it takes between sit and reward is recorded and sent to db
	- at end of game, show their score

## elements of the program
3 parts to every game:
1. window
2. game loop
3. event handler

the big parts of this game:
1. sprite animations
	- stand, lick, sit
2. random time pass
	- a random double value translated to seconds - 1-5 seconds
3. menu
4. user interactions
	- click buttons
	- command sit
	- give reward

## organizing the code
- sprite sheet
- sprite animation
- main
	- event handler
	- game loop
	- window