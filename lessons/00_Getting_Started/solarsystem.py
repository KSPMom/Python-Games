import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
d_T = 1 # timestep (delta time)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Solar System")

class Planet:
    def __init__(self, x_pos: float, y_pos: float, x_vel: float, y_vel: float, color: tuple, radius: int, mass: int):
        self.color = color
        self.radius = radius
        self.mass = mass
        self.force = pygame.Vector2(0, 0)
        self.pos = pygame.Vector2(x_pos, y_pos)
        self.vel = pygame.Vector2(x_vel, y_vel)
        self.acl = pygame.Vector2(0, 0)
        
    def update(self):
        
        
        self.force = 
        self.acl += self.force
        self.vel += self.acl * d_T
        self.pos += self.vel * d_T
        pygame.draw.circle(screen, self.color, self.pos, self.radius)



# Main loop
running = True

# things
earth = Planet(100, 300, 0, -0.01, (0,0,255), 10, 100)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            running = False
         
    

    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255, 255, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 50)
    earth.update()
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
