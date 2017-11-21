import pyglet

class Juego:
    def __init__(self, posx, posy, img=None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if img is not None:
            img = pyglet.image.load(img)
            self.sprite = pyglet.sprite.Sprite(img, x=self.posx, y=self.posy)

    def draw(self):
        self.sprite.draw()

#Mueve de izquerda a derecha la nave
    def update(self, dt):
        self.sprite.x += 150*dt
        self.sprite.y += 0*dt