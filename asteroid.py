from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.containers = Asteroid.containers
        super().__init__(x, y, radius)
        #self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):        
        self.position += self.velocity * dt

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_split_angle = random.uniform(20, 50)
            direction_asteroid1 = self.velocity.rotate(rand_split_angle)
            direction_asteroid2 = self.velocity.rotate(-rand_split_angle)
            asteroid1_new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid2_new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, asteroid1_new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, asteroid2_new_radius)
            new_asteroid1.velocity = direction_asteroid1 * 1.2
            new_asteroid2.velocity = direction_asteroid2 * 1.2