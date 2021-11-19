import pygame
import sys


'''         how to write the slides

1. This code is made to make
		a slide with a question
		next slide with the answer

2. How to separate the text of one slide from the others?
	Put an empty line in between

3. How to put an image?
	001.png,100,300

where 100 is the x and 300 is the y

4. Can I fit the screen with an image?

	Yes, like this, with the -1 at the end
	001.png, 100, -1

The image will be big as the screen

5. How can I go to next slide...?
	whit arrow key or mouse button right and left

6. Can I change the text size?
	Yes, with the mousewheel

'''
# THIS WILL BE A LIST OF STRINGS, SEPARATED BY THE EMPTY LINE HERE
text_for_slides = """5CE Pianificazione

D: Cos'è la pianificazione?

Le imprese devono prendere delle decisioni
prima sul lungo termine, strategiche,
preparando dei piani con le previsioni
su beni da acquistare (piani di investimento),
fonti di finanziamento (piani finanziari),
sugli utili futuri (piano economico) e
sulla composizione del patrimonio futuro

D: Come possono essere le previsioni?

le previsioni possono essere
- di espansione
- di consolidamento
- di ridimensionamento

001.png, 0,-1

FINE
"""

# A LIST OF STRINGS, EACH STRING IS A SLIDE SEPARATED BY EMPTY LINE ABOVE
text_for_slides = text_for_slides.split("\n\n")
# THE COUNTER AT THE TOP OF THE SLIDES
text_for_slides = [str(int((n / 2) + 0.5)) + f"/{(len(text_for_slides) - 1) // 2}" "\n" + page for n, page in enumerate(text_for_slides)]
counter = 0

pygame.init()
class Presenter:
	def __init__(self, text):
		self.screen = pygame.display.set_mode((1000,600), pygame.RESIZABLE)
		self.clock = pygame.time.Clock()
		self.title_font_size = 64
		self.slides_counter = 0
		self.font_init(text)
		self.mainloop()

	def mainloop(self):
		"This runs until you quit or escape"
		self.game = 1 # bool that if 1 the game goes on
		while self.game:
			for event in pygame.event.get():
				self.game = self.check_exit(event) # quit or escape
				self.event_listener(event)
			# self.update_screen()
			pygame.display.update()
			self.clock.tick(30)
		self.quit() # exit from the game

	def update_screen(self):
		self.screen.blit(self.title_surface, (30, 50))

	def quit(self):
		''' Exit from the game '''
		pygame.quit()
		sys.exit()

	def check_exit(self, event):
		''' Check if user presses quit or escape'''
		quit = event.type == pygame.QUIT
		exit = event.type == pygame.KEYDOWN  and event.key == pygame.K_ESCAPE
		if quit or exit:
			self.game = 0
		return self.game

	def go_on(self):
		if self.slides_counter < len(text_for_slides) - 1:
			self.slides_counter += 1

	def go_back(self):
		if self.slides_counter > 0:
			self.slides_counter -= 1

	def event_listener(self, event):
		"Makes the slides go on with right, back with left"
		self.key_events(event)
		self.mouse_events(event)
		self.font_init(text_for_slides[self.slides_counter])

	def key_events(self, event):
		''' move throught presentation with arrow keys '''
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				self.go_on()
			if event.key == pygame.K_LEFT:
				self.go_back()
				self.screen.fill((0, 0, 0))
			

	def mouse_events(self, event):
		''' control with the mouse: font size and slide back and forward '''
		if event.type == pygame.MOUSEBUTTONDOWN:
			self.change_font_size(event)
			self.mouse_move(event)

	def mouse_move(self, event):
		''' go on and back with mouse click '''
		if event.button == 3:
			self.go_on()
		if event.button == 1:
			self.go_back()

	def change_font_size(self, event):
			''' mousewheel changes size of text '''
			if event.button == 4:
				self.title_font_size += 6
			elif event.button == 5:
				self.title_font_size -= 6
			# self.font_init(text_for_slides[self.slides_counter])

	def font_init(self, text):
		"Show text in different rows if there is a #"
		self.text = text
		self.title_font = pygame.font.SysFont("Arial", self.title_font_size)
		self.top_font = pygame.font.SysFont("Arial", 24)
		# GET THE WIDTH AND HEIGHT OF THE SCREEN
		self.win_w, self.win_h = pygame.display.get_surface().get_size()
		# MAKE A SURFACE LIKE THE SCREEN
		self.title_surface = pygame.Surface((self.win_w, self.win_h))
		offsetx = 0
		offsety = 0
		# SPLIT THE TEXT INTO LINES
		text = text.split("\n")
		# GET THE NUMBER OF LINES IN THE TEXT
		num = len(text)
		num_sld = len(text_for_slides)
		for m, self.row in enumerate(text):
			if m == 0:
				# scritta verde
				self.row = self.top_font.render("_"*(self.slides_counter) + self.row, 0, (0, 255, 0))

			else:
				# You can put images in a slide, with position with offsetx and offsety
				if ".png" in self.row:
					# example
					# 001.png,100,200
					# image, x, y # where x and y are the position on the screen
					image, offsetx, offsety = self.row.split(",")
					image = image.replace(" ", "") # avoid spaces if there
												   # are at start of the line 
					if offsety == "-1":
						print("offsety =", offsety)
						# the screen is 1000x600
						self.row = pygame.image.load(f"{image}")
						x, y = self.row.get_size()
						rx = self.win_w / x
						ry = self.win_h / y
						print(rx)
						print(ry)
						ratio = rx if rx < ry else ry
						self.row = pygame.transform.scale(self.row, (int(x*rx), int(y*rx)))
						offsety = 50
						offsetx = int(offsetx)
					else:
						offsetx = int(offsetx)
						offsety = int(offsety)
						self.row = pygame.image.load(f"{image}")
				else:
					self.row = self.title_font.render(self.row, 0, (255, 255, 255))
			self.title_surface.blit(self.row, (0 + offsetx, 0 + offsety))
			# vertical space among text
			offsety += self.title_font_size


		self.screen.blit(self.title_surface, (0, 0))


# Put an introduction that will be seen only once at the start
Presenter("""Usa le frecce per scorrere il testo

- Freccia a sinistra e destra
  per andare indietro/avanti

- rotellina del mouse per
  modificare la grandezza
  del carattere""")
