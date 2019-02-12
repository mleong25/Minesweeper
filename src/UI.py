#This is the UI, it will handle the initial screen in which the User chooses the size of the board and number of mines
import pygame

from src.Gameboard import Gameboard
from src.Styles import Styles

class UI:

    def __init__(self, display):
        self.display = display

    def start_game(self,board_size,number_of_mines):

        self.board_size = int(board_size)
        self.number_of_mines = int(number_of_mines)

        clock = pygame.time.Clock() #adds clock imported from pygame

        game_board = Gameboard(board_size, number_of_mines, self.display)

        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.QUIT:
                    exit()
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    position = pygame.mouse.get_pos()
                    print(position)
                    game_board.rec_reveal(position[0], position[1])
                elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                    position = pygame.mouse.get_pos()
                    print(position)
                    #Tile.tile_flag(position[0], position[1])
                
        
            game_board.draw()
        pygame.display.flip()

        # pygame.display.update()
        clock.tick(30)

        # display = pygame.display.set_mode(
        #     (Styles['game']['width'],
        #     Styles['game']['width'])
        # )

		#Use a loop to obtain valid user input
		#while board_size < 2:
		#	print ("Enter board dimension (>= 2): ")
					#obtain user input for board_size

		#once a valid board size is obtain, get number of mines
		#while number_of_mines < 1:
			#        print ("Enter number of mines (>=1): ")
					#obtain user input for number_of_mines

			#Creates an instance of Gameboard -- call board_generator
                
			#Call run_game function -- we might have to make this a global variable so run_game can access the game board
			#run_game()

    def run_game():

        #game_victory = false
        #game_lost = false
        
			#Uses a loop to call is_not_mine (called when user clicks a tile)
			#while not game_victory or not game_lost:
					#obtain user input from clicking a tile (both right and left click)
                
					#call is_not_mine (a function in Gameboard that will call rec_reveal)
                
					#If all tiles are revealed (check every iteration), break the loop, user has won

					#If a mine is hit (is_not_mine returns false), break the loop, user has lost

					#Continues until a mine is hit or all tiles are revealed

        screen = pygame.screen.set_mode(
            (Styles['start_screen']['width'],
            Styles['start_screen']['width'])
        )

    def right_click():
        # to be defined
        click = 0 #some dummy code to make code work


