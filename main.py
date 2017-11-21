import pyglet
from Juego import Juego

#Creamos la clase ventana para mostrar nuestro juego, le pasamos 2 objetos
class Ventana(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(400,100)
        self.frame_rate = 1/60.0
        #Llamamos a nuestra imagen de la nave y se la pasamos al jugador
        self.jugador = Juego(500,100, 'nave.png')

        #img = pyglet.image.load('nave.png')
        #self.jugador = pyglet.sprite.Sprite(img, x=500, y=200)

    def on_draw(self):
        self.clear()
        self.jugador.draw()

    def update(self, dt):
        self.jugador.update(dt)

#Condición para que compruebe en que tipo de ventana estamos y que nos pinte una interfaz de 1200x900
if __name__ =="__main__":
    window = Ventana(1200, 900, "Space Invaders", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()