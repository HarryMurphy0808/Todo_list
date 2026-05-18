import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 900))
background_color = (30, 30, 30)

def main():
    running = True
    while running:
        screen.fill(background_color)
        title_font = pygame.font.SysFont('Arial', 48)
        title_text = title_font.render('To-Do List', True, (255, 255, 255))
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 50))
        
        button_font = pygame.font.SysFont('Arial', 36)
        add_button = button_font.render('Add Task', True, (255, 255, 255))
        
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
main()
    

