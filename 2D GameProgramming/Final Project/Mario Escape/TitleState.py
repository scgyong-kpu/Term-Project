from pico2d import *
from Background import *
from Button import *
import GameFramework
import GameWorld

capture = None

def enter():
	build_title_state()

def update():
	GameWorld.update()

def draw():
	GameWorld.draw()

def handle_event(event):
	global running

	if (event.type == SDL_QUIT):
		GameFramework.quit()

	if (handle_mouse(event)):
		return

def build_title_state():
	GameWorld.title_init(["background", "ui"])

	background = Background("Image/Title.png")
	GameWorld.add(GameWorld.layer.background, background)

	start_button = Button(0, 180, 300, 620, 300, GAME_START)
	GameWorld.add(GameWorld.layer.ui, start_button)

	des_button = Button(0, 90, 300, 620, 200, DESCRIPTION)
	GameWorld.add(GameWorld.layer.ui, des_button)

	exit_button = Button(100, 0, 100, 620, 100, EXIT)
	GameWorld.add(GameWorld.layer.ui, exit_button)

	GameWorld.curr_objects = GameWorld.title_objects

	global bgm
	
	bgm = load_music("SOUND/title theme.mp3")
	bgm.set_volume(100)
	bgm.repeat_play()

def handle_mouse(event):
	global capture

	if (capture != None):
		holding = capture.handle_event(event)

		if (not holding):
			capture = None
		
		return True

	for object in GameWorld.objects_at(GameWorld.layer.ui):
		if (object.handle_event(event)):
			capture = object

			return True

	return False

def exit():
	Image.unload("Image/Title.png")
	Image.unload("IMAGE/TitleMenu.png")
	GameWorld.clear()

	global bgm

	bgm.stop()
	del bgm

def pause():
	pass

def resume():
	build_title_state()

if (__name__ == "__main__"):
	GameFramework.run_main()