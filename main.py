# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def draw_text(screen, font_pose, text='No text', font_size=10, font_name='DejaVuSans.ttf', font_color= (0,0,0), italic=False, bold=False):
    pygame.font.init()
    font = pygame.font.Font(font_name, font_size)
    font.set_italic(italic)
    font.set_bold(bold)
    img = font.render(text, False, font_color)
    screen.blit(img, font_pose)

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    background_image = pygame.image.load('saturn_family1.jpg').convert()
    player_image = pygame.image.load('player.png').convert()
    player_image.set_colorkey(config.BLACK)
    clock = pygame.time.Clock() # Initialize the clock here
    running = True
    while running:
        running = handle_events()
#        screen.fill(config.WHITE) # Use color from config
        pygame.display.flip()
        player_post = pygame.mouse.get_pos()
        x = player_post[0]
        y = player_post[1]
        x = player_post[0] - 99 // 2
        y = player_post[1] - 75 // 2
        
        screen.blit(background_image, [0,0])
        screen.blit(player_image, [x,y])
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

        

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()
