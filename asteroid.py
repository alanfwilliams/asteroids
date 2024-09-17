from circleshape import CircleShape
from pygame.draw import circle


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        circle(screen,"white",self.position,self.radius,2)
    
    def update(self, dt):
        self.position += (dt * self.velocity)