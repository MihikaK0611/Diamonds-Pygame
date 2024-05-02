import pygame
import sys
import os

class UI:
    def __init__(self, game):
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.card_images = self.load_card_images()
    
    def load_card_images(self):
        card_images = {}
        suits = ['hearts', 'spades', 'clubs', 'diamonds']
        for suit in suits:
            card_images[suit] = {}
            for value in range(2, 15):
                filename = f'{value}_of_{suit}.png'
                image_path = os.path.join(suit, filename)
                if os.path.exists(image_path):
                    card_images[suit][value] = pygame.image.load(image_path)
                else:
                    print(f"Warning: Image not found for {filename}. Using placeholder image.")
                    # You can set a placeholder image here
                    # For simplicity, let's set it to None
                    card_images[suit][value] = None
        return card_images

    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.draw_board()
            pygame.display.flip()
            self.clock.tick(60)
        
        self.game.calculate_scores()
        pygame.quit()
        sys.exit()
    
    def draw_board(self):
        self.screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 36)
        text = font.render("Diamonds Game", True, (0, 0, 0))
        self.screen.blit(text, (300, 50))
        self.draw_scores()
        self.draw_cards()
    
    def draw_scores(self):
        font = pygame.font.SysFont(None, 24)
        for i, score in enumerate(self.game.scores):
            text = font.render(f"Player {i+1}: {score}", True, (0, 0, 0))
            self.screen.blit(text, (50, 100 + i * 50))
    
    def draw_cards(self):
        card_spacing = 20
        x_offset = 50
        y_offset = 200
        for i, hand in enumerate(self.game.hands):
            for j, card in enumerate(hand):
                suit, value = card
                image = self.card_images[suit.lower()].get(value)
                if image:
                    x = x_offset + j * (image.get_width() + card_spacing)
                    y = y_offset + i * (image.get_height() + card_spacing)
                    self.screen.blit(image, (x, y))
                else:
                    print(f"Warning: Image not found for {value} of {suit}")
