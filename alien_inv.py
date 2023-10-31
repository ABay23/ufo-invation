import sys
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        
        #* Controlling the frame rate
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('UFOs viteh')
        
        #Set Background Color
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                self.screen.fill(self.bg_color)
                
                pygame.display.flip()
                self.clock.tick(60)
                

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()